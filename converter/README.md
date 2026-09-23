# Converter subsystem

Current family: **cascaded H-bridge (CHB)**.

Current design authority is the accepted **40 m/s V2 motor baseline**.

## 1. Frozen converter architecture

The accepted converter baseline is:

- three-phase CHB;
- **4 H-bridge cells per phase**;
- **12 H-bridge cells per three-phase converter**;
- three longitudinal converter groups remain frozen;
- **36 floating H-bridge cells** across the three longitudinal groups;
- semiconductor technology: **1700 V / 3600 A-class single-switch IGBT modules**;
- **one IGBT module per switch position; no semiconductor paralleling**;
- normal H-bridge DC operating window: **1.0-1.1 kV**;
- converter output class: **4.5 kV line-line**;
- design current envelope: **3.5 kA RMS pulse class**.

Reference device: Infineon **FZ3600R17HP4_B2** or a verified equivalent 1700 V / 3600 A-class module.

Derived device count:
- 4 IGBT modules per H-bridge;
- 48 IGBT modules per three-phase converter;
- 144 IGBT modules across the three longitudinal converter groups.

## 2. 40 m/s electrical operating reference

Current V2 motor screening gives:
- 500 kN design-capability terminal voltage: approximately **4.01-4.15 kV line-line**;
- 500 kN / 3.6 Hz finite-width current reference: approximately **2.35 kA RMS**;
- PF approximately **0.70**.

At **1.0 kV/cell**, the present ~4.066 kV operating reference requires modulation index about **0.83**. The full **4.5 kV converter class** requires about **0.919**, still inside linear modulation capability for the four-cell-per-phase CHB.

## 3. Semiconductor current and thermal screening

Converter-screening simulations for the accepted topology give:

### Normal 500 kN reference
- phase current: **2.345 kA RMS**;
- worst single-IGBT RMS current: approximately **1.46 kA**;
- worst single-IGBT peak current: approximately **3.32 kA**;
- 1.5 s screening junction-to-case temperature rise: approximately **15 K**.

### 3.5 kA RMS design envelope
- worst single-IGBT RMS current: approximately **2.18 kA**;
- worst single-IGBT peak current: approximately **4.95 kA**;
- 1.5 s screening junction-to-case temperature rise: approximately **29 K**.

Conclusion: the baseline uses **single IGBT modules without paralleling**. Final double-pulse/RBSOA and hardware thermal validation are still required.

## 4. PWM and switching frequency

Baseline control principle:
- phase-shifted-carrier PWM across the four cascaded H-bridge cells per phase;
- nominal device switching frequency: **300 Hz** — CONDITIONAL;
- targeted screening range: **250-400 Hz**.

The topology is frozen. The switching frequency may move within the screening range after detailed loss, EMI, acoustic and double-pulse validation without reopening the converter architecture.

## 5. Local DC-link capacitor

Each H-bridge shall use a dedicated low-inductance polypropylene-film DC-link capacitor bank.

Current nominal design:
- capacitance: **50 mF/H-bridge** — CONDITIONAL;
- design range: **40-60 mF**;
- capacitor voltage rating: **>=1.25 kVDC**;
- ripple-current capability: **>=2.0 kA RMS**, **2.5 kA RMS preferred**;
- short-pulse current capability: **>=5 kA**.

The local film capacitor bank is intended mainly for PWM-frequency and commutation current. The supercapacitor source shall carry average power and most low-frequency double-frequency power pulsation.

## 6. Storage-source electrical interface

To retain the **1.0 kV normal lower DC-link limit**:

- target total source-path equivalent resistance per H-bridge: **<=10 mOhm**;
- approximately **15 mOhm** is the upper conditional limit for the ~2.35 kA normal point, but does not guarantee the full 3.5 kA envelope;
- storage feed inductance: **<=3 uH**.

At the 3.5 kA RMS design-envelope screening point, using:
- 50 mF local DC link,
- 10 mOhm source resistance,
- 3 uH feed inductance,

the simulated minimum local DC-link voltage is approximately **999 V** with about **67.9 Vpp** ripple.

Increasing film capacitance cannot compensate excessive source ESR because the average source-current voltage drop remains.

## 7. Commutation-loop parasitic target

Do not confuse the microhenry-scale storage-feed inductance with the nanohenry-scale IGBT commutation loop.

Current targets:
- total commutation-loop stray inductance: **<=25 nH**;
- external busbar plus capacitor-connection target: **<=20 nH**.

Final clamp/snubber design and allowable turn-off overshoot require double-pulse testing or equivalent validated hardware parasitic extraction.

## 8. Detailed hardware items still open

1. double-pulse turn-off overvoltage and RBSOA verification at 1.1 kV DC link;
2. final active-clamp/snubber design;
3. measured/extracted commutation-loop parasitic inductance;
4. final DC-link film-capacitor thermal/lifetime validation;
5. supercapacitor branch ESR/ESL realization;
6. cooling-plate and cabinet design;
7. precharge, discharge, bypass and fault-isolation hardware;
8. final PWM insulation and common-mode stress verification.

The converter topology, cell count, device voltage/current class, single-device policy and 1.0-1.1 kV/cell operating window are baseline decisions.
