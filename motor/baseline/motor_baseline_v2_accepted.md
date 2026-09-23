# DSLIM Motor Baseline — V2 Accepted 40 m/s Design

Status: **ACCEPTED BASELINE for 40 m/s design authority**

## 1. Topology and segmentation

- Dual-channel, double-sided long-primary linear induction motor.
- Four stator faces at the same longitudinal station are connected in series and carry the same three-phase current.
- Three longitudinal converter groups are interleaved:
  - A: G1, G4, G7, ...
  - B: G2, G5, G8, ...
  - C: G3, G6, G9, ...
- Basic stator segment: **3.0 m**.
- Normal travel repeatedly operates in **two-segment and three-segment energized states** as the 4.5 m secondary moves across the 3.0 m stator segmentation.
- Two adjacent energized segments provide a **6.0 m** stator window; three adjacent energized segments provide a **9.0 m** geometric stator window.
- The **three-segment full-current state is a recurring normal operating state, not only a brief handover envelope**. When the 4.5 m secondary is centered over a 3 m segment, the approximate longitudinal overlap is 0.75 m / 3.0 m / 0.75 m across the preceding / centered / following segments.
- The longitudinal segments are supplied by independent A/B/C converter branches; they are not electrically series-connected to one another.
- Effective secondary length: **4.5 m**.
- Reference current ramp during takeover: **10 ms (CONDITIONAL)**.
- At 40 m/s, the modulo-3 reuse geometry provides 1.5 m / 37.5 ms nominal converter reuse margin before acceleration correction.

## 2. Electromagnetic geometry

| Parameter | V2 value | State |
|---|---:|---|
| Pole pitch | 500 mm | FROZEN |
| Phases | 3 | FROZEN |
| q | 2 | FROZEN |
| Segment length | 3.0 m | FROZEN |
| Poles / segment | 6 | DERIVED |
| Slots / segment | 36 | DERIVED |
| Normal energized segments | **2 or 3, position-dependent** | FROZEN operational principle |
| Maximum simultaneous energized segments | **3** | FROZEN operational requirement |
| Geometric energized stator length | **6.0 or 9.0 m** | DERIVED |
| Secondary effective length | 4.5 m | FROZEN |
| Stator active width | 800 mm | FROZEN |
| Secondary active width | 1.2 m | FROZEN |
| Single-side air gap | 14 mm | FROZEN |
| Aluminium thickness | 16 mm | FROZEN |
| Slot | 32 x 79 mm | FROZEN |
| Tooth width | ~51.3 mm | DERIVED |
| Yoke thickness | 105 mm | FROZEN |
| Equivalent turns / slot side | 3 | FROZEN |
| Phase belt | A+, A+, C-, C-, B+, B+, A-, A-, C+, C+, B-, B- | FROZEN |

Two 4.5 m x 1.2 m x 16 mm aluminium secondaries contain approximately **466.6 kg** of active aluminium at 2700 kg/m3.


## 2.1 V4.2 winding baseline

Selected winding: **V4.2 low-loop-area paired-slot back-connected winding**.

Key geometry:
- pair span: **500 mm**;
- equivalent turns: **3**;
- homogenized three-turn active slot-pack envelope: **24 x 46 mm**;
- six non-overlapping end-turn layers, **12 mm** layer pitch;
- rounded side/end transitions;
- A/C/B phase-separated routing corridors;
- top and bottom stators use opposite +/-Y routing sides;
- final representative Boolean collision audit: phase-to-phase, winding-to-core and winding-to-secondary solid intersection volume = **0 mm3**.

The 24 x 46 mm active pack is a geometric envelope and must **not** be treated as solid copper. Current copper-loss calculations use a conditional **300 mm2 copper area per turn** (design range 280-320 mm2), with 80 degC copper as the engineering resistance reference.

### CAD-derived copper length and resistance - one 3 m stator face

