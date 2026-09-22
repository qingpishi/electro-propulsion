# Converter subsystem

Current family: **cascaded H-bridge (CHB)**.

Current design authority is the accepted **40 m/s V2 motor baseline**.

## 1. Current converter interface

The present conditional converter envelope is:

- line-line output class: **4.5 kV**;
- pulse/current capability: **3.5 kA RMS class**;
- current 500 kN motor screening point: approximately **4.01-4.15 kV line-line** and **2.18-2.26 kA RMS direct-2D current**;
- 1.2 m transverse-edge screening reference at 3.6 Hz: approximately **2.35 kA RMS**;
- retain a **5 kV insulation/interface margin** pending final PWM insulation and physical winding closure.

The former ~3.3 kV / ~1.8 kA V1-era interface is superseded and shall not be used for current detailed design.

## 2. Current CHB candidate

The current detailed-design candidate is:

- **2 H-bridge cells per phase**;
- **6 H-bridge cells per three-phase converter**;
- three longitudinal converter groups remain the system baseline;
- candidate semiconductor voltage class: **4.5 kV**;
- candidate cell DC operating window: **2.0-2.5 kV**;
- each H-bridge requires an electrically floating DC source.

The exact semiconductor part number, switching frequency, snubber/clamp network, local DC-link capacitance and storage coupling architecture remain open.

## 3. Storage interface

Use the requirements in `energy_storage/README.md` for detailed converter work.

First-round per-H-bridge storage-interface references are:

- average DC discharge power: ~**2 MW**;
- low-bus average DC current: ~**1 kA**;
- short-pulse DC current capability: **>=2.5 kA**;
- dedicated low-inductance local film DC-link buffering is required;
- bidirectional regenerative energy flow is required.

## 4. Detailed-design items still open

1. final 4.5 kV semiconductor topology and device count;
2. switching-frequency and modulation strategy;
3. conduction and switching loss model over the launch pulse;
4. IGCT/IGBT/diode current sharing and thermal transient;
5. local DC-link capacitance and 2f ripple-power split;
6. clamp/snubber and stray-inductance limits;
7. precharge, bypass, fault isolation and crowbar strategy;
8. cell-level control, synchronization and segment handover;
9. insulation coordination and common-mode/PWM stress;
10. converter cooling and cabinet mechanical layout.
