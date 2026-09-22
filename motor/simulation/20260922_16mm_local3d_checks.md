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

## C. Normal-force / eccentricity interpretation correction

**Correction after force-object review:** the previous local screening mixed two different quantities:

1. air-gap Maxwell magnetic pressure acting on / loading the stator faces; and
2. the net electromagnetic force acting on the nonmagnetic aluminium secondary.

Those are not interchangeable.

The 16 mm aluminium secondary has approximately mu_r = 1 and has no ferromagnetic attraction term. Its mechanical normal force must be obtained from the induced-current Lorentz force

```
F_y,Al = integral_VAl < J x B >_y dV
```

or equivalently from a **closed** Maxwell-stress surface enclosing only the aluminium secondary.

The previously quoted ~340-390 kN/face values are therefore retained only as **air-gap magnetic-pressure / stator-face structural screening magnitudes**. They must not be interpreted as attraction acting on the aluminium secondary, and the previous top-minus-bottom pressure difference must not be used to infer the secondary eccentricity-force sign.

For the present aluminium-only double-sided LIM, the expected time-averaged normal action from each stator on the secondary in normal positive-slip motoring is eddy-current repulsion away from that stator. At the centered position, the two opposing repulsive forces cancel by symmetry. If the secondary moves closer to one stator, the closer-side field and induced-current interaction is expected to strengthen, so the first-order physical expectation is a restoring force back toward the center.

This is consistent with the older validated 12 mm model, where direct Lorentz-force integration in the secondary and closed-force cross-check both showed restoring behavior.

**Current 16 mm status:** the magnitude and sign of the eccentricity force are OPEN until the 16 mm optimized geometry is recomputed with direct aluminium-volume JxB integration (or an equivalent closed Maxwell surface). Do not credit electromagnetic restoring behavior as a safety feature before that calculation is complete.

**Structural note:** ~0.4 MN/face remains a useful order-of-magnitude stator air-gap pressure load for support-structure screening, but it is not a mover-side force and its direction/net resultant on the stator assembly still requires a closed-surface force balance.

## Overall
1. Transverse edge effect remains the largest unresolved local-3D correction.
2. 1.2-1.25 m secondary transverse width is the next practical candidate.
3. 3-turn end leakage remains acceptable; 4.5 kV-class conversion remains plausible.
4. Air-gap magnetic pressure on the stator faces remains structurally important; it must not be interpreted as aluminium-secondary attraction.
5. The prior sign-reversal statement is withdrawn. The physical expectation for the aluminium secondary is restoring repulsion, but the 16 mm magnitude/sign remains OPEN pending direct secondary JxB integration; guide/rail design must not rely on it.
6. Freeze-grade closure still requires a self-consistent 3D H(curl) moving-conductor model.
