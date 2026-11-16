# UWLPT System Architecture

**Baseline:** 12 V DC input, 24 W target, underwater inductive power transfer.

## Functional path

The transmitter converts DC into controlled high-frequency alternating voltage. The TX compensation network and coil generate an alternating magnetic field. The RX coil receives energy; the receiver compensation, rectifier and regulator deliver DC to the load.

## Current inputs

| Parameter | Value | Status |
|---|---:|---|
| DC input | 12 V | Requirement |
| Target transferred power | 24 W | Requirement |
| Nominal output target | 12 V, 2 A | Target; regulation tolerance and exact measurement point open |
| Inverter | Full H-bridge | Selected topology |
| TX / RX outer diameter | 70 mm each | Current geometry |
| Turns | 7 each | Current geometry |
| Reference gap | 30 mm | Calculation point |
| TX / RX self-inductance | About 2.2963 µH each | Wheeler estimates |
| Mutual inductance | About 0.327653 µH | Filament model |
| Coupling coefficient | About 0.142686 | Preliminary derived estimate |

## Proposed transmitter control chain

1. NE555 astable creates a clock.
2. Divide-by-two toggle stage creates two opposite-phase 50% timing references.
3. Separate interlock logic inserts dead time and provides a hardware disable.
4. Two half-bridge gate drivers drive four N-channel MOSFETs.
5. The bridge applies alternating polarity across the primary resonant network.

The NE555 is a clock source only, not a MOSFET gate driver.

## Protection requirements

- Input fuse and current-limited bench supply during development.
- DC-link bulk and ceramic bypass capacitors close to the bridge.
- Gate-source pull-down resistors and suitable gate resistors.
- Hardware shutdown that defaults all MOSFETs OFF.
- Non-overlap logic to prevent shoot-through.
- Current sensing and overcurrent shutdown.
- Driver undervoltage handling.
- Thermal checks for MOSFETs, drivers, coils and capacitors.
- Oscilloscope validation before connecting the final resonant coil.

## Open decisions

Operating frequency; exact meaning/location of the 2 A current target; compensation topology; measured in-environment inductance; MOSFET; gate-driver supply; dead-time; current-sense threshold; soft-start; fault recovery; receiver rectifier/regulator.

No component values are final until these dependencies are resolved.
