# Energy-storage subsystem

Baseline technology: **supercapacitor**.

Current design authority is the **40 m/s** launch case.

## 1. Design status

The storage technology remains frozen as **supercapacitor**.

The accepted converter architecture is now:
- 4 H-bridge cells per phase;
- 12 H-bridge cells per three-phase converter;
- each H-bridge uses an electrically floating storage source;
- normal local DC operating window: **1.0-1.1 kV**.

The exact supercapacitor manufacturer, module/cell realization, series/parallel count and cooling implementation remain open.

## 2. Electrical interface requirements

| Item | Requirement | State |
|---|---:|---|
| H-bridge normal DC operating window | **1.0-1.1 kV** | FROZEN INTERFACE |
| Floating source per H-bridge | required | FROZEN PRINCIPLE |
| Bidirectional energy acceptance | required | REQUIREMENT |
| Local DC-link film capacitor | **50 mF nominal, 40-60 mF range** | CONDITIONAL VALUE |
| Film-capacitor voltage rating | **>=1.25 kVDC** | REQUIREMENT |
| Film-capacitor ripple current | **>=2.0 kA RMS; 2.5 kA preferred** | REQUIREMENT |
| Film-capacitor pulse current | **>=5 kA** | REQUIREMENT |

## 3. System-level storage requirements

| Item | Requirement | State |
|---|---:|---|
| System usable stored energy | **>=16 MJ** | CONDITIONAL REQUIREMENT |
| System peak discharge power | **>=25 MW** | CONDITIONAL REQUIREMENT |
| Full-power pulse capability | **>=1.5 s** | REQUIREMENT |
| Recharge time | **<=2 h** | REQUIREMENT |

These remain screening-grade system requirements until full launch-profile loss integration is closed.

## 4. Per-H-bridge storage-source requirements

Current converter-screening references:

### Normal 500 kN point
- average H-bridge power: approximately **0.96 MW**;
- average low-bus DC current: approximately **1.0 kA**;
- source RMS current: approximately **1.4 kA**.

### 3.5 kA RMS design envelope
- source RMS current capability: **>=2.1 kA for 1.5 s**;
- source peak current capability: **>=4.5 kA**.

Source-path impedance requirements:
- target equivalent resistance: **<=10 mOhm**;
- approximately **15 mOhm** is the upper conditional limit for the normal ~2.35 kA operating point;
- source-feed inductance: **<=3 uH**.

Excess source ESR cannot be compensated by simply increasing local film capacitance.

## 5. Power-ripple split

The accepted power-ripple policy is:

- supercapacitor source carries **average power and most low-frequency 2f power pulsation**;
- local film DC-link bank carries **PWM-frequency and commutation ripple current**.

The supercapacitor bank shall not be relied on as the sole high-frequency ripple sink.

## 6. Regeneration

The storage system shall support **bidirectional energy acceptance** for electromagnetic braking.

Final regenerative peak power and energy remain open until the braking profile is closed.

## 7. Monitoring and protection requirements

The storage implementation shall provide:
- cell/submodule voltage monitoring;
- cell/submodule temperature monitoring;
- balancing/equalization;
- overvoltage and undervoltage protection;
- overtemperature protection;
- overcurrent and short-circuit isolation;
- precharge control;
- controlled discharge;
- maintenance isolation and residual-voltage handling.

## 8. Items still open

Do not freeze from this document alone:
- supercapacitor vendor or part number;
- exact series/parallel count;
- exact equivalent capacitance;
- exact cooling topology;
- direct-coupled versus isolated bidirectional DC/DC realization, if later needed for source-impedance compliance;
- final regenerative charging power.

The 1.0-1.1 kV electrical interface and source-impedance targets are part of the accepted converter/storage baseline.
