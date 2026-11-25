# SPICE model files

This directory contains SPICE models and LTspice schematics used for numerical and circuit-level experimentation.

## Files

- [Coupled resonant-link testbench](uwlpt-resonant-link.cir) — idealized series-series compensated TX/RX link.
- [LTspice inverter experiment](ltspice/inverter.asc) — original four-N-channel-MOSFET H-bridge schematic, preserved as supplied. See [its notes](ltspice/README.md).

## Model baseline: coupled resonant link

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

The coupled-link netlist has not yet been run in an LTspice installation. The inverter schematic is stored as a source design, not as evidence of a validated simulation. Inspect the schematics and generated waveforms before relying on simulation results. These are engineering models, not a complete or hardware-ready charger.

Functional block diagrams remain in [docs/diagrams](../docs/diagrams/README.md).
