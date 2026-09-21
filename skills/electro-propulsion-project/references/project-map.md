# Project map and handoff rules

## Repository

`qingpishi/electro-propulsion`

## Expected layout

```text
README.md
design_baseline.json
docs/
  system_requirements.md
  design_governance.md
motor/
  baseline/
  simulation/
converter/
energy_storage/
sled/
control/
skills/
```

## Current design authority

The 40 m/s system is the active baseline. High-speed studies up to 170 m/s are extension analyses only and must not silently propagate into the baseline.

## Baseline update order

When a parameter change is accepted:

1. update `design_baseline.json`;
2. update the corresponding subsystem baseline Markdown;
3. update simulation/result notes if evidence changed;
4. note cross-subsystem impacts;
5. preserve previous result files instead of overwriting historical evidence when practical.

## Recommended subsystem boundaries

- `motor/`: electromagnetic geometry, winding, segmentation, FEM, losses, force, normal force, insulation requirements imposed by motor terminals.
- `converter/`: CHB topology, cells, device ratings, switching, segment-selection network, protection, DC interface.
- `energy_storage/`: supercapacitor sizing, voltage window, ESR, pulse power, charge management.
- `sled/`: secondary support, chassis, guidance, wheels, braking mechanics, alignment and air-gap mechanics.
- `control/`: launch state machine, current/thrust control, segment handover, BIT, interlocks, protection.

## Model maturity labels

- `SCREENING`: useful for trends only.
- `ENGINEERING`: converged enough for parameter selection.
- `FREEZE_CANDIDATE`: targeted convergence/validation completed; can support conditional freeze.
- `VALIDATED`: cross-checked with independent FEM/test/source evidence.
