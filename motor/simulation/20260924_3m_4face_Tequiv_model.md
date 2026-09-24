# 3 m four-face-series T-equivalent motor model

Status: **ENGINEERING_BASELINE_CONDITIONAL**

## Scope
One 3 m longitudinal stator segment, with four same-station stator faces connected in series and carrying the same three-phase current.

## Per-phase equivalent circuit
Standard T form:

`R1 + jXsigma1 + [ jXm || (R2'/s + jXsigma2') ]`

Parameters:
- R1,dc @80C = 0.017284 ohm;
- R1,ac engineering = 0.01815 ohm;
- Lsigma1,2D = 0.526 mH;
- Lend,V4.2 preferred = 0.273 mH;
- Lsigma1,total preferred = 0.799 mH;
- Lsigma1,total conservative = 0.849 mH;
- Lm = 7.962 mH;
- R2' = 0.08753 ohm;
- Lsigma2' = 0.7026 mH;
- Rfe = OPEN.

## Extraction
Joint fit of terminal complex impedance and secondary loss over the accepted nonlinear 16 mm 2D moving-conductor FEM:
- thrust levels: 443.2 and 500 kN total;
- slip: 3.4, 3.6 and 3.8 Hz;
- speed: 40 m/s;
- longitudinal end effect represented;
- transverse finite-width effect not represented in the T parameters.

V4.2 CAD-derived R1 and the current 0.273 mH preferred end-leakage value are used.

## Validation
Across six points:
- VLL RMS error ~0.42%;
- PF abs error ~0.003;
- secondary-loss RMS error ~2.21%;
- thrust RMS error ~1.00%;
- maximum thrust error ~1.35%.

At 500 kN / 3.6 Hz:
- I1 = 2210.8 A;
- I2' ~1855 A;
- P2 ~0.904 MW per branch;
- Pag ~10.943 MW per branch;
- Pmech ~10.039 MW per branch;
- F ~250.98 kN per branch;
- two branches -> 501.96 kN versus 500.09 kN FEM.

## Finite-width use rule
For the selected 1.2 m secondary, keep the transverse-edge correction outside the T model until a full 3D complex-impedance extraction exists. At 3.6 Hz, use the current screening relation 2210.8 A -> ~2344.9 A, equivalent to thrust factor ~0.889.
