# Engineering Documentation Index

## System architecture
- [System architecture](architecture/system-architecture.md)
- [System block diagram](diagrams/system-block-diagram.mmd)

## Transmitter power stage
- [12 V full H-bridge design](power-stage/h-bridge-inverter.md)
- [H-bridge diagram](diagrams/h-bridge-power-stage.mmd)

## Oscillator and control
- [NE555 oscillator](control/ne555-oscillator.md)
- [NE555 timing diagram](diagrams/ne555-timing.mmd)
- [Bridge switching sequence](diagrams/h-bridge-switching-timing.mmd)

## Coil design and research
- [TX/RX coil calculations](design/coil-design-and-coupling.md)
- [Research source index](research/README.md)
- [Formula provenance](research/formulas/formula-provenance.md)
- [Chen et al. paper equations](research/formulas/chen-2024-paper-equations.md)
- [Chen et al. paper review](research/papers/chen-2024-tile-shaped-underwater-wpt.md)

## Reproducible model
- [Coil calculation script](../tools/coil_model.py)

## Status convention
- Requirement: explicitly specified by the project owner.
- Calculated: derived from stated inputs and a named method.
- Candidate: under evaluation, not selected.
- Open: information needed before final design.
- Validated: checked by simulation or measurement with evidence recorded.

A functional diagram is not automatically a verified electrical schematic.
