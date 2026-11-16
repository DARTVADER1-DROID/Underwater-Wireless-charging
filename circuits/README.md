# SPICE model files

This directory retains the preliminary coupled-resonant-link SPICE netlist for numerical experimentation. It is not a graphical circuit diagram.

## File

- [Coupled resonant-link testbench](uwlpt-resonant-link.cir) — idealized series-series compensated TX/RX link.

## Model baseline

| Item | Value | Status |
|---|---:|---|
| Switching frequency | 30 kHz | Project target; exact control implementation pending |
| Differential bridge waveform | -12 V to +12 V | Idealized full-bridge equivalent |
| TX inductance | 2.29631793 uH | Preliminary Wheeler estimate |
| RX inductance | 2.29631793 uH | Preliminary Wheeler estimate |
| Coupling coefficient | 0.14268615 | Preliminary calculated estimate at 30 mm coaxial spacing |
| TX/RX series capacitors | 12.27 uF each | Calculated ideal resonance at 30 kHz |
| Receiver AC load | 12 ohm | Illustrative comparison value from the cited paper, not a project requirement |

The ideal resonance capacitor is calculated from `C = 1 / ((2 pi f)^2 L)`. Actual values must be revisited after measuring the built coils and accounting for capacitor tolerance, ESR, parasitics, encapsulation and operating conditions.

## Validation status

This netlist has not yet been run in an LTspice installation. Inspect the generated netlist and waveforms before relying on simulation results. It is an engineering model, not a complete or hardware-ready charger.

Graphical circuit schematics are intentionally not maintained here; functional block diagrams are in [docs/diagrams](../docs/diagrams/README.md).
