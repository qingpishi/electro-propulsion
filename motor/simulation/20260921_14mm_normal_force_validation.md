# 14 mm air-gap normal-force / eccentricity recalculation

Status: **engineering validation of the current 40 m/s baseline; baseline parameters unchanged**

## Model
- Baseline: DSLIM-V1-candidate-40mps-tau500
- Speed: 40 m/s
- Main result slip frequency: 3.0 Hz
- Current: 1430 A RMS per stator face
- Pole pitch: 500 mm
- q = 2
- Main energized length: 6.0 m
- Continuous secondary length: 5.8 m
- Stator effective width/depth in 2D model: 600 mm
- Nominal single-side gap: 14 mm
- Aluminium secondary thickness: 12 mm
- Nonlinear 35WW300 engineering B-H model
- Moving-conductor harmonic FEM, SUPG factor 0.05
- High-resolution mesh: about 76,755 nodes / 152,064 triangles
- Longitudinal end effect included
- Transverse edge effect not included

Positive eccentricity means the secondary moves toward the top stator:
- g_top = 14 mm - e
- g_bottom = 14 mm + e

## 3 Hz high-resolution result

| Eccentricity | Top / bottom gap | Net Fy per channel | Top face attraction | Bottom face attraction |
|---:|---:|---:|---:|---:|
| 0 mm | 14 / 14 mm | 0 kN | 99.04 kN | 99.04 kN |
| +0.25 mm | 13.75 / 14.25 mm | -0.739 kN | 98.65 kN | 99.41 kN |
| +0.50 mm | 13.5 / 14.5 mm | -1.479 kN | 98.24 kN | 99.78 kN |
| +1.00 mm | 13 / 15 mm | -3.060 kN | 96.82 kN | 99.88 kN |

Negative sign means restoring force for the stated coordinate convention.

Linear fit around the studied range:

```
Fy/e ~= -3.04 kN/mm per DSLIM channel
```

Longitudinal thrust changes by less than about 0.2% at 1 mm eccentricity in this model.

## Force-method cross-check

The residual normal force was calculated from:
1. Lorentz-force integration in the conducting secondary; and
2. Maxwell-stress integration in the two air gaps.

At the high-resolution points the two methods agree within roughly 0.06 kN at e=0.5 mm and nearly exactly at e=1 mm, supporting the numerical stability of the residual-force result.

## Slip-frequency sensitivity

At 2.44 Hz and the same 1430 A:
- centered absolute attraction increases to about 126 kN per stator face;
- residual force is about 1.71 kN/channel at e=0.5 mm;
- residual force is about 3.43 kN/channel at e=1.0 mm.

Therefore structural sizing should not use only the 3 Hz absolute-attraction value if operation near the maximum-thrust slip plateau is allowed.

## Differential-current compensation

At e=+0.5 mm, 3 Hz:
- equal-current residual Fy: about -1.48 kN/channel;
- delta = (Itop-Ibottom)/(Itop+Ibottom) ~= -0.8% gives Itop ~= 1418.6 A and Ibottom ~= 1441.4 A;
- high-resolution residual Fy falls to about -0.06 kN/channel.

First 40 m/s compensation gain:

```
delta/e ~= -1.6 % per mm
```

This is a preliminary control calibration, not a structural safety feature.

## Mechanical interpretation

The dominant structural load is the **absolute face attraction**, not the small residual eccentricity force.

For one DSLIM channel:
- ~99 kN per face at 3 Hz;
- up to ~126 kN per face near 2.44 Hz at the same 1430 A.

Use at least **130 kN per stator face as an initial electromagnetic structural screening load** at 40 m/s before applying dynamic, manufacturing, model-uncertainty and safety factors.

The guide structure should withstand eccentricity loads without relying on active differential-current compensation.

## Limitation

The present 2D model predicts restoring magnetic behavior. This must **not** be credited as a safety mechanism before 3D finite-width and transient validation.
