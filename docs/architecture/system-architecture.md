# UWLPT System Architecture

**Current target:** 12 V lead-acid battery input; nominal 24 W input-stage target; 30 kHz-class resonant link; resistive receiving-side load.

## Energy path

1. 12 V lead-acid battery supplies DC to the transmitter.
2. NE555 timer generates a 30 kHz timing signal (the exact frequency node must be specified: timer output versus H-bridge output).
3. Gate-control logic and suitable high/low-side gate drivers produce safe MOSFET gate signals with dead time.
4. Four-switch H-bridge converts DC into a bipolar square-wave voltage.
5. TX resonant capacitor and TX coil form the primary compensated resonant circuit.
6. TX and RX coils transfer energy magnetically across the water gap.
7. RX resonant capacitor and RX coil form the secondary compensated resonant circuit.
8. A high-frequency bridge rectifier converts receiver AC to pulsating DC.
9. A resistive load is connected to the receiving-side DC output.

## Current inputs and coil baseline

| Parameter | Value | Status |
|---|---:|---|
| Battery nominal voltage | 12 V | Requirement |
| Battery chemistry | Lead-acid | Requirement |
| Input power | 24 W nominal if 12 V × 2 A is the intended rating | Needs confirmation |
| Operating frequency | 30 kHz | Target from research context; confirm at coil |
| H-bridge | Full bridge | Selected |
| TX/RX coil OD | 70 mm each | Current design |
| Turns | 7 each | Current design |
| Reference coil separation | 30 mm | Calculation point |
| TX/RX self-inductance | 2.2963 µH each | Preliminary Wheeler estimates |
| Mutual inductance | 0.327653 µH | Preliminary filament model |
| Coupling coefficient | 0.142686 | Preliminary derived estimate |
| Receiver load | Resistive | Requirement |

## Important power definition

12 V × 2 A = 24 W is nominal DC input power, not guaranteed load power. If 24 W is required at the receiver, input power must be greater than 24 W by the reciprocal of total end-to-end efficiency. Battery current must be calculated using loaded battery voltage and measured/estimated efficiency.

## Control and gate-drive boundary

The NE555 is the oscillator/timing source. Do not connect its single output directly to all four bridge MOSFET gates. The H-bridge requires two-leg complementary switching, high-side gate drive and non-overlap dead time.

## Receiver rectifier

Select a rectifier suitable for actual secondary frequency, RMS current, peak inverse voltage and thermal dissipation. At 30 kHz, ordinary mains-frequency rectifiers may have unsuitable reverse-recovery behaviour. Evaluate fast-recovery or Schottky devices against actual voltage/current requirements. Select output capacitance after defining ripple and load requirements.

## Open decisions

- Is 24 W the battery input rating or required receiver load power?
- Does 30 kHz refer to NE555 pin 3 or H-bridge/coil excitation?
- Exact NE555 gate-control logic and dead-time implementation.
- MOSFET and gate-driver part numbers.
- Compensation arrangement and measured coil parameters.
- Battery Ah capacity, condition and intended runtime.
- Rectifier part and output filtering.
- Resistive load voltage and power target.
