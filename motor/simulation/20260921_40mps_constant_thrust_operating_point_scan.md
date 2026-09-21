# 40 m/s constant-thrust slip scan

Status: **engineering-grade response-surface scan; proposed operating point, not yet frozen**

## Model basis
- DSLIM-V1 candidate, pole pitch 500 mm, q=2.
- Single-side air gap 14 mm.
- 12 mm continuous aluminium secondary.
- High-resolution nonlinear 2D moving-conductor FEM at 1430 A/face provides the slip-dependent thrust, voltage, PF and loss basis.
- Longitudinal end effect is represented.
- Transverse edge effect is not represented.
- Constant-thrust current interpolation uses F proportional to I^n with n=1.928, calibrated from the actual 3 Hz FEM points at 1365 A and 1430 A.
- Voltage scales approximately linearly with current; P2/Pcu/Pfe use I^2 scaling. At 3 Hz this reproduces the direct 1365 A nominal FEM point closely.
- V4 winding terminal correction uses 0.4461 mH/phase free-space end leakage and 1.1465 mH/phase high-mu screening bound.
- Copper loss uses the existing 2D baseline resistance and does **not** credit the still-unvalidated V4 copper-length reduction.

## Slip selection criterion
Use the V4 high-mu end-leakage estimate as the conservative boundary and require, at the 500 kN design capability:
- VLL < 3.3 kV per stator face;
- corrected PF >= 0.75;
- current < 1.8 kA per stator face;
while minimizing loss/current.

The first practical region satisfying this is about 3.35 Hz. A **3.4 Hz** normal slip target is recommended to provide control/model margin.

At 40 m/s and tau=0.5 m:
- slip target: **3.4 Hz**
- supply frequency: **43.4 Hz**
- slip ratio: **7.83%**

## Nominal 443.2 kN total operating point
Target: 221.6 kN/channel.

- Current: **1.406 kA RMS/face**
- 2D line-line voltage before end correction: ~2.443 kV/face
- V4-corrected line-line voltage: **2.59 kV free estimate / 2.88 kV high-mu bound**
- 2D PF before end correction: ~0.887
- V4-corrected PF: **0.835 free / 0.753 high-mu**
- Channel efficiency: **84.61%**
- Secondary loss: **1.134 MW/channel**
- Primary copper loss: **0.474 MW/channel**
- Iron loss: **~4.1 kW/channel**
- Total motor loss: **1.613 MW/channel**
- Two-channel total motor loss: **3.225 MW**
- Mechanical output: 8.864 MW/channel
- Motor input: **10.477 MW/channel / 20.953 MW total**

## 500 kN design-capability operating point
Target: 250 kN/channel.

- Current: **1.497 kA RMS/face**
- 2D line-line voltage before end correction: ~2.600 kV/face
- V4-corrected line-line voltage: **2.76 kV free estimate / 3.06 kV high-mu bound**
- 2D PF before end correction: ~0.887
- V4-corrected PF: **0.835 free / 0.753 high-mu**
- Channel efficiency: **84.55%**
- Secondary loss: **1.285 MW/channel**
- Primary copper loss: **0.537 MW/channel**
- Iron loss: **~4.7 kW/channel**
- Total motor loss: **1.827 MW/channel**
- Two-channel total motor loss: **3.655 MW**
- Mechanical output: 10.000 MW/channel
- Motor input: **11.827 MW/channel / 23.655 MW total**
- Conservative 3.3 kV voltage margin: **~239 V/face**
- 1.8 kA current margin: **~303 A/face**

## Comparison
- 2.4-2.5 Hz gives minimum current and best efficiency, but poor PF and insufficient/very small conservative voltage margin after V4 end-leakage correction.
- Around 3.0 Hz efficiency remains high, but conservative PF is only about 0.73.
- 3.3-3.5 Hz provides the best practical compromise.
- Beyond about 3.5 Hz, PF improves slowly but current, secondary loss and copper loss rise increasingly quickly.

## Proposed control policy
- Use **~3.4 Hz** as the normal 40 m/s slip target.
- Command current from thrust demand:
  - ~1.41 kA/face for 443.2 kN total;
  - ~1.50 kA/face for 500 kN total.
- Retain 2.3-2.6 Hz as a maximum-force/minimum-current reserve region when terminal-voltage margin allows.
- Do not freeze this operating point into main until a direct current-adjusted FEM check at 3.4 Hz and final nonlinear 3D winding impedance validation close the remaining uncertainty.
