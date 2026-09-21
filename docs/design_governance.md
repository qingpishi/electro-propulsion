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


## Operating-point naming rule

Do not mix values from different 40 m/s studies into one motor design point.

Use the following terms consistently:
- **NOMINAL_REQUIREMENT**: system thrust requirement, currently 443.2 kN total at 40 m/s for the 12 t / 50 deg / 3g case. It does not by itself define motor current, slip, voltage or PF.
- **DESIGN_CAPABILITY**: verified motor capability target, currently 500 kN total. The present self-consistent fixed-current evidence is 1430 A/face, 2.44 Hz slip and about 250.07 kN/channel in the high-resolution 2D scan.
- **OPERATING_POINT**: a self-consistent set of thrust, current, slip, voltage, PF, efficiency and loss. This is still OPEN at 40 m/s and must be closed by constant-thrust optimization.
- **LEGACY_REFERENCE**: older engineering values retained for traceability only. In particular, the 3 Hz / 2.74 kV / PF 0.87 reference must not be combined with the 2.44 Hz maximum-thrust point.

When a quantity is not available from the same validated model/run as the rest of an operating point, mark it OPEN instead of borrowing it from another study.
