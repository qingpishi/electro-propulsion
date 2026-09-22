# Direct 2D FEM recalculation — 16 mm secondary on current optimized geometry

Status: **engineering-grade direct 2D moving-conductor FEM; operating band proposed, not frozen**

## Geometry / excitation
- speed: 40 m/s;
- stator module: 3.0 m, 6 poles, 36 slots;
- model energized longitudinal window: 6.0 m;
- effective secondary length: 4.5 m;
- aluminium thickness: **16 mm (FROZEN thickness baseline)**;
- pole pitch: 500 mm;
- stator effective width: 800 mm;
- slot: 32 x 79 mm;
- yoke: 105 mm;
- single-side air gap: 14 mm;
- equivalent turns per slot side: 3;
- nonlinear 35WW300-like engineering B-H law;
- moving-conductor harmonic formulation with SUPG stabilization;
- longitudinal end effect represented;
- transverse edge effect not represented in this 2D solve.

The custom solver is locally calibrated to the converged 12 mm optimized-geometry 4.5 Hz point so that systematic source/voltage/post-processing bias is removed before comparing the direct 16 mm solution. The 16 mm thickness itself is solved explicitly in the conductor domain; it is not represented by a current/slip scaling factor.

## Mesh / numerical check
- longitudinal maximum mesh size: 25 mm;
- aluminium thickness mesh: about 2 mm;
- air-gap mesh: about 2.5 mm;
- about 30.6k nodes / 60.5k triangles for the 16 mm geometry;
- nonlinear Picard iteration with relaxed engineering B-H update.

## Fixed-current result
At 2300 A RMS, the direct slip scan gives 559.7 / 567.3 / 568.0 / 566.6 / 558.0 / 541.8 / 518.6 kN total at 2.8 / 3.0 / 3.1 / 3.2 / 3.4 / 3.6 / 3.8 Hz. A quadratic fit around 3.0-3.2 Hz gives the fixed-current peak near **3.083 Hz**.

## Constant-thrust result
For 443.2 kN total, direct FEM requires approximately:
- 2.037 / 2.036 / 2.038 / 2.053 / 2.083 / 2.129 kA at 3.0 / 3.1 / 3.2 / 3.4 / 3.6 / 3.8 Hz.

For 500 kN total:
- 2.161 / 2.160 / 2.163 / 2.179 / 2.211 / 2.259 kA at 3.0 / 3.1 / 3.2 / 3.4 / 3.6 / 3.8 Hz;
- 2.412 / 2.465 / 2.525 kA at 4.2 / 4.3 / 4.4 Hz.

The 500 kN B95 values remain moderate over 3.0-3.8 Hz:
- tooth B95 ~1.61-1.66 T;
- yoke B95 ~1.69-1.71 T.

## Operating-band interpretation
1. This direct solve supersedes the earlier 4.1-4.5 Hz thickness-scaling screening estimate for this optimized geometry.
2. The **maximum-thrust/minimum-current plateau is about 3.0-3.2 Hz**, centered near 3.1 Hz.
3. A practical normal operating range is **3.4-3.8 Hz** because it lowers terminal voltage and improves PF while keeping current, losses, and B95 moderate.
4. A preferred sub-band is **3.4-3.6 Hz**, pending transverse-edge correction.
5. The 4.2-4.4 Hz points are feasible but no longer attractive because current, secondary loss, and B95 increase.

## Limitations
- transverse finite-width edge effect is not included in these 2D values;
- normal-force / eccentricity load needs a fresh 16 mm check on this geometry;
- final terminal voltage/PF requires the selected physical winding end geometry and 3D impedance closure;
- the 800 mm stator / wider secondary planform must be reconciled with the quasi-3D transverse-edge study before freezing current.