| Phase | 3D copper path | R @20 degC, 300 mm2 | R @80 degC, 300 mm2 |
|---|---:|---:|---:|
| A | 57.641 m | 3.312 mOhm | **4.094 mOhm** |
| B | 61.943 m | 3.560 mOhm | **4.399 mOhm** |
| C | 62.951 m | 3.618 mOhm | **4.471 mOhm** |
| Average phase | 60.845 m | 3.497 mOhm | **4.321 mOhm** |

Four same-station stator faces are series-connected inside one longitudinal 3 m segment. Therefore one converter sees approximately:
- phase A: **16.374 mOhm**;
- phase B: **17.596 mOhm**;
- phase C: **17.882 mOhm**;
- average phase resistance: **17.284 mOhm**.

The three-phase copper-loss equivalent resistance for one energized 3 m longitudinal segment is:

`Rsum,1seg = RA + RB + RC = 51.852 mOhm`

For loss accounting:
- two simultaneously full-current longitudinal segments: **103.705 mOhm** equivalent;
- three simultaneously full-current longitudinal segments: **155.557 mOhm** equivalent.

Both are recurring operating states. The three-segment value is not merely a handover-only limit.

These latter values are **loss-equivalent sums across independent converter branches, not series terminal resistances**.

At 3.6 Hz using a 1.05 AC-resistance screening multiplier:
- 443.2 kN / 2.210 kA: **0.532 MW** for two full-current segments, **0.798 MW** for three;
- 500 kN / 2.345 kA: **0.599 MW** for two full-current segments, **0.898 MW** for three;
- 3.5 kA design envelope: **1.334 MW** for two full-current segments, **2.001 MW** for three (short-pulse screening only).

For handover with unequal segment currents, use:

`Pcu = 1.05 * Rsum,1seg * (I1^2 + I2^2 + I3^2)`

with currents in A and `Rsum,1seg = 0.051852 Ohm`.


### V4.2 end-region leakage inductance — 2026-09-23

The former **0.385 mH/phase** high-mu value came from geometry scaling of the earlier V4 winding and is now **superseded for current V4.2 design work**.

Current V4.2 extraction uses the actual six-layer end-turn geometry, phase-separated A/C/B routing corridors, series links and terminal leads. Active-slot conductors are excluded from the leakage integral so the 2D main-field inductance is not double-counted.

Per phase, per one 3 m longitudinal segment after the four same-station stator faces are series-connected:

| Treatment | Free-space | High-mu screening |
|---|---:|---:|
| Preferred, top/bottom mutual included | **0.106 mH** | **0.273 mH** |
| Conservative, no face-to-face mutual | **0.126 mH** | **0.323 mH** |
| Historical V4 geometry-scaled value | ~0.150 mH | ~~0.385 mH~~ |

Use:
- **0.273 mH/phase** for current engineering terminal-voltage / PF calculations;
- **0.323 mH/phase** as the conservative voltage-design upper screening value.

Method: analytic regularized self terms + 8-point Gauss-Legendre mutual integration, balanced positive-sequence energy extraction, free-space calibration to the historical V4 **0.4461 mH/phase** reference, and the same high-mu image multiplier **1.1465 / 0.4461 = 2.5701**.

This is **ENGINEERING-grade**, not freeze-grade full 3D H(curl) with nonlinear laminated end-region iron.

### Segmentation and per-source maximum-power sizing

Because the 4.5 m secondary moves across 3 m stator segments, normal travel repeatedly includes both two-segment and three-segment energized states. Three-segment full-current operation is therefore a recurring normal state, not only a short handover envelope.

For **per-H-bridge / per-supercapacitor maximum-power sizing**, retain the **two-segment simultaneous-operation case** as the governing condition: the system propulsion demand is concentrated into **24 active H-bridge sources** (2 converter groups x 12 cells) rather than 36. In the recurring three-segment state, all 36 sources may be active, but the same total propulsion demand is distributed across three converter groups, so it does not replace the two-segment case as the maximum per-source power sizing condition.

## 3. 40 m/s operating policy

Direct nonlinear 16 mm 2D moving-conductor FEM gives:

