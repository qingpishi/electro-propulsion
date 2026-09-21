---
name: electro-propulsion-project
description: Repository-aware engineering workflow for the ZQJS heavy-load electromagnetic propulsion project stored in the GitHub repository qingpishi/electro-propulsion. Use when working on the project's DSLIM motor, segmented stator control, CHB converter, supercapacitor storage, sled/rail mechanics, braking, insulation, control, simulation, validation, or design-baseline updates. Always restore the repository baseline before calculations, preserve frozen parameters unless an explicit design change is requested, separate 40 m/s baseline work from 170 m/s extension analysis, and record cross-subsystem impacts when proposing changes.
---

# Electro Propulsion Project

## Core workflow

1. Treat `qingpishi/electro-propulsion` as the source of truth.
2. Before substantive work, read `design_baseline.json` and the relevant subsystem baseline document.
3. Identify every affected parameter state: `FROZEN`, `CONDITIONAL`, `OPEN`, `REFERENCE`, or derived.
4. Use repository values instead of stale conversation values when they conflict.
5. Do not silently change a `FROZEN` parameter. If a change is necessary, present it as a design delta and wait for explicit acceptance before updating the baseline.
6. Keep the current design authority at 40 m/s. Treat 170 m/s work as extension analysis only unless the user explicitly promotes it into the baseline.
7. When calculations or simulations modify a `CONDITIONAL` or `OPEN` parameter, document the old value, new value, reason, evidence, and downstream effects.
8. After an accepted baseline change, update both the machine-readable baseline and the relevant human-readable subsystem document.

## Repository files to read first

Always read:
- `design_baseline.json`
- `docs/design_governance.md`

Then read as needed:
- system requirements: `docs/system_requirements.md`
- motor: `motor/baseline/motor_baseline_v1_candidate.md`
- motor simulation notes: `motor/simulation/README.md`

Use `references/project-map.md` for the expected repository layout and handoff rules.

## Engineering rules

### Motor

Preserve the topology unless an explicit redesign is requested:
- dual-channel, double-sided long-primary LIM;
- four independently controlled stator faces;
- three phases per stator face;
- main simultaneously active longitudinal segments use equal current;
- energized stator length must remain greater than the effective secondary length;
- preserve magnetic-field continuity during segment handover.

Do not call 3 Hz the maximum-thrust slip frequency. The current fixed-current 40 m/s scan has a peak near 2.44 Hz. The normal operating slip schedule remains open until constant-thrust loss/PF optimization is completed.

### Simulation integrity

For every simulation result, state:
- geometry/baseline version;
- 2D or 3D;
- material model;
- excitation/current/voltage condition;
- mesh or numerical method;
- whether longitudinal end effect is included;
- whether transverse edge effect is included;
- whether the result is screening-grade or freeze-grade.

Never use a coarse screening result as a frozen design result without a targeted convergence or cross-validation step.

### Cross-subsystem impact check

When changing motor geometry, current, voltage, segmentation, or slip, check effects on:
- CHB voltage/current/MVA and switching strategy;
- insulation and PWM stress;
- supercapacitor usable energy and peak power;
- sled mass, secondary support, air-gap tolerance, and braking;
- control states, segment handover, and protection.

When changing sled mass or launch requirements, recalculate propulsion force and braking force before updating motor or energy-storage sizing.

## Design delta format

For any proposed baseline change, use this compact structure:

- Parameter
- Current value/state
- Proposed value/state
- Reason
- Evidence
- Downstream impact
- Recommendation: keep / conditionally accept / freeze

Do not update the repository baseline until the user accepts the design change unless the user explicitly asked for the update itself.

## GitHub editing behavior

Prefer safe working branches for nontrivial changes. For simple project bootstrap files or user-requested baseline initialization, direct commits are acceptable if the repository is empty and the user explicitly asked to establish the project.

For later substantive engineering updates:
1. create a branch;
2. edit the baseline and supporting analysis notes;
3. summarize the delta;
4. open a PR when useful for review.

Never merge a PR or overwrite a frozen baseline decision without explicit user approval.
