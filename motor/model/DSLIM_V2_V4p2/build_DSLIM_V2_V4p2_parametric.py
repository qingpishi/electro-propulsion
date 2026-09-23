"""Generate the current DSLIM V2 + V4.2 parametric CAD.

Requires: cadquery
Default output: ./generated
Set DSLIM_MODEL_SEGMENTS=2 for the normal 6 m window or =3 for the
maximum handover envelope.
"""
import cadquery as cq
from cadquery import Vector
from pathlib import Path
import os, json, csv

OUT = Path(os.getenv("DSLIM_MODEL_OUT", "generated"))
OUT.mkdir(parents=True, exist_ok=True)
N_SEG = int(os.getenv("DSLIM_MODEL_SEGMENTS", "2"))
if N_SEG not in (2, 3):
    raise ValueError("DSLIM_MODEL_SEGMENTS must be 2 or 3")

# Accepted V2 geometry, mm.
SEG_L=3000.0; TAU=500.0; SLOTS=36; PITCH=SEG_L/SLOTS
SLOT_W=32.0; SLOT_D=79.0; YOKE_T=105.0; STATOR_W=800.0
SEC_L=4500.0; SEC_W=1200.0; SEC_T=16.0; GAP=14.0; TURNS=3

# V4.2 winding model geometry.
FACE_Z=SEC_T/2+GAP
SLOT_Z1=FACE_Z+SLOT_D
YOKE_Z1=SLOT_Z1+YOKE_T
PACK_W=24.0; PACK_H=46.0; PACK_Y=770.0
ZACTIVE=FACE_Z+8+PACK_H/2
SIDE=STATOR_W/2
END_Y=SIDE+60
END_HALF=12.0
END_T=10.0
LAYER_PITCH=12.0
END_Z0=ZACTIVE+24
R=5.0
START_MAP={0:("A",+1),1:("A",+1),2:("C",-1),3:("C",-1),4:("B",+1),5:("B",+1)}
PHORDER=["A","C","B"]
PHCOL={"A":cq.Color(0.88,0.13,0.08),"B":cq.Color(0.10,0.52,0.14),"C":cq.Color(0.08,0.30,0.90)}
CORECOL=cq.Color(0.34,0.36,0.40)
ALCOL=cq.Color(0.73,0.76,0.80)

def box(dx,dy,dz,cx,cy,cz):
    return cq.Workplane("XY").box(dx,dy,dz).translate((cx,cy,cz)).val()

def cyl(a,b,r=R):
    av=Vector(*a); bv=Vector(*b); v=bv-av
    return cq.Solid.makeCylinder(r,v.Length,av,v.normalized())

def tube(points,r=R):
    sh=[cyl(a,b,r) for a,b in zip(points[:-1],points[1:])]
    for p in points[1:-1]:
        sh.append(cq.Solid.makeSphere(r,Vector(*p)))
    return sh

def core_top():
    zslot=(FACE_Z+SLOT_Z1)/2
    teeth=box(SEG_L,STATOR_W,SLOT_D,SEG_L/2,0,zslot)
    for i in range(SLOTS):
        xc=(i+0.5)*PITCH
        teeth=teeth.cut(box(SLOT_W,STATOR_W+2,SLOT_D+2,xc,0,zslot))
    yoke=box(SEG_L,STATOR_W,YOKE_T,SEG_L/2,0,(SLOT_Z1+YOKE_Z1)/2)
    return cq.Compound.makeCompound([teeth,yoke])

def active(x):
    return box(PACK_W,PACK_Y,PACK_H,x,0,ZACTIVE)

def u_end(x1,x2,layer):
    z=END_Z0+layer*LAYER_PITCH
    ys=SIDE+14; yc=END_Y; ym=(ys+yc)/2
    leg=abs(yc-ys)
    sh=[
        box(2*END_HALF,leg,END_T,x1,ym,z),
        box(2*END_HALF,leg,END_T,x2,ym,z),
        box(abs(x2-x1),2*END_HALF,END_T,(x1+x2)/2,yc,z),
        cq.Solid.makeCylinder(END_HALF,END_T,Vector(x1,yc,z-END_T/2),Vector(0,0,1)),
        cq.Solid.makeCylinder(END_HALF,END_T,Vector(x2,yc,z-END_T/2),Vector(0,0,1)),
    ]
    for x in (x1,x2):
        pts=[
            (x,PACK_Y/2,ZACTIVE),
            (x,SIDE+14,ZACTIVE),
            (x,SIDE+34,z),
            (x,END_Y-END_HALF,z),
        ]
        sh += tube(pts)
    return sh

