# Back-wound end-leakage parameter scan

Status: **engineering screening; main baseline unchanged**

## Scan domain
- rear-return clearance: 6 / 8 / 10 / 12 mm
- side end-turn core clearance: 6 / 8 / 10 mm
- outer bend radius: 26 / 32 / 38 mm
- equivalent coil-pack aspect ratio at constant pack area: 36.6x19.5, 34x21, 29.75x24, 26.44x27, 23.8x30 mm

## V2 reference
- rear return clearance: 12 mm
- side clearance: 8 mm
- outer bend radius: 32 mm
- pack: 34 x 21 mm

High-resolution 6 m face results:
- free-space end leakage: 0.5099 mH/phase
- ideal high-mu image estimate: 1.3755 mH/phase

## Robust local optimum inside the existing back-wound topology

Recommended V3 local candidate:
- rear return clearance: **12 mm**
- side clearance: **6 mm**
- outer bend radius: **38 mm**
- coil pack: **34 x 21 mm**

High-resolution 6 m face:
- free-space end leakage: **0.5031 mH/phase**, -1.35%
- high-mu image estimate: **1.3691 mH/phase**, -0.47%
- equivalent coil copper length: 305.90 -> 302.34 m per 2 m face model, -1.16%
- sampled side-field hot point around 200 mm: 47.90 -> 37.55 mT RMS, -21.6%

At 43 Hz / 1430 A using the current 2D voltage reference:
- free-space corrected VLL: ~2921 V, PF ~0.816
- image-bound corrected VLL: ~3290 V, PF ~0.725

## Findings

1. Reducing rear clearance from 12 mm to 8 or 6 mm is not a robust leakage reduction. The free-space estimate decreases but the high-mu image estimate increases.
2. Changing pack aspect ratio at constant copper-pack area changes leakage only around 1%; no robust gain was found.
3. The V3 local candidate is useful mainly because it lowers side leakage field and copper length without changing the main electromagnetic geometry.
4. Millimetre-level back-wound geometry changes do not solve the end-leakage voltage burden.

## Topology benchmark

A full-pitch distributed-winding reference that preserves the same slot current-sheet pattern was evaluated only as a benchmark:
- free-space 6 m end leakage: ~0.391 mH/phase, about -23% vs V2
- image-model 6 m end leakage: ~0.999 mH/phase, about -27% vs V2
- image-model corrected VLL: ~3.12 kV
- image-model corrected PF: ~0.763

This is not a baseline change. It shows that a >20% reduction probably requires return-path topology change rather than only local back-wound geometry tuning.

## Recommendation

Use V3 as the next back-wound CAD candidate, but keep the winding topology CONDITIONAL. If 3.3 kV voltage margin is mandatory, perform nonlinear 3D FEA comparing V3 back-wound against a topology-level return-path redesign before winding freeze.
