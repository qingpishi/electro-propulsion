# 16 mm optimized LIM — local 3D screening update

Status: **engineering screening; not freeze-grade whole-machine 3D H(curl) FEA**

## Basis
- stator module: 3.0 m, 6 poles / 36 slots;
- stator active width: 800 mm;
- slot: 32 x 79 mm;
- yoke: 105 mm;
- equivalent turns: 3;
- secondary: 4.5 m effective length, **16 mm aluminium baseline**;
- single-side air gap: 14 mm;
- speed: 40 m/s;
- direct 16 mm 2D normal band: 3.4-3.8 Hz, preferred 3.4-3.6 Hz.

## A. Transverse finite-width screening

At 3.6 Hz slip, aluminium skin depth is about **44.8 mm**. The 16 mm plate has t/delta about **0.357**, so the thickness-integrated conducting-sheet approximation remains suitable for screening.

For an 800 mm primary, the transverse current-closure factor depends mainly on pole pitch and secondary transverse width:
- 0.8 m secondary: kc = 0.607;
- 1.0 m: kc = 0.790;
- 1.2 m: kc = 0.888;
- 1.25 m: kc = 0.904;
- 1.4 m: kc = 0.940.

The direct 16 mm FEM gives a local thrust-current exponent near **n = 2.03** at 3.6 Hz.

For the 500 kN 2D point (2211 A):
- 0.8 m secondary -> closure-corrected current ~2.83 kA;
- 1.0 m -> ~2.48 kA;
- 1.2 m -> ~2.34 kA;
- 1.25 m -> ~2.32 kA;
- 1.4 m -> ~2.28 kA.

A separate finite-primary magnetic-pressure sensitivity factor is about **0.870** for the 16 mm geometry. This is deliberately kept separate from the current-closure correction and should not be multiplied into the baseline thrust before a self-consistent 3D iron/eddy-current solve.

Two-channel active aluminium mass for two 4.5 m plates is approximately:
- 0.8 m width: 311 kg;
- 1.2 m width: 467 kg;
- 1.25 m width: 486 kg.

**Disposition:** a 1.2-1.25 m secondary width remains a practical next candidate if the target is to keep the transverse current-closure penalty near or below 10%.

## B. V4-style end-winding leakage

The 3-turn V4 loop geometry is not changed by the 12 -> 16 mm secondary-thickness decision. Local 3D geometry scaling remains:
- free-space end leakage: ~0.15 mH/phase per converter;
- high-mu screening bound: ~0.385 mH/phase per converter.

For 500 kN direct 16 mm operating points using the high-mu bound:
- 3.4 Hz / 2179 A: terminal VLL ~4.15 kV, PF ~0.696;
- 3.6 Hz / 2211 A: terminal VLL ~4.07 kV, PF ~0.702;
- 3.8 Hz / 2259 A: terminal VLL ~4.01 kV, PF ~0.700.

**Disposition:** local end leakage does not invalidate a 4.5 kV-class CHB. Retain 5 kV insulation/interface margin until the physical winding and iron are closed in full 3D.

## C. Normal-force / eccentricity screening

The Maxwell-stress model was re-run with the explicit 16 mm secondary and the new direct 16 mm operating currents. Absolute-force postprocessing is cross-calibrated to the prior optimized-geometry 12 mm reference, and the finite-width magnetic-pressure sensitivity factor (~0.870) is then applied as a local 3D screening correction.

Results:
- nominal 443.2 kN @ 3.1 Hz / 2036 A: ~340 kN/face finite-width screened attraction;
- design 500 kN @ 3.1 Hz / 2160 A: ~382 kN/face;
- nominal 443.2 kN @ 3.6 Hz / 2083 A: ~345 kN/face;
- design 500 kN @ 3.6 Hz / 2211 A: ~388 kN/face.

At 1 mm eccentricity the residual top-minus-bottom force is only about:
- ~0.21 kN/channel nominal @ 3.1 Hz;
- ~0.23 kN/channel design @ 3.1 Hz;
- ~0.40 kN/channel nominal @ 3.6 Hz;
- ~0.44 kN/channel design @ 3.6 Hz.

The reduced model shows the closer-gap face becoming slightly stronger, i.e. a sign reversal relative to the older 12 mm baseline restoring tendency. However this differential is only about 0.1% of the absolute face attraction, so the sign is **not robust enough to freeze** and must not be credited as a safety/restoring feature.

**Disposition:** use about **0.45 MN/face as a preliminary electromagnetic structural screening load** for the present 16 mm candidate before dynamic/safety factors. This replaces the earlier ~0.55 MN/face local-screen value from the 12 mm optimized candidate.

## Overall
1. Transverse edge effect remains the largest unresolved local-3D correction.
2. 1.2-1.25 m secondary transverse width is the next practical candidate.
3. 3-turn end leakage remains acceptable; 4.5 kV-class conversion remains plausible.
4. Absolute normal attraction is lower than in the 12 mm optimized candidate but is still structurally important.
5. Eccentricity-force sign remains unresolved; guide/rail design must not rely on electromagnetic restoring behavior.
6. Freeze-grade closure still requires a self-consistent 3D H(curl) moving-conductor model.
