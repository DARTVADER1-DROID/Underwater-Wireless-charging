# NE555 Timer — Oscillator and H-Bridge Clock Source

**Status:** Candidate clock-source stage. Timing values are intentionally open until the bridge operating frequency is selected.

## 1. Role

The NE555 generates a timing clock for the control logic. It must not directly drive the four H-bridge MOSFET gates.

Proposed chain:

NE555 astable → divide-by-two toggle flip-flop → dead-time/interlock logic → two half-bridge gate drivers.

The toggle stage provides opposite-phase 50% references. It does not create dead time; interlock logic remains mandatory.

## 2. Common 8-pin NE555 pinout

| Pin | Name | Astable connection |
|---:|---|---|
| 1 | GND | Control ground |
| 2 | TRIG | Join to pin 6 and timing-capacitor node |
| 3 | OUT | Clock to logic input only |
| 4 | RESET | Hold high for normal oscillation; pull low to stop |
| 5 | CONT | Optional 10 nF bypass to ground |
| 6 | THRES | Join to pin 2 and timing-capacitor node |
| 7 | DISCH | RA/RB junction |
| 8 | VCC | Supply; NE555 recommended range is 4.5–16 V |

At a 12 V supply, the NE555 is within its recommended supply range. Decouple the IC locally. Check the exact manufacturer and package suffix of the purchased timer.

## 3. Astable network connections

- RA from VCC to the RA/RB junction.
- RB from the RA/RB junction to the timing-capacitor node.
- Pin 7 to the RA/RB junction.
- Pins 2 and 6 joined at the timing-capacitor node.
- Timing capacitor C from that node to ground.
- Pin 4 RESET held high.
- Pin 5 CONT optionally bypassed with 10 nF.
- Pin 3 provides the oscillator output.

See [NE555 timing diagram](../diagrams/ne555-timing.mmd).

## 4. Readable timing equations

The capacitor charges through RA plus RB and discharges through RB.

High time: **t-high = 0.693 × (RA + RB) × C**

Low time: **t-low = 0.693 × RB × C**

Period: **T = 0.693 × (RA + 2 × RB) × C**

Frequency: **f-555 = 1 / T = 1.44 / [(RA + 2 × RB) × C]**

High-duty ratio: **D-high = (RA + RB) / (RA + 2 × RB)**

Low-duty ratio: **D-low = RB / (RA + 2 × RB)**

Use ohms for resistors and farads for capacitance. Time is seconds; frequency is hertz.

The standard astable output is not 50% duty because RA is positive. Do not use its raw output as two complementary bridge gate commands.

## 5. Divide-by-two relationship

If the NE555 drives a toggle flip-flop:

**f-bridge = f-555 / 2**

Therefore:

**f-555 = 2 × f-bridge**

TI's March 2026 NE555 datasheet recommends 100 kHz or below for the standard astable configuration to reduce distortion. With the divide-by-two chain, this suggests a bridge frequency ceiling of approximately 50 kHz. This is a limitation of this proposed clock chain, not of the H-bridge itself.

If the selected resonant operating frequency is above 50 kHz, use another oscillator/controller architecture or an appropriate CMOS timer. TI notes TLC555 as an alternative for higher-frequency operation; check its separate supply and output specifications before using it.

## 6. Why no RA, RB or C values are specified

The project operating frequency is not yet finalized. Once selected:

1. Set f-555 to twice the desired bridge frequency for the divide-by-two design.
2. Select a practical timing capacitor with suitable tolerance and temperature coefficient.
3. Calculate RA + 2RB = 1.44 / (f-555 × C).
4. Choose RA and RB within datasheet and practical limits.
5. Recalculate frequency and duty using actual standard values.
6. Check frequency drift and jitter over supply and temperature.
7. Measure the clock before connecting the logic stage.

No arbitrary component values are inserted merely to make the schematic appear complete.

## 7. Output is not a gate driver

The timer output is a logic timing signal. It is not a substitute for high-side/low-side MOSFET gate drivers. High-side gate drive must be referenced to the moving MOSFET source node.

## 8. Source

Texas Instruments, NA555 / NE555 / SA555 / SE555 Precision Timers, datasheet SLFS022K, revised March 2026: https://www.ti.com/lit/ds/symlink/ne555.pdf

Relevant sections: pin configuration (section 4), recommended supply range (section 5.3), astable circuit and pin connections (section 6.3.2), and timing equations (section 6.3.2).
