# LTspice circuits

This directory contains native LTspice-compatible circuit files.

## Current model

- [Coupled resonant link testbench](uwlpt-resonant-link.cir)

The current file is a **first-pass AC link model**, not a complete charger schematic. It models the bridge output as an ideal bipolar source and models the transmitter and receiver coils as coupled inductors. It does not yet contain MOSFET gate drivers, dead-time logic, a physical rectifier, output filter, protection, or a validated battery/load interface.

Open the `.cir` file in LTspice and run the transient analysis. The file is deliberately a netlist so that its electrical connectivity is explicit and reviewable.

## Model status

| Item | Value | Status |
|---|---:|---|
| Switching frequency | 30 kHz | Project target; exact control implementation pending |
| Differential bridge waveform | -12 V to +12 V | Idealized full-bridge equivalent |
| TX inductance | 2.29631793 µH | Preliminary Wheeler estimate |
| RX inductance | 2.29631793 µH | Preliminary Wheeler estimate |
| Coupling coefficient | 0.14268615 | Preliminary calculated estimate at 30 mm coaxial spacing |
| TX/RX series capacitors | 12.27 µF each | Calculated ideal resonance at 30 kHz |
| Receiver AC load | 12 Ω | Illustrative comparison value from the cited paper, not a project requirement |

The ideal resonance capacitor is calculated from (C=1/( (2\pi f)^2 L )). The actual capacitor values must be revisited after measuring the built coils and accounting for capacitor tolerance, ESR, parasitics, water/encapsulation effects, and operating conditions.

## Next schematic stages

1. Replace the ideal bridge source with a pin-accurate MOSFET H-bridge and gate-driver implementation.
2. Add the receiver rectifier and output filter using selected real components.
3. Add measured coil models, winding resistance, capacitor ESR, and parasitics.
4. Validate transient stress, resonant current, power transfer, and thermal margins before hardware.
