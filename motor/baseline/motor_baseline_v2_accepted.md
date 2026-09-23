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
- Normal propulsion uses two adjacent main segments, providing a **6.0 m** energized longitudinal window.
- During handover, **up to three adjacent 3.0 m longitudinal segments may be energized simultaneously**. These longitudinal segments are supplied by independent A/B/C converter branches; they are not electrically series-connected to one another.
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
| Normal main energized segments | 2 | FROZEN principle |
| Maximum simultaneous energized segments during handover | 3 | FROZEN operational requirement |
| Main energized length | 6.0 m | DERIVED |
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

For loss accounting only:
- two simultaneously full-current longitudinal segments: **103.705 mOhm** equivalent;
- three simultaneously full-current longitudinal segments: **155.557 mOhm** equivalent.

These latter values are **loss-equivalent sums across independent converter branches, not series terminal resistances**.

At 3.6 Hz using a 1.05 AC-resistance screening multiplier:
- 443.2 kN / 2.210 kA: **0.532 MW** for two full-current segments, **0.798 MW** for three;
- 500 kN / 2.345 kA: **0.599 MW** for two full-current segments, **0.898 MW** for three;
- 3.5 kA design envelope: **1.334 MW** for two full-current segments, **2.001 MW** for three (short-pulse screening only).

For handover with unequal segment currents, use:

`Pcu = 1.05 * Rsum,1seg * (I1^2 + I2^2 + I3^2)`

with currents in A and `Rsum,1seg = 0.051852 Ohm`.

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

For the 500 kN 3.4-3.8 Hz band, the 3-turn V4-style high-mu end-leakage screening gives approximately:
- terminal VLL: **4.01-4.15 kV**;
- power factor: **~0.696-0.700**.

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
3. three-group segmented handover transient, including the normal two-segment state and maximum three-segment simultaneous energization;
4. final rectangular copper conductor dimensions, insulation build, detailed AC resistance/proximity loss and physical phase-impedance closure;
5. mechanical FEA for the 300 kN/mm guide target and 450 kN/face stator pressure load;
6. secondary/support structural validation.

## 8. Superseded V1 reference

The former V1 candidate used 2 m segments, 5.8 m secondary length, 600 mm primary width, 12 mm aluminium, 42 x 60 mm slots, 80 mm yoke and 8 turns. It is retained only for traceability and must not be mixed with V2 operating points.
