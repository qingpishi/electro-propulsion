# 16 mm split-secondary validation — 40 m/s baseline

Status: **analysis only; baseline not changed**

## Candidate
- Replace 12 mm continuous aluminium secondary with 16 mm aluminium.
- Split each 5.8 m channel secondary into two 2.9 m plates.
- Straight 2–3 mm centre gap.
- Both plates transfer force independently into one common carrier/frame.
- No conductive bridge across the gap in the first prototype concept.

## Electromagnetic method
- 2D longitudinal nonlinear moving-conductor FEM.
- 35WW300 engineering nonlinear B-H model.
- SUPG stabilization factor 0.05.
- High-resolution design checks use about 30.9k nodes / 60.6k triangles.
- Longitudinal end effect included.
- Transverse edge effect not included; 3D validation remains required.

## 16 mm thickness result
At fixed 1430 A/face and 40 m/s:
- 12 mm baseline maximum-thrust slip: about 2.44 Hz, about 250.1 kN/channel.
- 16 mm candidate maximum-thrust region: about 2.25–2.35 Hz, peak near 2.30 Hz.
- At the same 1430 A, 16 mm produces about 224.9 kN/channel at 2.30 Hz.

At 16 mm / 2.30 Hz, restored to 250 kN/channel:
- current: about 1513 A/face;
- line-line voltage: about 2.855 kV/face;
- PF: about 0.796;
- channel efficiency: about 84.95%;
- secondary loss: about 1.218 MW/channel;
- Btooth95: about 1.45 T;
- Byoke95: about 1.29 T.

Interpretation: 16 mm requires about 5.8% more current than the 12 mm maximum-thrust reference but remains within the preliminary 3.3 kV / 1.8 kA converter envelope.

## 2–3 mm centre-joint result
High-resolution comparisons against a seamless 16 mm plate at identical position:

| Secondary shift | 2 mm joint thrust delta | 3 mm joint thrust delta |
|---:|---:|---:|
| -0.25 m | +0.322% | +0.435% |
| 0.00 m | +0.016% | +0.014% |
| +0.25 m | +0.030% | +0.027% |

A coarser phase-position screening scan showed a conservative spread below about 1.3%.

The small positive/negative signs are not treated as a performance benefit; they are local current-redistribution/numerical interaction. The important result is that the 2–3 mm split does not create a material thrust penalty in the present 2D longitudinal model.

## Mechanical screening
Each 2.9 m x 0.918 m x 16 mm plate:
- mass: about 115 kg;
- nominal longitudinal force: about 125 kN per half plate;
- initial interface screening load: 200 kN per half plate.

Average stress estimates:
- full section at 200 kN: about 13.6 MPa;
- if force is carried only by the two ~159 mm side overhang strips: about 39.3 MPa before local stress concentration.

With about 0.5 m transfer/support pitch:
- 200 kN screening load gives about 33 kN per transfer station;
- about 17 kN per side.

Conservative 16 mm strip bending at 0.5 m support pitch:
- 5 kPa equivalent normal pressure: ~0.17 mm deflection;
- 10 kPa: ~0.35 mm;
- 20 kPa: ~0.69 mm.

Target structural support / force-transfer pitch should therefore be about 0.4–0.5 m if the local air-gap deflection target is <=0.3–0.5 mm.

## System impact
Compared with the 12 mm baseline, active aluminium mass increases by about 115 kg across the two propulsion channels.

If sled mass increases from 2.000 t to 2.115 t with all else unchanged:
- nominal 3g electromagnetic thrust rises from about 443.2 kN to about 447.4 kN;
- 500 kN design-thrust margin remains about 52.6 kN before any carrier/frame mass increase.

## Recommendation
Conditionally accept the following for next-stage validation:
- 16 mm aluminium conductor;
- two 2.9 m plates per channel;
- straight 2–3 mm centre gap;
- mechanically common, electrically unbridged;
- independent distributed force transfer into the common frame;
- ~0.4–0.5 m support / force-transfer pitch;
- thermal sliding features rather than fully locking each plate.

Do **not** change the main baseline yet.

Closure items:
1. 3D transverse-edge + centre-joint electromagnetic validation.
2. Recalibrate 14 mm-gap eccentricity/normal force and use it as the structural load.
3. Detailed carrier/frame and attachment FEA.
