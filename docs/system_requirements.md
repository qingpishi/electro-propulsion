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
- Four independently controlled stator faces
- Left/right differential thrust capability retained
- Opposed-face current trim retained for residual normal-force compensation

## 3. Braking reference

The payload is released before braking. For a 2 t sled and 10 g net deceleration on a 50 deg incline:

```
F_brake,em ~= 181 kN
```

Use ~200 kN as the preliminary electromagnetic braking design level until the final sled mass is frozen.

## 4. Architecture constraints

- Use a dual-channel, double-sided long-primary LIM.
- Each stator face is three-phase.
- Main propulsion segments that are simultaneously active use equal current.
- Energized stator length must remain greater than the effective secondary length.
- Preserve magnetic-field continuity ahead of and behind the secondary during segment handover.
- A fourth segment may be pre-excited for handover, but the exact pre-excitation strategy remains open.
