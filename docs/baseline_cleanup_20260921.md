# 40 m/s baseline cleanup — 2026-09-21

## Purpose
Remove mixed operating-point values from the V1 candidate baseline.

## What changed
- Separated the 443.2 kN system nominal requirement from the 500 kN motor design capability.
- Made the 1430 A / 2.44 Hz / 250.068 kN-per-channel fixed-current scan the authoritative **thrust capability evidence**.
- Reclassified the 3 Hz / 2.74 kV / PF 0.87 data as **LEGACY REFERENCE**.
- Marked voltage, PF, efficiency and loss at the final 40 m/s operating point as OPEN.
- Kept the normal slip schedule OPEN.
- Kept the preliminary 3.3 kV / 1.8 kA CHB envelope CONDITIONAL.
- No frozen geometry or system requirement was changed.

## Why
The previous baseline placed 250 kN/channel together with 2.74 kV, PF 0.87 and 85.6% efficiency even though the latest high-resolution scan shows that 1430 A at 3 Hz produces only 242.361 kN/channel, while the 250 kN/channel fixed-current peak occurs near 2.44 Hz.

The cleanup prevents values from different runs/model stages from being treated as one self-consistent operating point.

## Next closure
Run a constant-thrust 40 m/s optimization that solves current and slip for 443.2 kN nominal and 500 kN design-capability cases, including selected-winding end leakage, then freeze terminal voltage, PF, efficiency and loss.
