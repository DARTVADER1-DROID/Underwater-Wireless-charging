# LTspice circuits

This directory contains native LTspice-compatible circuit files.

## Current model

- [Coupled resonant link testbench](uwlpt-resonant-link.cir)

The current files are **simulation starting points**, not complete charger schematics. The symbol-based [H-bridge power-stage schematic](h-bridge-power-stage.asc) uses four generic NMOS devices and ideal gate-to-source pulse sources so the switching topology and dead time can be inspected visually. It is not a hardware-ready driver design. It models the bridge output as an ideal bipolar source and models the transmitter and receiver coils as coupled inductors. It does not yet contain MOSFET gate drivers, dead-time logic, a physical rectifier, output filter, protection, or a validated battery/load interface.

Open the `.asc` schematic or `.cir` netlist in LTspice. The H-bridge schematic is a graphical electrical drawing; the resonant-link netlist remains an explicit SPICE model.

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

## H-bridge schematic assumptions\n\n- Q1/Q4 and Q2/Q3 are alternating diagonal switch pairs.\n- Idealized gate-to-source pulses use 10 V amplitude and 1 us dead time at 30 kHz.\n- The generic `SWNMOS` model is a simulation placeholder, not a selected MOSFET or a validated loss model.\n- The 12 ohm resistor is a test load, not the final resonant transmitter load.\n- The ideal gate sources do not represent a real high-side/low-side gate-driver IC, bootstrap supply, undervoltage lockout, or protection circuit.\n- Check the generated netlist and run the schematic in LTspice before relying on any waveform.\n\n## Next schematic stages

1. Replace the ideal bridge source with a pin-accurate MOSFET H-bridge and gate-driver implementation.
2. Add the receiver rectifier and output filter using selected real components.
3. Add measured coil models, winding resistance, capacitor ESR, and parasitics.
4. Validate transient stress, resonant current, power transfer, and thermal margins before hardware.
