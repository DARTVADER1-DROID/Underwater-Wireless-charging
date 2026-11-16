# Underwater Wireless Charging (UWLPT)

Engineering documentation for a 12 V lead-acid-battery-fed, 30 kHz-class underwater wireless power-transfer prototype. The 24 W rating is being clarified as input power versus delivered load power.

## Current analytical coil baseline

| Parameter | Value | Status |
|---|---:|---|
| TX / RX outer diameter | 70 mm each | Current design dimension |
| TX / RX clear inner opening | 20 mm each | Current design dimension |
| Turns per coil | 7 | Current design iteration |
| Insulated wire diameter | 2.7 mm | H05V-U reference; verify exact purchased cable |
| Coil plane separation | 30 mm | Reference calculation |
| TX self-inductance | 2.29631793 µH | Wheeler estimate |
| RX self-inductance | 2.29631793 µH | Wheeler estimate |
| Mutual inductance | 0.3276527625 µH | 49-pair Maxwell filament calculation |
| Coupling coefficient | 0.1426861491 | Preliminary derived estimate |

These are preliminary analytical values, not measured results.

## Engineering documentation

- [Documentation index](docs/README.md)
- [System architecture](docs/architecture/system-architecture.md)
- [Full H-bridge inverter](docs/power-stage/h-bridge-inverter.md)
- [NE555 oscillator and gate-control interface](docs/control/ne555-oscillator.md)
- [Text-based engineering diagrams](docs/diagrams/README.md)
- [TX/RX coil calculations](docs/design/coil-design-and-coupling.md)
- [Research-source index](docs/research/README.md)
- [Formula provenance](docs/research/formulas/formula-provenance.md)
- [Chen et al. paper equations](docs/research/formulas/chen-2024-paper-equations.md)
- [Research paper technical note](docs/research/papers/chen-2024-tile-shaped-underwater-wpt.md)
- [Reproducible coil model](tools/coil_model.py)

## Current system definition

- Input: nominal 12 V lead-acid battery.
- Inverter: four-switch full H-bridge, bipolar square-wave output.
- Timing: NE555-based timing source; 30 kHz target at the bridge/coil must be distinguished from timer pin frequency.
- TX/RX: resonant capacitor and previously calculated TX/RX coils.
- Receiver: high-frequency bridge rectifier and resistive DC load.
- Power: 12 V × 2 A = 24 W is the nominal input if those values refer to the battery side. A 24 W receiver load requires greater input power due to losses.

## Reproduce coil calculations

`python -m pip install scipy` then `python tools/coil_model.py`.

## Status

Analytical coil baseline documented; not yet hardware-validated. Do not infer final resonant capacitors or end-to-end efficiency from the coil estimates alone.
