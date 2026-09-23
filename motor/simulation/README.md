# Motor Simulation Index

## Current authoritative studies

### 40 m/s / 500 mm pole-pitch V1 candidate

Key outputs:
- nonlinear 2D moving-conductor FEM
- final geometry convergence
- nominal 0–40 m/s schedule
- 40 m/s slip-frequency sweep
- maximum-thrust slip point near 2.44 Hz

### Validation state

Validated numerically:
- manufactured-solution convergence of the custom P1 FEM
- mesh convergence at representative operating points
- nonlinear 35WW300 engineering B-H model

Still required:
- 3D transverse edge effects
- segmented transient commutation
- final insulation / PWM stress
- structural verification of secondary support

## Result naming convention

Use:

```
YYYYMMDD_<model-version>_<geometry-version>_<study>.csv
YYYYMMDD_<model-version>_<geometry-version>_<study>.png
```

Every study should include a short Markdown note describing:
- inputs,
- solver assumptions,
- result summary,
- limitations,
- whether the result changes the baseline.


## Consolidated validation evidence (2026-09-21)

- 14 mm nominal-gap normal-force/eccentricity validation: ENGINEERING-grade 2D result.
- 16 mm two-piece secondary: analysis-only candidate; 2D joint screening passed, not part of the baseline.


## Baseline cleanup — 2026-09-21

The 40 m/s operating data is now separated into four categories:

1. **Nominal system requirement**: 443.2 kN total / 221.6 kN per channel.
2. **Verified 500 kN fixed-current capability**: 1430 A/face, 2.44 Hz slip, 250.068 kN/channel, 500.136 kN total.
3. **Historical 3 Hz reference**: 1430 A/face, 242.361 kN/channel. The older 2.74 kV / PF 0.87 / efficiency / B values are traceability-only.
4. **Final normal operating point**: OPEN pending constant-thrust voltage/PF/loss optimization including selected winding end leakage.

Do not use the legacy 2.74 kV / PF 0.87 values as if they were validated at the 2.44 Hz maximum-thrust point.


## 40 m/s operating-band policy — 2026-09-21

The normal operating baseline is now a **slip-frequency band**, not a single point:

- normal operating band: **3.0-4.0 Hz**;
- preferred sub-band: **3.3-3.7 Hz**;
- 3.4 Hz is a reference center only;
- 2.3-2.6 Hz remains a maximum-thrust/minimum-current reserve region.

This range definition is based on the constant-thrust engineering scan with the V4 high-mu end-leakage bound. It is CONDITIONAL pending direct validation.


## 16 mm secondary baseline update — 2026-09-22

- Aluminium secondary thickness is now **16 mm FROZEN** for the 40 m/s design authority.
- The former 12 mm electrical operating bands are historical pending direct 16 mm recalculation.
- A FEM-calibrated screening recalibration for the current 3 m / 4.5 m optimized candidate indicates a next direct-solve window of about **4.1-4.5 Hz**, centered near **4.3 Hz**.
- Expected screening currents are about **2.25-2.35 kA** for 443.2 kN and **2.4-2.5 kA** for 500 kN.
- The two-piece 2 x 2.9 m / 2-3 mm joint architecture remains analysis-only; only thickness was promoted to baseline.


## Direct 16 mm optimized-geometry FEM — 2026-09-22

The earlier 4.1-4.5 Hz thickness-scaling estimate is superseded for operating-band selection by a direct 16 mm moving-conductor solve on the current optimized geometry (3 m segment / 4.5 m secondary / 800 mm width / 32 x 79 mm slot / 105 mm yoke / 3 turns / 14 mm gap).

Direct result:
- fixed-current peak near **3.08 Hz**;
- maximum-force/minimum-current plateau: **3.0-3.2 Hz**;
- practical normal operating range: **3.4-3.8 Hz**;
- preferred sub-band: **3.4-3.6 Hz**, pending transverse-edge correction;
- 500 kN current is about **2.16-2.26 kA** over 3.0-3.8 Hz;
- 443.2 kN current is about **2.04-2.13 kA** over the same range.

Do not freeze the operating band until the finite-width transverse-edge correction and final winding impedance are closed.


## Motor V2 accepted baseline — 2026-09-22

The current 40 m/s motor baseline is `motor/baseline/motor_baseline_v2_accepted.md`.

Accepted geometry:
- 3.0 m segment / 6 poles / 36 slots;
- 4.5 m secondary;
- 800 mm primary width / 1.2 m secondary width;
- 16 mm aluminium;
- 14 mm single-side gap;
- 32 x 79 mm slot / 105 mm yoke;
- 3 turns.

Current operating policy:
- normal 3.4-3.8 Hz;
- preferred 3.4-3.6 Hz;
- maximum-force/minimum-current reserve 3.0-3.2 Hz.

V1 values are superseded and traceability-only.


## V4.2 winding resistance and handover-loss update — 2026-09-23

The current winding baseline is `motor/winding/winding_baseline_v42.md` and the canonical current CAD source is under `motor/model/DSLIM_V2_V4p2/`.

Key resistance values at 80 degC and 300 mm2 copper per turn:
- one 3 m stator face: A/B/C = **4.094 / 4.399 / 4.471 mOhm**;
- one 3 m longitudinal segment after four same-station faces are series-connected: A/B/C = **16.374 / 17.596 / 17.882 mOhm**;
- three-phase loss-equivalent sum per energized 3 m segment: **51.852 mOhm**.

Operating-state definition:
- normal main state: **2 energized segments**;
- handover maximum: **3 simultaneously energized segments**.

At 500 kN / 3.6 Hz / 2.345 kA using the initial 1.05 AC multiplier:
- two full-current segments: **~0.599 MW copper loss**;
- three full-current segments: **~0.898 MW copper loss**.

For transient handover, do not assume all three segments carry equal current; integrate the actual `I1(t)^2 + I2(t)^2 + I3(t)^2` trajectory.


## V4.2 end-leakage recalculation — 2026-09-23

The current V4.2 3D winding geometry supersedes the old 0.385 mH/phase high-mu geometry-scaled V4 estimate.

Per phase / per one 3 m longitudinal segment:
- preferred free-space: **0.106 mH**;
- conservative free-space: **0.126 mH**;
- preferred high-mu screening: **0.273 mH**;
- conservative high-mu screening: **0.323 mH**.

Use 0.273 mH/phase for current engineering terminal-voltage/PF calculations and 0.323 mH/phase as the conservative voltage-design screening upper bound.

The former terminal-voltage range 4.01-4.15 kV is tied to the superseded 0.385 mH value and must not be treated as current V4.2 voltage evidence.
