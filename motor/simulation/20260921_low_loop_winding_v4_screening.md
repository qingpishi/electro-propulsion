# Low-loop-area winding V4 candidate

Status: **CONDITIONAL candidate; main baseline unchanged**

## Topology
V4 replaces each independent one-slot toroidal/back-wound coil with a paired-slot coil. Slots of the same phase and opposite current sign, separated by one pole pitch (500 mm), become the two active sides of one 8-turn coil. The air-gap-side current sheet remains unchanged. The 600 mm transverse rear return of each individual V3 coil is eliminated.

The practical CAD uses six end-turn layers to avoid overlap.

## Geometry
- active slot pack: 34 x 21 mm;
- paired active-side span: 500 mm;
- side end-turn center: 360 mm from stator centerline;
- flattened end-turn pack: about 48 x 10 mm;
- six end-turn layers;
- layer pitch: 12 mm;
- maximum end-turn lift: about 60 mm;
- 8 turns per paired coil;
- 88 mm2 preliminary conductor per turn;
- independent A1/A2, B1/B2, C1/C2 terminals remain per 2 m module.

## Slot pairing
Per 12-slot electrical period:
- A: (1,7), (2,8)
- C: (3,9), (4,10)
- B: (5,11), (6,12)

The pattern repeats for slots 13-24. This preserves:
A+, A+, C-, C-, B+, B+, A-, A-, C+, C+, B-, B-.

## Leakage screening
| Parameter | V3 | V4 practical | Change |
|---|---:|---:|---:|
| Free-space 6 m end leakage | 0.503 mH/ph | 0.446 mH/ph | -11.3% |
| High-mu screening bound | 1.369 mH/ph | 1.147 mH/ph | -16.3% |
| Main coil copper-path estimate, 2 m face | 302.3 m | ~238.2 m | -21.2% |

An aggressive compact six-layer layout can reach about 0.430 / 1.104 mH per phase, but has insufficient manufacturing space for the first prototype.

## Electrical implication
At 43 Hz / 1430 A, using the current 2D 2.74 kV / PF 0.87 reference:
- free-space correction: ~2.90 kV line-line, PF ~0.822;
- high-mu screening bound: ~3.19 kV line-line, PF ~0.748.

V4 therefore materially improves the chance that the 3.3 kV CHB envelope is sufficient, but nonlinear 3D FEA is still required before voltage-class freeze.

## Field tradeoff
Removing the transverse rear-return conductor lowers rear leakage field substantially, but moves leakage energy toward the transverse side end turns. Side structural steel and magnetic sensors therefore need re-evaluation.

## Classification
V4 is not a classical one-slot toroidal coil. It is a **low-loop-area paired-slot back-connected derivative** of the selected back-wound concept. It preserves the current slot-current electromagnetic baseline while changing the return-path topology.

Recommendation: use V4 as the preferred low-leakage winding candidate for nonlinear 3D validation. Do not merge into the main motor baseline yet.
