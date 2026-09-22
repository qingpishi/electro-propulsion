# 16 mm secondary recalibration for the current 3 m / 4.5 m candidate

Status: **engineering screening; 16 mm thickness baseline change accepted, electrical operating point not frozen**

## Baseline decision

The aluminium secondary thickness is now **16 mm FROZEN** for the 40 m/s design authority.
Only thickness is frozen. The previously studied two-piece 2 x 2.9 m / 2-3 mm centre-joint architecture remains analysis-only.

## Candidate geometry used for this recalibration

This study does not promote the following candidate geometry into the main baseline. It uses the latest optimized candidate only to estimate the new 16 mm electrical operating region:
- stator segment: 3.0 m, 6 poles, 36 slots;
- effective secondary length: 4.5 m;
- pole pitch: 500 mm;
- single-side gap: 14 mm;
- stator effective width: 800 mm;
- slot: 32 x 79 mm;
- yoke: 105 mm;
- equivalent turns: 3;
- speed: 40 m/s.

## 2D basis and method

The project already contains a direct nonlinear 2D moving-conductor FEM comparison of 12 mm and 16 mm aluminium on the earlier geometry. That direct study established two robust thickness effects at 40 m/s:
- maximum-thrust slip moves from about 2.44 Hz (12 mm) to about 2.30 Hz (16 mm), i.e. slip scale factor 2.30/2.44 = 0.9426;
- restoring 250 kN/channel at the 16 mm peak requires about 1513 A instead of 1430 A, i.e. current scale factor 1.0580.

The latest optimized 12 mm candidate has already been solved on the converged 25 mm longitudinal mesh. The present study maps those fine-grid response surfaces through the **directly validated 16 mm thickness factors** above. This is therefore a **2D FEM-calibrated screening recalibration**, not a brand-new full remesh/re-solve of the 16 mm optimized geometry.

Longitudinal end-effect trends are inherited from the two source FEM studies. Transverse edge effects remain outside the 2D model.

## Recalibrated operating range

For the 500 kN total design-capability target, the estimated 16 mm current is approximately:
- 3.8 Hz: 2.40 kA;
- 4.0 Hz: 2.42 kA;
- 4.2 Hz: 2.45 kA;
- 4.4 Hz: 2.49 kA;
- 4.6 Hz: 2.55 kA;
- 4.8 Hz: 2.61 kA.

For the 443.2 kN nominal requirement:
- 3.8 Hz: 2.23 kA;
- 4.0 Hz: 2.25 kA;
- 4.2 Hz: 2.28 kA;
- 4.4 Hz: 2.31 kA;
- 4.6 Hz: 2.37 kA;
- 4.8 Hz: 2.43 kA.

The thickness-induced slip shift moves the previous 12 mm practical region of roughly 4.4-4.8 Hz to approximately **4.1-4.5 Hz** for the 16 mm baseline. A reference-center screening value near **4.3 Hz** is appropriate for the next direct solve.

## Voltage and magnetic caution

Voltage and B95 columns in the companion CSV are first-order screening quantities mapped from the converged 12 mm response surface and scaled by the validated 16 mm current ratio. They are intentionally conservative and must not be frozen.

The conservative 500 kN terminal-voltage screening trend is roughly:
- ~4.5 kV near 4.0 Hz;
- ~4.3 kV near 4.2 Hz;
- ~4.2 kV near 4.4 Hz;
- ~4.1 kV near 4.6 Hz.

This continues to support a 4.5 kV-class CHB as the minimum candidate, with 5 kV insulation/interface margin retained until a direct 16 mm optimized-geometry solve and final end-leakage closure are complete.

The mapped B95 values exceed the desired margin at the 500 kN reserve point if simple current scaling is applied. Because a thicker secondary also increases electromagnetic screening, those B95 values are best treated as **upper screening estimates**, not direct FEM predictions.

## Recommendation

1. Keep **16 mm aluminium thickness FROZEN**.
2. Treat the old 12 mm 3.0-4.0 Hz / 3.3-3.7 Hz operating bands as historical only.
3. For the current 3 m / 4.5 m optimized candidate, use **4.1-4.5 Hz** as the next direct 16 mm 2D solve window, centered near **4.3 Hz**.
4. Expect approximately **2.4-2.5 kA** for 500 kN and **2.25-2.35 kA** for 443.2 kN in that window.
5. Do not freeze voltage, PF, loss, or B95 from this recalibration; perform a fresh nonlinear 16 mm solve on the optimized geometry before closing the electrical operating point.
