# DSLIM Motor Baseline — V1.0 Candidate

Status: **Conditionally frozen for 40 m/s design**

## Topology

- Dual-channel, double-sided long-primary linear induction motor
- Two physical DSLIM channels
- Four independently controlled stator faces
- Three phases per stator face
- Main longitudinal segments use equal-current operation

## Electromagnetic geometry

| Parameter | Value | State |
|---|---:|---|
| Pole pitch | 500 mm | FROZEN |
| Phases per stator face | 3 | FROZEN |
| q | 2 | FROZEN candidate |
| Basic stator segment | 2.0 m | FROZEN candidate |
| Poles per segment | 4 | Derived |
| Slots per segment | 24 | Derived |
| Main energized segments | 3 | FROZEN principle |
| Main energized length | 6.0 m | Derived |
| Secondary effective length | 5.8 m | CONDITIONAL |
| Stator effective width | 600 mm | CONDITIONAL |
| Single-side air gap | 14 mm | CONDITIONAL |
| Aluminium secondary thickness | 12 mm | CONDITIONAL |
| Slot size | 42 x 60 mm | CONDITIONAL |
| Yoke thickness | 80 mm | CONDITIONAL |
| Equivalent turns per slot side | 8 | CONDITIONAL |

## 40 m/s design point

Design thrust:
- Total: 500 kN
- Per channel: 250 kN

Current FEM reference at 40 m/s:
- Current per stator face: ~1.43 kA RMS
- Line-line voltage per stator face: ~2.74 kV RMS
- Power factor: ~0.87
- Single-channel efficiency: ~85.6%
- Tooth B95: ~1.31 T
- Yoke B95: ~1.20 T

Recommended preliminary main CHB envelope:
- **3.3 kV class**
- **1.8 kA pulse current class per stator face**

## Slip-frequency status

The slip-frequency controller is **not frozen**.

At 40 m/s and fixed ~1.43 kA per stator face, the current high-resolution scan gives:

- Peak thrust slip frequency: **~2.44 Hz**
- Peak thrust plateau: approximately 2.3–2.6 Hz
- Previous 3 Hz value: engineering operating reference only, not the maximum-thrust point

Therefore do not label 3 Hz as the maximum-thrust slip frequency.

A constant-thrust efficiency/PF/loss scan is still required before freezing the normal operating slip schedule.

## Segmentation principle

Normal main propulsion:
- Three adjacent 2 m segments form a 6 m main field window.
- Main segments carry equal current.

Handover:
- A fourth segment may be used for pre-excitation / takeover.
- Exact pre-excitation current and transfer circuit remain OPEN.
- The final handover design must preserve thrust continuity and must not rely on unequal main-segment current.

## 14 mm air-gap normal-force baseline

2D high-resolution validation at 40 m/s, 3 Hz and 1.43 kA RMS/face:
- centered absolute attraction: ~99.0 kN per stator face;
- residual restoring force: ~0.739 / 1.479 / 3.060 kN per channel at 0.25 / 0.50 / 1.00 mm eccentricity;
- equivalent lateral magnetic stiffness: ~-3.04 kN/mm/channel.

At the 2.44 Hz maximum-thrust slip region and the same current:
- centered absolute attraction rises to ~126 kN per stator face;
- residual force is ~1.71 kN at 0.5 mm and ~3.43 kN at 1.0 mm.

Use **130 kN per stator face** as the initial electromagnetic structural screening load before mechanical dynamic/safety factors.

The 2D model predicts restoring behavior. Do not credit that sign as a safety mechanism until 3D/transient validation.

## Secondary structural alternative under study

The main baseline remains the 12 mm continuous aluminium plate.

A **16 mm, two-piece (2 x 2.9 m) secondary with a 2-3 mm centre gap and common mechanical carrier** has passed preliminary 2D electromagnetic screening. It remains ANALYSIS ONLY pending 3D transverse-edge/joint validation and detailed structural FEA.

## Remaining V1.0 closure items

1. Local 3D transverse edge-effect validation for the 600 mm stator width.
2. 40 m/s three-main-segment + fourth-segment handover transient.
3. 3D/transient confirmation of the 14 mm-gap normal-force behavior.
4. Final 3.3 kV PWM form-wound insulation coordination.
5. Secondary structural/support validation.
