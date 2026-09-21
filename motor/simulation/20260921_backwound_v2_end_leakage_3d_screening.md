# V2 back-wound winding end-leakage / end-field 3D screening

Status: **engineering screening; not manufacturing-frozen**

## Method

This study uses the actual V2 winding current paths (rear return, side end turns, same-phase jumpers and six terminal leads) with balanced three-phase phasor current.

Numerical methods:
- 3D softened Biot-Savart field integration;
- QMC magnetic-energy integration of end/back leakage regions;
- a ferromagnetic image-method screening bound following the toroidal-winding DSLIM methodology in Zhang, Zhang & Luo, IET Electric Power Applications 18(10), 1382-1391 (2024), DOI 10.1049/elp2.12486.

This is not a final nonlinear 3D iron-core FEA. Finite 35WW300 permeability, lamination anisotropy, saturation and eddy-current coupling still require Maxwell/COMSOL.

## Leakage inductance

For one 2 m stator-face module:

- complete closed-path free-space external leakage: ~0.110 mH/phase;
- end-region air-core definition: ~0.171 mH/phase;
- ideal high-permeability image-method screening: ~0.464 mH/phase.

For three 2 m modules in series (6 m face), use the current engineering uncertainty band:

```
L_end,6m ~= 0.51 ... 1.39 mH/phase
```

The coil/end geometry contributes about 97% of the free-space leakage. Explicit jumpers and terminal leads contribute only about 2-3%.

The rear-return/back region contributes roughly 69% of the free-space end/back magnetic energy.

## Terminal-voltage implication

Using the current 2D design reference:

- 43 Hz;
- 1430 A RMS;
- 2740 V line-line;
- PF = 0.87.

With ~0.51 mH/phase additional 6 m end leakage:

- corrected VLL ~2.92 kV;
- corrected PF ~0.815.

With the ideal high-mu image screening value ~1.39 mH/phase:

- corrected VLL ~3.29 kV;
- corrected PF ~0.724.

Therefore the preliminary **3.3 kV** CHB envelope does not yet have confirmed voltage margin and must remain CONDITIONAL.

## End/back magnetic field

Complete closed-path free-space model at 1430 A RMS:

- ~60 mT RMS at 40 mm behind yoke back;
- ~43 mT at 90 mm;
- ~30 mT at 140 mm;
- ~15 mT at 240 mm;
- ~7.5 mT at 340 mm;
- below ~1 mT at about 640 mm behind the yoke.

Typical side field away from jumper hot spots:

- ~18-25 mT at ~100 mm outside stator side edge;
- ~7-10 mT at ~200 mm;
- ~3-5 mT at ~300 mm;
- around/below ~1 mT at ~500 mm.

A sampled jumper-lane hot spot near y~500 mm, z~220 mm reaches about 35 mT RMS / 50 mT instantaneous peak.

## Design interpretation

1. End leakage is non-negligible for this 600 mm-wide toroidal/back-wound stator.
2. Rear-return geometry is the dominant optimization target.
3. External phase jumpers are not the dominant inductance source.
4. Gross leakage-field magnitude is much smaller than the main air-gap flux density, but local nonlinear yoke flux and additional iron loss must be checked in the true 3D FEA.
5. Do not freeze the winding or 3.3 kV converter voltage until nonlinear 3D validation closes the leakage-inductance range.

## Required next gate

Build a nonlinear 3D eddy-current model with:
- finite laminated 35WW300 core;
- V2 winding geometry;
- 12 mm aluminium secondary;
- 14 mm single-side gaps;
- ~43 Hz excitation and 40 m/s mover;
- extraction of phase impedance, thrust, local 3D B, and end-region iron loss.
