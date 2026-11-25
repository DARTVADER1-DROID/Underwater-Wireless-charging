# LTspice inverter experiment

This folder contains the original LTspice schematic, preserved as supplied. It is a preliminary standalone 12 V H-bridge inverter experiment associated with the transmitter power-electronics work; it is **not** the complete underwater wireless power-transfer transmitter or a validated 30 kHz design.

## Schematic

- [inverter.asc](inverter.asc) — original LTspice schematic; four N-channel BSC010NE2LS MOSFETs in an H-bridge, driven by two ground-referenced pulse sources, with a 1 ohm differential load.

## Parameters encoded in the schematic

| Parameter | Schematic value |
|---|---:|
| DC source | 12 V |
| MOSFETs | 4 × BSC010NE2LS |
| Pulse-source levels | 0–12 V |
| Pulse period | 20 ms |
| Pulse width | 10 ms |
| Nominal switching frequency | 50 Hz |
| Load R1 | 1 ohm |
| Transient analysis | 1 s |

## Important interpretation and limitations

- The two pulse sources are complementary, but the schematic does not implement explicit dead time.
- All four devices are N-channel MOSFETs. The high-side gates are driven by ground-referenced 0–12 V sources; this does not provide a proper floating high-side gate drive as the switch node rises. High-side VGS must be checked before interpreting the bridge as an ideal switch.
- The schematic is preserved unchanged. No gate-driver redesign, component substitution, or simulation-result claims have been added.
- No LTspice run or waveform validation is asserted by storing this file in the repository.
- The 50 Hz inverter test is distinct from the project's 30 kHz wireless-power-transfer operating target. Do not treat its values as the final transmitter specification.

## Suggested next validation

In LTspice, inspect differential load voltage V(inverter+,inverter-), each MOSFET's actual gate-to-source voltage, load current, and input power. Test a controlled range of load resistances and record waveforms before changing the circuit.
