# Engineering Baseline Governance

## Parameter states

- **FROZEN**: Do not change without an explicit design-change decision.
- **CONDITIONAL**: Preferred value; may move after a targeted validation.
- **OPEN**: Not yet frozen; optimization or architecture selection is still allowed.

## Mandatory workflow

Before any substantive design work:

1. Read `design_baseline.json`.
2. Identify which subsystem and parameter states are affected.
3. Use the baseline as the calculation starting point.
4. Do not import stale values from chat history if they conflict with the repository.
5. For a proposed change, document:
   - old value,
   - proposed value,
   - reason,
   - analysis or simulation evidence,
   - effects on motor, converter, insulation, energy storage, sled/rail, and control.
6. Update the baseline only after the change is accepted.

## Scope rule

The current design authority is **40 m/s**.

A 170 m/s extension study must be stored separately and may identify future changes, but must not modify the 40 m/s baseline by default.

## Simulation integrity

All reported simulation results must identify:

- model version,
- geometry version,
- material assumptions,
- excitation condition,
- mesh / numerical method,
- whether the result is 2D or 3D,
- whether longitudinal end effect and transverse edge effect are represented,
- whether the result is screening-grade or freeze-grade.

## Known model limitations

Current in-house FEM is primarily a 2D longitudinal moving-conductor model. The final baseline still requires:

- local 3D transverse-edge-effect validation,
- segmented handover transient validation,
- final PWM insulation coordination,
- mechanical validation of the 5.8 m secondary support structure.
