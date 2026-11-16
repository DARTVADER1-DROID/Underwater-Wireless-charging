# Underwater Wireless Charging (UWLPT)

Engineering documentation for a 12 V DC, 24 W underwater wireless power-transfer prototype.

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
| Coupling coefficient | 0.1426861491 | Derived, dimensionless |

**These are preliminary analytical values, not measured results.** The self-inductance uses Wheeler's approximate flat-spiral equation. Mutual inductance uses ideal circular filament turns in free space. Their ratio is therefore a preliminary mixed-model estimate of coupling.

## Documentation

- [Readable coil geometry, inductance and coupling calculations](docs/design/coil-design-and-coupling.md)
- [Research-source index](docs/research/README.md)
- [Readable formula provenance and derivations](docs/research/formulas/formula-provenance.md)
- [Equations from the Chen et al. research paper](docs/research/formulas/chen-2024-paper-equations.md)
- [Research paper technical note](docs/research/papers/chen-2024-tile-shaped-underwater-wpt.md)
- [Reproducible numerical model](tools/coil_model.py)

## Project requirements and unresolved decisions

- DC input: 12 V
- Target transferred power: 24 W
- Transmitter: full H-bridge
- TX current target: 2 A AC; RMS definition and measurement point still need clarification
- Artificial saltwater target: approximately 35 g/kg; conductivity must be measured at test temperature
- Coil separation study range: 20–40 mm; 30 mm is the fully documented reference calculation

Operating frequency, compensation topology, final conductor, waterproofing, ferrite/shielding, receiver rectifier and thermal limits are not finalized.

## Reproduce the numerical calculation

Install SciPy and run:

```bash
python -m pip install scipy
python tools/coil_model.py
```

The script prints geometry, Wheeler self-inductance, the 7 × 7 mutual-inductance matrix, a direct Neumann-integral numerical cross-check and the coupling coefficient.

## Engineering status

**Analytical baseline documented; not hardware-validated.** Do not select resonant capacitors or claim power-transfer efficiency from these inductance estimates alone. Validate the finite-conductor coil geometry using an electromagnetic field solver and then measure the fabricated coils.

## Source policy

Research-paper equations and reported values are kept separate from the project's own calculations. Never substitute the paper's coil parameters into this design without recalculation.