- normal slip band: **3.4-3.8 Hz** — CONDITIONAL;
- preferred sub-band: **3.4-3.6 Hz**;
- fixed-current maximum-thrust/minimum-current reserve: **3.0-3.2 Hz**;
- fitted fixed-current peak: **~3.083 Hz**.

### 443.2 kN nominal system requirement

Across 3.4-3.8 Hz:
- direct 2D current: **2.05-2.13 kA RMS** in the common series path;
- at 3.6 Hz, 1.2 m transverse-edge screening gives about **2.21 kA**.

### 500 kN design capability

Across 3.4-3.8 Hz:
- direct 2D current: **2.18-2.26 kA RMS**;
- at 3.6 Hz, 1.2 m transverse-edge screening gives about **2.35 kA RMS**;
- tooth B95: **~1.61-1.66 T**;
- yoke B95: **~1.69-1.71 T**;
- screening total motor loss: **~2.28-2.48 MW**;
- screening efficiency: **~88.9%-89.8%**.

The operating band remains conditional until a self-consistent finite-width 3D moving-conductor calculation is complete.

## 4. Converter interface

Current converter envelope:
- **4.5 kV class line-line — CONDITIONAL**;
- **3.5 kA RMS pulse/current capability — CONDITIONAL**;
- retain **5 kV insulation/interface margin** until PWM insulation and final physical winding impedance are closed.

The former **4.01-4.15 kV / PF ~0.696-0.700** terminal-voltage screening used the superseded **0.385 mH/phase** V4 geometry-scaled end-leakage value. Recalculate terminal voltage and PF using the current V4.2 leakage values **0.273 mH/phase preferred** and **0.323 mH/phase conservative** before using those old voltage figures for design.

## 5. Transverse edge effect

For an 800 mm primary and 16 mm secondary at 3.6 Hz:
- 0.8 m secondary current-closure factor: ~0.607;
- 1.0 m: ~0.790;
- **1.2 m: ~0.888**;
- 1.25 m: ~0.904.

The selected **1.2 m secondary width** is a design compromise between transverse-current closure and mover mass. The 500 kN 3.6 Hz reference current increases from about 2.21 kA (2D) to about **2.35 kA** in the current local-3D screening.

## 6. Magnetic pressure, eccentricity, and guide design

- Approximately **450 kN per stator face** is used as a preliminary air-gap magnetic-pressure structural screening load.
- This is a stator structural load and is **not** a force acting as attraction on the nonmagnetic aluminium secondary.
- Secondary eccentricity force remains an engineering item requiring direct aluminium-volume JxB integration for final closure.
- Current cross-check estimate for total two-channel electromagnetic restoring stiffness:
  - nominal 443.2 kN: ~19.5 kN/mm;
  - 500 kN design: ~21.9 kN/mm.
- Mechanical guide equivalent translational stiffness target: **300 kN/mm per guide direction — CONDITIONAL**.
- The guide system must not rely on electromagnetic self-restoring behavior as a safety feature.

## 7. Model status

Validated / accepted:
- direct nonlinear 2D moving-conductor calculation with 16 mm secondary;
- longitudinal end effect;
- 25 mm longitudinal mesh convergence on the optimized geometry;
- local transverse-current-closure screening;
- local 3-turn end-leakage screening.

Still open:
1. self-consistent finite-width 3D H(curl) moving-conductor validation;
2. direct 16 mm aluminium JxB eccentricity-force closure;
3. segmented transition transient including the recurring two-segment and three-segment normal operating states, with current sharing and thrust-continuity validation;
4. final rectangular copper conductor dimensions, insulation build, detailed AC resistance/proximity loss and physical phase-impedance closure;
5. mechanical FEA for the 300 kN/mm guide target and 450 kN/face stator pressure load;
6. secondary/support structural validation.

## 8. Superseded V1 reference

The former V1 candidate used 2 m segments, 5.8 m secondary length, 600 mm primary width, 12 mm aluminium, 42 x 60 mm slots, 80 mm yoke and 8 turns. It is retained only for traceability and must not be mixed with V2 operating points.
