# Energy-storage subsystem

Baseline technology: **supercapacitor**.

Current design authority is the **40 m/s** launch case. Do not size this subsystem from the 170 m/s extension study unless the project baseline is explicitly changed.

## 1. Design status

The storage **technology** is frozen as supercapacitor. The detailed realization remains open:

- manufacturer and part number;
- cell versus module implementation;
- series/parallel count;
- equivalent capacitance and ESR;
- direct coupling versus isolated bidirectional DC/DC;
- cooling architecture;
- regenerative charging power;
- local DC-link film capacitance.

The current objective is to define the storage-to-converter interface before detailed CHB design.

## 2. Electrical interface requirements

For the current 4.5 kV-class CHB candidate:

| Item | Requirement | State |
|---|---:|---|
| Normal H-bridge DC operating window | **2.0-2.5 kV** | CONDITIONAL |
| Derated/emergency lower region | **down to ~1.9 kV** | REFERENCE LIMIT |
| Electrical isolation | **floating source per H-bridge** | FROZEN PRINCIPLE |
| Bidirectional energy flow | **required** | REQUIREMENT |
| Converter insulation interface | compatible with **5 kV interface margin** | CONDITIONAL REQUIREMENT |

The 2.0 kV normal lower limit is selected to retain practical modulation headroom for the 4.5 kV-class converter. Exact withstand, creepage/clearance, grounding and common-mode design remain open until the physical CHB cabinet and PWM insulation design are closed.

## 3. Energy and power requirements

The preliminary 40 m/s storage requirements are:

| Item | Requirement | State |
|---|---:|---|
| System usable stored energy | **>= 16 MJ** | CONDITIONAL REQUIREMENT |
| System peak discharge power | **>= 25 MW** | CONDITIONAL REQUIREMENT |
| Full-power pulse capability | **>= 1.5 s** | CONDITIONAL REQUIREMENT |
| Recharge time | **<= 2 h** | REQUIREMENT |

Basis:

- nominal mission: 12 t moving mass, 50 deg launch angle, approximately constant 3g net acceleration to 40 m/s;
- design propulsion capability: 500 kN total thrust;
- 500 kN at 40 m/s corresponds to 20 MW mechanical output;
- the 16 MJ and 25 MW values include first-round allowances for motor, converter and storage losses plus engineering margin.

These values are screening-grade subsystem requirements. Final stored energy and peak power shall be closed by full launch-profile loss integration.

## 4. Per-H-bridge DC-terminal screening values

For detailed converter work, use the following first-round storage-interface references:

- average H-bridge DC discharge power: **~2.0 MW**;
- low-bus average DC current: **~1.0 kA**;
- short-pulse DC current capability: **>= 2.5 kA**.

These are interface screening values, not frozen supercapacitor ratings. Final values depend on local DC-link ripple buffering and the detailed CHB modulation strategy.

## 5. Local DC-link requirement

Each H-bridge shall include a dedicated low-inductance film DC-link capacitor bank.

The supercapacitor bank shall **not** be treated as the sole sink/source for:

- PWM-frequency ripple current;
- local commutation current;
- the full single-phase double-frequency power ripple.

The final split of average power, 2f ripple power and switching-frequency ripple between the supercapacitor bank and local film capacitors remains open and shall be resolved during detailed converter design.

## 6. Regeneration and braking

The storage system shall support **bidirectional energy acceptance** so that regenerative energy from electromagnetic braking can be returned to storage.

The final regenerative peak power, energy and charge-current requirements remain open until the braking profile and sled mass are fully closed.

## 7. Monitoring and protection requirements

The storage implementation shall provide:

- cell or submodule voltage monitoring;
- cell or submodule temperature monitoring;
- active or passive balancing/equalization as required;
- overvoltage and undervoltage protection;
- overtemperature protection;
- overcurrent and short-circuit isolation;
- precharge control;
- controlled discharge;
- maintenance isolation and safe residual-voltage handling.

## 8. Items intentionally left open

Do not freeze the following from this document alone:

- specific supercapacitor vendor or part number;
- 900S or any other exact series count;
- exact equivalent capacitance;
- exact ESR target;
- exact cooling topology;
- exact number of parallel strings;
- direct-coupled versus DC/DC-coupled storage architecture;
- exact local film-capacitor size.

These items shall be selected after the detailed CHB switching, loss, protection and DC-link ripple analysis.
