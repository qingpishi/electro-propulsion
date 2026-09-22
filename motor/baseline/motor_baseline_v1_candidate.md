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
| Aluminium secondary thickness | **16 mm** | **FROZEN** |
| Slot size | 42 x 60 mm | CONDITIONAL |
| Yoke thickness | 80 mm | CONDITIONAL |
| Equivalent turns per slot side | 8 | CONDITIONAL |

## 16 mm secondary baseline decision — 2026-09-22

The aluminium secondary thickness is now **FROZEN at 16 mm** for the 40 m/s design authority.

This decision freezes **thickness only**. It does not freeze the previously studied two-piece 2 x 2.9 m split, the 2-3 mm centre joint, or the current secondary length/width architecture.

The prior 12 mm electrical operating points, including the 2.44 Hz / 1430 A capability point and the 3.0-4.0 Hz operating band, are retained only for traceability until a fresh 16 mm calculation is completed.

## 40 m/s operating-point baseline

### System nominal thrust requirement

For the current 12 t launch mass, 50 deg incline and 3g net acceleration:

- Total nominal electromagnetic thrust requirement: **443.2 kN**
- Per physical DSLIM channel: **221.6 kN**

This is a **system requirement**, not yet a frozen motor electrical operating point. The current/slip/voltage/PF combination used to meet 443.2 kN remains OPEN.

### 500 kN design capability — current authoritative thrust evidence

The current high-resolution 2D moving-conductor fixed-current scan at 40 m/s gives:

- Current per stator face: **1430 A RMS**
- Maximum-thrust slip frequency: **2.44 Hz**
- Maximum-thrust plateau: approximately **2.3–2.6 Hz**
- Supply frequency at 2.44 Hz slip: **42.44 Hz**
- Slip ratio: **~5.75%**
- Thrust: **250.068 kN/channel**
- Total two-channel thrust: **500.136 kN**

Therefore the 500 kN thrust capability is supported by the current fixed-current 2D model.

However, **voltage, PF, efficiency and loss are not frozen at this 2.44 Hz point**. They require a self-consistent constant-thrust optimization and final winding end-leakage closure.

### Historical 3 Hz engineering reference

At 40 m/s, 3 Hz slip and 1430 A/face, the latest high-resolution thrust scan gives:

- Supply frequency: **43 Hz**
- Slip ratio: **~6.98%**
- Thrust: **242.361 kN/channel**
- Total thrust: **484.722 kN**

Older electrical reference values retained for traceability:
- Line-line voltage per face: ~2.74 kV RMS
- Power factor: ~0.87
- Single-channel efficiency: ~85.6%
- Tooth B95: ~1.31 T
- Yoke B95: ~1.20 T

These older electrical values are **LEGACY REFERENCE values only**. Do not combine them with the 2.44 Hz maximum-thrust point.

### Current operating-point baseline band

The 40 m/s normal operating baseline is defined as a **range**, not a single slip-frequency point:

- Normal operating slip band: **3.0-4.0 Hz**
- Preferred operating sub-band: **3.3-3.7 Hz**
- Reference center only: **~3.4 Hz**
- Maximum-force/minimum-current reserve band: **2.3-2.6 Hz** (not normal baseline)

At 40 m/s and tau = 0.5 m, the normal band corresponds to:
- Supply frequency: **43.0-44.0 Hz**
- Slip ratio: **~6.98-9.09%**

For the **443.2 kN nominal total-thrust requirement**, the current engineering scan across 3.0-4.0 Hz gives approximately:
- Current: **1.365-1.514 kA RMS/face**
- V4 conservative line-line voltage: **~3.04 down to 2.71 kV/face**
- V4 conservative PF: **~0.728-0.761**
- Channel efficiency: **~85.2%-83.1%**
- Total two-channel motor loss: **~3.08-3.62 MW**

For the **500 kN design-capability case**, the same band gives approximately:
- Current: **1.453-1.612 kA RMS/face**
- V4 conservative line-line voltage: **~3.23 down to 2.88 kV/face**
- V4 conservative PF: **~0.728-0.761**
- Channel efficiency: **~85.1%-83.0%**
- Total two-channel motor loss: **~3.49-4.10 MW**

The preferred **3.3-3.7 Hz** sub-band gives the best practical balance of converter voltage margin, PF, current and efficiency.

Recommended preliminary main CHB envelope remains:
- **3.3 kV class — CONDITIONAL**
- **1.8 kA pulse current class per stator face — CONDITIONAL**

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

The baseline aluminium thickness is now **16 mm**.

A **two-piece (2 x 2.9 m) secondary with a 2-3 mm centre gap and common mechanical carrier** remains ANALYSIS ONLY. The thickness decision does not by itself select that split/joint architecture.

## Remaining V1.0 closure items

1. Local 3D transverse edge-effect validation for the 600 mm stator width.
2. 40 m/s three-main-segment + fourth-segment handover transient.
3. 3D/transient confirmation of the 14 mm-gap normal-force behavior.
4. Final 3.3 kV PWM form-wound insulation coordination.
5. Secondary structural/support validation.
