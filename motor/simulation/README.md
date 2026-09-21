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
