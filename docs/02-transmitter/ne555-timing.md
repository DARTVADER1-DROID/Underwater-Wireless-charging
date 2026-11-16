# NE555 Timing Source

## Role

The NE555 is intended to generate the timing reference for the transmitter control logic. It does **not** directly drive all four MOSFET gates.

## Standard astable equations

For the conventional two-resistor astable circuit:

- High interval: tH = 0.693 × (RA + RB) × C
- Low interval: tL = 0.693 × RB × C
- Period: T = 0.693 × (RA + 2RB) × C
- Frequency: f = 1.44 ÷ [(RA + 2RB) × C]
- High duty ratio: Dhigh = (RA + RB) ÷ (RA + 2RB)

Use ohms, farads, seconds and hertz. The conventional astable output is not inherently 50% duty cycle.

## Frequency planning

The design target is 30 kHz at the H-bridge differential output / resonant link.

If a toggle flip-flop divides the NE555 clock by two, the NE555 must run at 60 kHz to obtain a 30 kHz bridge waveform. A 30 kHz timer clock divided by two would give a 15 kHz bridge waveform. Other logic arrangements are possible, but the timer frequency and bridge frequency must be explicitly distinguished.

Do not calculate RA, RB and C until the switching-logic architecture is chosen. Then select a practical capacitor, calculate the required resistor sum, choose standard resistor values and recalculate the resulting frequency and duty cycle.

## Common 8-pin NE555 astable connections

| Pin | Name | Connection |
|---:|---|---|
| 1 | GND | Circuit ground |
| 2 | TRIG | Joined to pin 6 and timing-capacitor node |
| 3 | OUT | Timing reference to logic input |
| 4 | RESET | Held high for normal operation; pulled low to reset |
| 5 | CONT | Follow the selected manufacturer's bypass guidance |
| 6 | THRES | Joined to pin 2 and timing-capacitor node |
| 7 | DISCH | RA/RB junction |
| 8 | VCC | Timer supply within device ratings |

Astable network: RA from VCC to pin-7 junction; RB from pin-7 junction to pins 2/6; timing capacitor from pins 2/6 to ground. Decouple the timer supply locally. Confirm the exact manufacturer's pinout and recommended component values.

## Gate-drive interface

The NE555 output feeds timing/control logic. That logic must produce complementary bridge states and guaranteed dead time. Two half-bridge drivers can then drive the two bridge legs. Verify input polarity, UVLO, bootstrap operation, propagation delays, peak gate current and safe shutdown behaviour from the selected datasheets.

Reference: Texas Instruments, NA555/NE555/SA555/SE555 timer datasheet: https://www.ti.com/lit/ds/symlink/ne555.pdf.
