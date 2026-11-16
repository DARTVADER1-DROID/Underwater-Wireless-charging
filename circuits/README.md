# LTspice circuits

This directory contains native LTspice-compatible schematics and SPICE testbenches.

## Files

- [H-bridge power-stage schematic](h-bridge-power-stage.asc) — graphical four-MOSFET bridge using idealized gate-to-source pulse sources.
- [Coupled resonant-link testbench](uwlpt-resonant-link.cir) — explicit SPICE netlist for the preliminary series-series compensated wireless link.

## H-bridge schematic assumptions

- Q1/Q4 and Q2/Q3 are alternating diagonal switch pairs.
- Idealized gate-to-source pulses use 10 V amplitude at a 30 kHz repetition rate.
- The pulse timing provides 1 us of non-overlap dead time between diagonal pairs.
- The generic `SWNMOS` model is a simulation placeholder, not a selected MOSFET or a validated loss model.
- The 12 ohm resistor is a test load, not the final resonant transmitter load.
- The ideal gate sources do not represent a real high-side/low-side gate-driver IC, bootstrap supply, undervoltage lockout, gate resistors, or protection circuit.

## Resonant-link model baseline

| Item | Value | Status |
|---|---:|---|
| Switching frequency | 30 kHz | Project target; exact control implementation pending |
| Differential bridge waveform | -12 V to +12 V | Idealized full-bridge equivalent |
| TX inductance | 2.29631793 uH | Preliminary Wheeler estimate |
| RX inductance | 2.29631793 uH | Preliminary Wheeler estimate |
| Coupling coefficient | 0.14268615 | Preliminary calculated estimate at 30 mm coaxial spacing |
| TX/RX series capacitors | 12.27 uF each | Calculated ideal resonance at 30 kHz |
| Receiver AC load | 12 ohm | Illustrative comparison value from the cited paper, not a project requirement |

The ideal resonance capacitor is calculated from `C = 1 / ((2 pi f)^2 L)`. Actual capacitor values must be revisited after measuring the built coils and accounting for capacitor tolerance, ESR, parasitics, water/encapsulation effects, and operating conditions.

## Validation status

The files have been added to the repository and their LTspice text structure and intended pin/wire coordinates have been reviewed. **They have not yet been opened or simulated in an LTspice installation.** Run them in LTspice and inspect the generated netlist and waveforms before relying on results.

These are engineering starting points, not complete or hardware-ready charger designs.

## Next schematic stages

1. Replace ideal gate-drive sources with a selected, datasheet-backed gate-driver and interlock implementation.
2. Select MOSFETs from datasheet voltage/current, gate-charge, switching-loss, and thermal requirements.
3. Add the transmitter resonant branch and coupled receiver coil to a graphical schematic.
4. Add the receiver rectifier and output filter using selected real components.
5. Add measured coil resistance, capacitor ESR, and parasitics.
6. Validate transient stress, resonant current, power transfer, and thermal margins before hardware.
