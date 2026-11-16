# Underwater Wireless Charging (UWLPT)

Engineering documentation for a 12 V DC, 24 W underwater wireless power transfer prototype.

## Current design baseline

The current documented coil model is a **preliminary air-core analytical reference**, not a validated underwater design:

- TX and RX: identical, coaxial, single-layer circular planar spiral coils
- Outer diameter: 70 mm each
- Inner opening diameter: 20 mm each
- Turns: 7 each
- Conductor: 1.0 mm² solid copper, PVC-insulated H05V-U reference wire
- Nominal insulated wire diameter: 2.7 mm
- Derived clear spacing between adjacent insulated turns: 1.0167 mm
- Reference axial coil-plane separation: 30 mm (study range: 20–40 mm)
- Wheeler self-inductance estimate: 2.2963 µH per coil
- Maxwell/Neumann filament-pair mutual-inductance estimate: 0.327653 µH at 30 mm
- Derived preliminary coupling coefficient: 0.142686

These values are explicitly conditional on the geometry and assumptions documented below. They must not be treated as measured or seawater-validated values.

## Documentation

- [Coil geometry, self-inductance, mutual inductance and coupling calculation](docs/design/coil-design-and-coupling.md)
- [Research-source index](docs/research/README.md)
- [Formula provenance and applicability](docs/research/formulas/formula-provenance.md)
- [Equations and findings transcribed from the underwater WPT paper](docs/research/formulas/chen-2024-paper-equations.md)
- [Research paper technical note](docs/research/papers/chen-2024-tile-shaped-underwater-wpt.md)
- [Reproducible numerical model](tools/coil_model.py)

## Project requirements and unresolved decisions

- DC input: 12 V
- Target transferred power: 24 W
- Full H-bridge transmitter inverter
- TX current target: 2 A AC (RMS/measurement point still needs explicit definition)
- Artificial saltwater target: approximately 35 g/kg salinity
- Coil separation design range: 20–40 mm; 30 mm is the calculation reference

Operating frequency, compensation topology, actual conductor suitability at frequency, waterproofing/encapsulation, ferrite or shielding, receiver rectifier, and thermal limits are not yet finalized.

## Reproduce the calculation

The numerical model uses SciPy for complete elliptic integrals and numerical quadrature:

```bash
python -m pip install scipy
python tools/coil_model.py
```

The script prints the turn geometry, Wheeler self-inductance estimate, 7 × 7 Maxwell mutual-inductance matrix, a direct Neumann-integral cross-check, and the derived coupling coefficient. It includes numerical and physical consistency assertions.

## Engineering status

**Status: analytical baseline documented; not hardware-validated.**

Do not choose resonant capacitors or claim transfer efficiency from the present inductance/coupling estimates alone. Next validation work should use a field solver with the real finite conductor, coil alignment, surrounding materials and measured saltwater conductivity, followed by LCR/impedance measurements on the fabricated coils.

## Source and attribution policy

Research-derived formulas and paper-specific parameters are separated under [docs/research](docs/research/README.md). Research values are not silently substituted for this prototype's design values.