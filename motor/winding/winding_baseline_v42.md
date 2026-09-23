# DSLIM V2 V4.2 winding baseline

Status: **current winding baseline**

## Geometry

The V4.2 winding is the current winding form for the accepted V2 motor geometry.

- 3.0 m stator segment, 36 slots, q = 2;
- 500 mm pole pitch and 500 mm paired-slot span;
- 3 equivalent turns;
- V4.2 low-loop-area paired-slot back-connected topology;
- six end-turn layers with 12 mm layer pitch;
- rounded end transitions;
- A/C/B phase-separated routing corridors;
- top/bottom stators route on opposite +/-Y sides;
- phase-to-phase, winding-to-core and winding-to-secondary Boolean intersections are zero in the validated representative model.

The 24 x 46 mm slot pack is a homogenized three-turn geometric envelope, not solid copper.

## Copper conductor reference

Current loss calculations use:
- 300 mm2 copper per turn — CONDITIONAL;
- design sensitivity range 280-320 mm2;
- copper temperature 80 degC;
- rho20 = 1.724e-8 ohm m;
- alpha = 0.00393 / degC;
- initial AC-resistance multiplier = 1.05 at about 43-44 Hz.

## 3D-CAD-derived phase lengths — one 3 m stator face

| Phase | Copper path |
|---|---:|
| A | 57.641 m |
| B | 61.943 m |
| C | 62.951 m |
| Average | 60.845 m |

At 80 degC and 300 mm2/turn:

| Phase | One 3 m face | Four same-station faces in series |
|---|---:|---:|
| A | 4.094 mOhm | 16.374 mOhm |
| B | 4.399 mOhm | 17.596 mOhm |
| C | 4.471 mOhm | 17.882 mOhm |
| Average phase | 4.321 mOhm | 17.284 mOhm |

One converter feeding one 3 m longitudinal segment therefore sees about 17.28 mOhm average phase resistance.

The three-phase loss-equivalent resistance of one energized 3 m segment is 51.852 mOhm. Two- and three-segment values are 103.705 and 155.557 mOhm **for total copper-loss accounting only**. Adjacent longitudinal segments are independent converter branches and are not electrically series-connected.

## Handover loss

For unequal currents during handover:

`Pcu = 1.05 * 0.0518524262 * (I1^2 + I2^2 + I3^2)`

with currents in A and power in W.

At 500 kN / 3.6 Hz / 2.345 kA:
- one full-current segment: 299 kW;
- two: 599 kW;
- three: 898 kW.

At the 3.5 kA pulse envelope:
- one: 667 kW;
- two: 1.334 MW;
- three: 2.001 MW.

The 3.5 kA values are short-pulse screening values, not continuous thermal ratings.
