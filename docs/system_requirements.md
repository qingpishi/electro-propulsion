# System Requirements Baseline

## 1. Mission profile

| Item | Baseline |
|---|---:|
| Payload mass | 10,000 kg |
| Sled target mass | 2,000 kg |
| Sled design upper limit | 2,500 kg |
| Launch inclination | 50 deg |
| Exit speed | 40 m/s |
| Net acceleration | 3 g, approximately constant |
| Launch interval | >= 2 h |
| Energy storage | Supercapacitor |
| Main converter family | Cascaded H-bridge (CHB) |
| Braking object | Sled only after payload separation |
| Braking target | 10 g net deceleration |
| High-speed extension | 170 m/s analysis only; not a baseline driver |

## 2. Propulsion requirements

For the nominal 12 t moving mass:

```
F_em = m * (3g + g sin(50 deg))
     ~= 443.2 kN
```

The motor design capability is:

- Total design thrust: **500 kN**
- Per DSLIM channel: **250 kN**
- Four stator faces at the same longitudinal station are connected in series and carry the same three-phase current
- Three interleaved longitudinal converter groups are used: A -> G1/G4/G7..., B -> G2/G5/G8..., C -> G3/G6/G9...
- Differential face-current trim is no longer part of the baseline architecture; thrust-centering is obtained primarily by common series current and mechanical guide stiffness

## 3. Braking reference

The payload is released before braking. For a 2 t sled and 10 g net deceleration on a 50 deg incline:

```
F_brake,em ~= 181 kN
```

Use ~200 kN as the preliminary electromagnetic braking design level until the final sled mass is frozen.

## 4. Architecture constraints

- Use a dual-channel, double-sided long-primary LIM.
- Each stator face is three-phase.
- Basic stator segment length is 3.0 m; two adjacent main segments provide a 6.0 m energized window.
- Effective secondary length is 4.5 m.
- Energized stator length must remain greater than the effective secondary length.
- Three longitudinal converter groups reuse converters every three segments; current ramp reference is 10 ms.
- Preserve magnetic-field continuity during segment handover.
- Mechanical gaps between stator modules are not a dedicated thrust-ripple design item in the current baseline.
