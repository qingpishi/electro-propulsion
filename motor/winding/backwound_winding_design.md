# DSLIM winding selection — back-wound winding

Status: **selected candidate; not yet manufacturing-frozen**

## Baseline
- 40 m/s design authority
- pole pitch 500 mm
- 2 m stator segment
- 24 slots / 4 poles / 3 phases
- q = 2
- slot pitch 83.333 mm
- 14 mm single-side air gap
- 8 equivalent turns per active slot side
- phase-belt sequence: A+, A+, C-, C-, B+, B+, A-, A-, C+, C+, B-, B-

## Selection
Selected topology: **back-wound / toroidal slot winding**.

A back-wound coil has one active conductor pack in the stator slot and a return conductor pack routed across the rear of the yoke, connected around the two transverse side edges.

## Why not direct tooth-concentrated winding

For the present slot/pole geometry, the electrical slot angle is 30 degrees.

The existing q=2 phase belt has fundamental distribution factor:

```
kd1 = sin(q*beta/2) / (q*sin(beta/2)) ~= 0.966
```

A one-slot-pitch tooth coil has fundamental pitch factor:

```
kp1 = sin(beta/2) = sin(15 deg) ~= 0.259
```

Therefore a direct tooth-concentrated replacement would need roughly 3.7 times the ampere-turn loading to recover the same fundamental field, before harmonic penalties. It would also change the spatial-harmonic spectrum seen by the aluminium plate secondary.

A concentrated winding could be reconsidered only together with a new slot/pole combination. That would be a new motor baseline, not a winding-only substitution.

## Preliminary coil package
- 8 turns per slot coil
- preliminary copper area per turn: ~88 mm2
- example conductor: rectangular formed copper ~8 x 11 mm, or electrically equivalent parallel construction
- current density at 1430 A: ~16.3 A/mm2
- current density at 1.8 kA pulse envelope: ~20.5 A/mm2
- CAD homogenized coil-pack envelope: ~34 mm x 28 mm in the slot

Each 2 m segment has 8 slot coils per phase, connected in series with physical coil orientation reversed as required by the +/- slot sign.

Each segment should retain independent U/V/W terminals so segment selection and fourth-segment pre-excitation remain possible.

## Manufacturing / integration
- Provide insulated rear winding channels behind the yoke.
- Keep rear copper clear of the primary structural load path.
- Support side end-turns against pulsed electromagnetic force.
- Use VPI or equivalent impregnation.
- Finalize conductor bend radius, turn insulation and main insulation with the conductor supplier.
- Rear winding accessibility is favorable for cooling and inspection.

## 3D model
A full one-channel 6 m STEP and a representative 2 m segment STEP have been generated. The copper bodies are homogenized 8-turn coil-pack envelopes suitable for packaging review and stranded-coil assignment in 3D FEM.

## Closure items
1. 3D end-winding leakage calculation.
2. Terminal voltage / PF correction including end leakage.
3. Final conductor cross-section and insulation build.
4. End-turn electromagnetic force / vibration.
5. Segment terminal and busbar layout.
6. Pulse thermal verification.