def build_top_winding():
    phase={p:[] for p in ("A","B","C")}
    rec={p:[] for p in ("A","B","C")}
    for period in range(3):
        base=period*12
        for k in range(6):
            s1=base+k+1; s2=s1+6
            p,sgn=START_MAP[k]
            x1=(s1-0.5)*PITCH
            x2=(s2-0.5)*PITCH
            phase[p] += [active(x1),active(x2)]
            phase[p] += u_end(x1,x2,k)
            xin,xout=(x1,x2) if sgn>0 else (x2,x1)
            rec[p].append({"x1":x1,"x2":x2,"xin":xin,"xout":xout})
    terminals=[]
    for ip,p in enumerate(PHORDER):
        cs=sorted(rec[p],key=lambda r:min(r["x1"],r["x2"]))
        ylane=-(SIDE+80+ip*36)
        zlane=YOKE_Z1-30+ip*16
        for j in range(len(cs)-1):
            xa=cs[j]["xout"]; xb=cs[j+1]["xin"]
            pts=[
                (xa,-PACK_Y/2,ZACTIVE),(xa,-SIDE-14,ZACTIVE),
                (xa,-SIDE-28,zlane),(xa,ylane,zlane),
                (xb,ylane,zlane),(xb,-SIDE-28,zlane),
                (xb,-SIDE-14,ZACTIVE),(xb,-PACK_Y/2,ZACTIVE)
            ]
            phase[p] += tube(pts)
        yl=-(SIDE+245)
        zl=YOKE_Z1+20+ip*18
        xls=110+ip*75; xle=SEG_L-110-ip*75
        for xsrc,xlug,label in [
            (cs[0]["xin"],xls,p+"1"),
            (cs[-1]["xout"],xle,p+"2")
        ]:
            pts=[
                (xsrc,-PACK_Y/2,ZACTIVE),(xsrc,-SIDE-14,ZACTIVE),
                (xsrc,-SIDE-28,zl),(xsrc,yl,zl),(xlug,yl,zl)
            ]
            phase[p] += tube(pts)
            phase[p].append(box(50,24,12,xlug,yl,zl))
            terminals.append({"phase":p,"terminal":label,"x":xlug,"y":yl,"z":zl})
    return {p:cq.Compound.makeCompound(phase[p]) for p in phase}, terminals

def xf(shape,tx=0,mirror_bottom=False):
    s=shape
    if mirror_bottom:
        s=s.rotate((0,0,0),(1,0,0),180)
    if tx:
        s=s.translate((tx,0,0))
    return s

core=core_top()
phases,terminals=build_top_winding()

audit=[
    ("active pack x clearance each slot side",(SLOT_W-PACK_W)/2,0,(SLOT_W-PACK_W)>0),
    ("active pack front clearance",(ZACTIVE-PACK_H/2)-FACE_Z,0,(ZACTIVE-PACK_H/2)>FACE_Z),
    ("active pack back clearance",SLOT_Z1-(ZACTIVE+PACK_H/2),0,SLOT_Z1>(ZACTIVE+PACK_H/2)),
    ("adjacent active pack x surface gap",PITCH-PACK_W,0,PITCH>PACK_W),
    ("end-turn layer surface gap",LAYER_PITCH-END_T,0,LAYER_PITCH>END_T),
    ("series phase-lane y surface gap",36-2*R,0,36>2*R),
    ("series phase-lane z surface gap",16-2*R,0,16>2*R),
    ("secondary to stator tooth-face airgap",GAP,0,GAP>0),
]

assy=cq.Assembly(name=f"DSLIM_V2_V4p2_{N_SEG}seg")
for si in range(N_SEG):
    tx=si*SEG_L
    assy.add(xf(core,tx=tx),name=f"CORE_SEG{si+1}_TOP",color=CORECOL)
    assy.add(xf(core,tx=tx,mirror_bottom=True),name=f"CORE_SEG{si+1}_BOTTOM",color=CORECOL)
    for p in ("A","B","C"):
        assy.add(xf(phases[p],tx=tx),name=f"WIND_SEG{si+1}_TOP_{p}",color=PHCOL[p])
        assy.add(xf(phases[p],tx=tx,mirror_bottom=True),name=f"WIND_SEG{si+1}_BOTTOM_{p}",color=PHCOL[p])

window=N_SEG*SEG_L
sec=box(SEC_L,SEC_W,SEC_T,window/2,0,0)
assy.add(sec,name="SECONDARY_AL_16MM_4P5M",color=ALCOL)

stem=f"DSLIM_V2_single_channel_{N_SEG}x3m_V4p2"
assy.export(str(OUT/(stem+".step")),exportType="STEP")
assy.export(str(OUT/(stem+".glb")),exportType="GLTF",tolerance=1.0,angularTolerance=0.3)

meta={
    "model_id":"DSLIM_V2_V4p2_3D_20260923",
    "segments":N_SEG,
    "configuration":"normal" if N_SEG==2 else "handover maximum simultaneous energized envelope",
    "segment_length_mm":SEG_L,
    "secondary_mm":[SEC_L,SEC_W,SEC_T],
    "stator_width_mm":STATOR_W,
    "slot_mm":[SLOT_W,SLOT_D],
    "yoke_mm":YOKE_T,
    "airgap_each_side_mm":GAP,
    "turns_equivalent":TURNS,
    "winding":"V4.2 adapted low-loop-area paired-slot back-connected",
    "non_overlap_analytic_audit_pass":all(x[3] for x in audit),
    "note":"Adjacent longitudinal segments are independent converter branches. The 3-segment model is a geometric/operational handover envelope, not a series electrical connection."
}
(OUT/(stem+"_metadata.json")).write_text(json.dumps(meta,indent=2),encoding="utf-8")
with (OUT/(stem+"_audit.csv")).open("w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["item","value_mm","required_mm","pass"])
    w.writerows(audit)
print("generated",stem,"audit_pass",all(x[3] for x in audit))
