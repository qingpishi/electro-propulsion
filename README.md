# Electro Propulsion

Repository for the ZQJS heavy-load electromagnetic launch / propulsion project.

## Current design authority

The **current project baseline is the 40 m/s system**.  
A 170 m/s extension may be studied for scalability, but it must **not** modify the 40 m/s baseline unless an explicit design-change decision is made.

## Current baseline status

- System: inclined heavy-load electromagnetic launch system
- Payload: 10 t
- Launch angle: 50 deg
- Exit speed: 40 m/s
- Net launch acceleration: 3 g
- Motor: dual-channel, double-sided long-primary linear induction motor (DSLIM)
- Design thrust: 500 kN total
- Pole pitch: 500 mm
- Electrical segmentation: 2.0 m basic stator segment
- Secondary effective length: 5.8 m
- Main energized window: three adjacent segments, 6.0 m total
- Main propulsion segments: equal-current series operation
- Fourth segment: pre-excitation / handover path
- Motor baseline maturity: **V1.0 candidate / conditionally frozen**

See:
- [System requirements](docs/system_requirements.md)
- [Motor baseline](motor/baseline/motor_baseline_v1_candidate.md)
- [Machine-readable baseline](design_baseline.json)
- [Simulation index](motor/simulation/README.md)
- [Engineering change rules](docs/design_governance.md)

## Repository layout

```
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
design_baseline.json
```

## Baseline rule

Before performing any new design calculation, simulation, optimization, or interface update:

1. Read `design_baseline.json`.
2. Check the parameter status: `FROZEN`, `CONDITIONAL`, or `OPEN`.
3. Do not silently replace a frozen parameter.
4. Record any proposed change as a design delta with reason, evidence, and downstream impact.
5. Treat 170 m/s studies as extension analysis only unless the baseline authority explicitly changes.
