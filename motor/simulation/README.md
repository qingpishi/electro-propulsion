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
