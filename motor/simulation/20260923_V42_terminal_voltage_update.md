# DSLIM V2 + V4.2 terminal-voltage update

Status: **ENGINEERING screening; baseline not changed by this study**

## Geometry / model authority
- baseline: DSLIM-V2-accepted-40mps-tau500-16mm;
- stator segment: 3.0 m, 36 slots, 800 mm active width;
- secondary: 4.5 m x 1.2 m x 16 mm aluminium;
- single-side gap: 14 mm;
- winding: V4.2 adapted low-loop-area paired-slot back-connected, 3 turns;
- winding resistance: current CAD-derived V4.2 values at 80 C, 300 mm2/turn;
- speed: 40 m/s; slip points: 3.4 / 3.6 / 3.8 Hz.

## 1. V4.2 end-leakage extraction

The old terminal-voltage baseline used a geometry-scaled V4 high-mu end-leakage value of 0.385 mH/phase. The current V4.2 extraction uses the actual end-path topology:
- paired-slot 500 mm loops;
- six end-turn layers;
- phase-separated A/C/B corridors;
- explicit series links and terminal leads;
- active slot conductors excluded from the end-leakage integral so the 2D main-field inductance is not double-counted.

Numerical method:
- analytic regularized self integral for every finite straight conductor section;
- 8-point Gauss-Legendre double integration for mutual terms;
- balanced three-phase positive-sequence energy extraction;
- free-space result calibrated against the repository V4 reference 0.4461 mH/phase;
- ideal high-mu image ratio retained from the old validated V4 screening: 1.1465 / 0.4461 = 2.5701.

Results per 3 m longitudinal converter segment (four stator faces in series):

| treatment | free-space Lpos | high-mu screening Lpos |
|---|---:|---:|
| double-sided top/bottom mutual included; two physical channels assumed mutually remote | 0.106 mH | **0.273 mH** |
| conservative: no mutual between the four faces | 0.126 mH | **0.323 mH** |
| old V4 geometry-scaled screening | ~0.150 mH | **0.385 mH** |

The V4.2 geometry therefore reduces the positive-sequence end-leakage screening value relative to the old 0.385 mH estimate. The 0.273 mH result is the preferred engineering value; 0.323 mH is retained as the conservative no-face-mutual upper screening value.

Because the V4.2 layer/corridor geometry is not perfectly phase-symmetric, the leakage is represented as a 3x3 phase-inductance matrix rather than three independent identical scalar inductors. This produces a modest line-voltage spread that must be retained in converter-margin checks.

## 2. Finite-width current correction and field impedance

For the selected 1.2 m secondary, transverse current-closure screening uses kc = 0.88756. The local force-current exponent around the 443/500 kN points is about n = 2.0, giving current correction factors around 1.06.

The terminal-voltage update does NOT scale the complete 2D impedance by this factor. Instead:
1. target mechanical power is held fixed (500 kN -> 20 MW total; 443.2 kN -> 17.728 MW total);
2. secondary aluminium loss is scaled by the corrected-current squared ratio;
3. the real field resistance is recalculated from mechanical power + corrected secondary loss;
4. the 2D field reactive impedance is retained as first-order screening;
5. current V4.2 AC copper resistance (1.05 x the 80 C CAD-derived resistance) and the new 3D end-leakage matrix are added in series.

This makes terminal voltage and the current motor-loss accounting mutually consistent.

## 3. Updated 500 kN terminal voltage

| slip | corrected current | preferred mutual-included max VLL | conservative no-face-mutual max VLL | terminal PF range |
|---:|---:|---:|---:|---:|
| 3.4 Hz | 2.311 kA | **4.205 kV** | **4.269 kV** | 0.674-0.681 |
| 3.6 Hz | 2.345 kA | **4.122 kV** | **4.185 kV** | 0.681-0.688 |
| 3.8 Hz | 2.396 kA | **4.065 kV** | **4.131 kV** | 0.680-0.687 |

At the preferred 3.6 Hz reference, the mutual-included line voltages are approximately:
- Vab = 4.092 kV;
- Vbc = 4.122 kV;
- Vca = 3.966 kV.

The conservative no-face-mutual values are about:
- Vab = 4.185 kV;
- Vbc = 4.155 kV;
- Vca = 3.964 kV.

## 4. Updated 443.2 kN terminal voltage

| slip | corrected current | preferred mutual-included max VLL | conservative no-face-mutual max VLL |
|---:|---:|---:|---:|
| 3.4 Hz | 2.178 kA | 3.970 kV | 4.031 kV |
| 3.6 Hz | 2.209 kA | 3.893 kV | 3.954 kV |
| 3.8 Hz | 2.257 kA | 3.839 kV | 3.901 kV |

## 5. CHB voltage margin

For the 500 kN worst normal-band point (3.4 Hz):
- preferred V4.2 mutual-included maximum VLL = 4.205 kV -> about 6.6% below 4.5 kV;
- conservative no-face-mutual maximum VLL = 4.269 kV -> about 5.1% below 4.5 kV.

At 1.0 kV/cell, the corresponding modulation indices are about 0.858 and 0.871.
At 1.1 kV/cell they are about 0.780 and 0.792.

Therefore the accepted 4-cell/phase, 1.0-1.1 kV/cell CHB remains voltage-feasible in this updated V4.2 screening. The previous 4.01-4.15 kV terminal-voltage range should be replaced after review; it belongs to the old V4 end-leakage estimate and uncorrected 2D current.

## 6. Model maturity / remaining closure

This is an ENGINEERING terminal-voltage update, not freeze-grade 3D H(curl) FEA. Remaining closure items:
- self-consistent finite-width 3D moving-conductor field solution;
- nonlinear laminated-core end-region permeability/saturation rather than calibrated image-bound high-mu treatment;
- final rectangular-conductor AC/proximity resistance;
- explicit segment-position-dependent impedance during recurring two-/three-segment overlap;
- final routing/phase-permutation check to minimize V4.2 phase leakage asymmetry.

Recommended current voltage design value for converter screening:
- preferred normal 3.6 Hz / 500 kN: use **4.12 kV max line-line**;
- normal-band worst-case conservative screening: use **4.27 kV max line-line**;
- retain **4.5 kV converter output class** and **5 kV insulation/interface margin**.
