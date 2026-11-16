# System Architecture and Design Status

## Energy path

1. A nominal 12 V lead-acid battery supplies the transmitter DC bus.
2. An NE555 timer provides the timing reference.
3. Logic generates the required bridge switching sequence and non-overlap dead time.
4. Two half-bridge gate drivers drive the four MOSFETs in a full H-bridge.
5. The H-bridge produces a bipolar square-wave voltage across the TX resonant branch.
6. The TX compensation capacitor and TX coil establish the primary resonant circuit.
7. Magnetic coupling transfers energy to the RX coil across the water gap.
8. The RX coil and compensation capacitor form the secondary resonant circuit.
9. A high-frequency bridge rectifier converts receiver AC to DC.
10. A resistive load is connected to the receiver DC output.

See [the system diagram](../diagrams/system-overview.md).

## Current project inputs

| Parameter | Current value | Status |
|---|---:|---|
| Battery nominal voltage | 12 V | Specified |
| Battery chemistry | Lead-acid | Specified |
| Input current | 2 A mentioned | Meaning/location to confirm |
| Power rating | 24 W | Input-versus-output definition unresolved |
| Resonant-link frequency | 30 kHz target | Paper-informed target; verify at coil |
| Inverter topology | Full H-bridge | Selected |
| TX/RX coil outer diameter | 70 mm each | Current coil design |
| Turns per coil | 7 | Current coil design |
| Reference axial separation | 30 mm | Analytical reference point |
| TX self-inductance | 2.29631793 µH | Wheeler estimate |
| RX self-inductance | 2.29631793 µH | Wheeler estimate |
| Mutual inductance | 0.3276527625 µH | Coaxial circular-filament calculation |
| Coupling coefficient | 0.1426861491 | Derived from the above estimates |
| Receiver load | Resistive | Specified load type |

Detailed coil geometry and derivations are in [the wireless-link section](../03-wireless-link/README.md).

## Power accounting

The expression 12 V × 2 A = 24 W describes 24 W at the battery terminals only if 2 A is the battery-side DC current at that operating voltage.

It does not imply 24 W at the receiver. For end-to-end efficiency η:

- Receiver output power = battery input power × η.
- Required battery current = receiver output power ÷ (loaded battery voltage × η).

The battery voltage under load will not remain exactly 12.0 V. Battery capacity (Ah), discharge runtime, allowable depth of discharge, battery condition and system efficiency are not yet specified. Therefore, no battery capacity or runtime is locked.

## Frequency accounting

The target is 30 kHz at the resonant link / H-bridge differential output. Do not assume the NE555 pin-3 clock must itself be 30 kHz: the result depends on the chosen logic architecture. For example, a divide-by-two stage requires a 60 kHz timer clock to produce a 30 kHz bridge cycle.

The selected paper reports a 30 kHz preferred seawater simulation frequency, but its reported component table and resonant values need to be treated as a separate research configuration, not copied directly into this prototype.

## Design boundaries and safety

- The NE555 is a timing source, not a four-channel MOSFET gate driver.
- High-side MOSFETs require suitable high-side gate-drive supplies/bootstrapping.
- Dead time must prevent both MOSFETs in either bridge leg from conducting simultaneously.
- A fuse must be placed close to the battery positive terminal.
- Begin with a current-limited bench supply, not an unrestricted battery.
- Verify gate waveforms, bridge voltage, resonant current, device stress and temperature before sustained operation.
- The receiver rectifier must be selected for the actual secondary waveform, reverse voltage, current, switching loss and thermal conditions.

## Open decisions

1. Does 24 W mean battery-side input power or power delivered to the receiver load?
2. Is the 2 A figure battery current, bridge current, TX coil current, or another measured current?
3. Does 30 kHz refer to timer clock, H-bridge differential voltage, or resonant coil current?
4. What battery Ah rating and operating runtime are required?
5. What exact control logic and dead-time implementation will be used?
6. Which MOSFETs, gate drivers and rectifier will be selected?
7. What compensation topology and capacitor values will be used after measured coil parameters are available?
8. What receiver DC voltage is required, and therefore what load resistance and power rating are required?
