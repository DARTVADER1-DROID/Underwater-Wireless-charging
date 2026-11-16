# Underwater Wireless Power Transfer

Design and engineering record for a 12 V lead-acid-battery-fed underwater wireless power-transfer prototype.

## System at a glance

- **Input source:** nominal 12 V lead-acid battery.
- **Transmitter:** NE555 timing source, switching logic with dead time, MOSFET full H-bridge.
- **Wireless link:** compensated TX and RX coils; current analytical baseline is documented separately.
- **Receiver:** high-frequency bridge rectifier and resistive DC load.
- **Frequency target:** 30 kHz at the resonant link, pending confirmation against the exact frequency definition in the selected paper and the final control architecture.
- **Power target:** 24 W is not yet classified as battery input power or delivered receiver-load power.

## Documentation

| Section | Contents |
|---|---|
| [System](docs/01-system/README.md) | Architecture, requirements and open decisions |
| [Transmitter](docs/02-transmitter/README.md) | NE555 timing, H-bridge and gate drive |
| [Wireless link](docs/03-wireless-link/README.md) | TX/RX coil geometry, inductance and coupling |
| [Receiver](docs/04-receiver/README.md) | Rectifier, output filtering and load |
| [Research](docs/05-research/README.md) | Research paper, equation notes and source provenance |
| [Diagrams](docs/diagrams/README.md) | System, inverter, timing and receiver diagrams |

## Reproducible coil calculation

Install SciPy and run:

```bash
python -m pip install scipy
python tools/coil_model.py
```

## Engineering status

The coil values are analytical estimates, not measured hardware results. The inverter, gate-drive, compensation, rectifier and battery operating points still require component-level design, simulation and measurement. Do not treat a functional block diagram as a production-ready schematic.
