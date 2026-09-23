# DSLIM V2 + V4.2 current 3D model

Model ID: **DSLIM_V2_V4p2_3D_20260923**

This directory contains the canonical parametric source and validation metadata for the current motor CAD.

## Current geometry
- 3.0 m stator segment;
- 36 slots / 6 poles per segment;
- 800 mm stator active width;
- 32 x 79 mm slots;
- 105 mm yoke;
- 14 mm single-side air gap;
- 4.5 m x 1.2 m x 16 mm aluminium secondary;
- V4.2 adapted 3-turn low-loop-area paired-slot back-connected winding.

## Operating configurations
- **Normal:** two adjacent longitudinal segments energized; 6 m main field window.
- **Handover maximum:** up to three adjacent longitudinal segments may be energized simultaneously.

The longitudinal segments are supplied by independent converter branches and are **not series-connected**. The 3-segment model is used for handover geometry, thermal/loss and control validation.

## Winding collision policy
The V4.2 routing uses:
- six end-turn layers;
- rounded transitions;
- separate A/C/B phase corridors;
- opposite +/-Y routing for top/bottom stators;
- separate internal links and external leads.

The validated representative CAD has zero Boolean intersection volume for:
- A vs B, A vs C, B vs C;
- winding vs core;
- winding vs 16 mm secondary.

## Rebuild
Install CadQuery, then run:

```bash
DSLIM_MODEL_SEGMENTS=2 python build_DSLIM_V2_V4p2_parametric.py
DSLIM_MODEL_SEGMENTS=3 python build_DSLIM_V2_V4p2_parametric.py
```

Use `DSLIM_MODEL_OUT=<directory>` to select the output folder.

## Generated binary CAD
STEP/GLB outputs are generated artifacts. `model_manifest.json` records SHA-256 hashes for the validated 2-segment files from the current model build.
