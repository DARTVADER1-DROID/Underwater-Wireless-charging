# 12 V Full H-Bridge Inverter — Preliminary Design

**Status:** Architecture selected; component-level design remains open.

## 1. Required bridge behaviour

Four switches form two half-bridge legs. Q1/Q2 form leg A; Q3/Q4 form leg B. The TX resonant branch connects between midpoints A and B.

| State | Q1 | Q2 | Q3 | Q4 | V(A)-V(B) |
|---|---|---|---|---|---:|
| Positive polarity | ON | OFF | OFF | ON | Approximately +12 V |
| Negative polarity | OFF | ON | ON | OFF | Approximately −12 V |
| Dead time | OFF | OFF | OFF | OFF | Set by resonant current and diode paths |

The two diagonal pairs alternate. Never turn on Q1 and Q2 together, or Q3 and Q4 together: either condition shorts the DC bus through one leg (shoot-through).

An ideal bipolar square wave between +12 V and −12 V has 24 V peak-to-peak and 12 V RMS. This describes bridge output voltage before losses and before the resonant network; it does not guarantee 24 W real power.

## 2. Functional topology

See [H-bridge diagram](../diagrams/h-bridge-power-stage.mmd). It is a topology-level drawing, not a production schematic.

## 3. Gate-driver architecture

A practical all-N-channel implementation can use two half-bridge gate-driver ICs:

- Driver A controls Q1 high-side and Q2 low-side.
- Driver B controls Q3 high-side and Q4 low-side.

**Candidate for evaluation: Texas Instruments UCC27211A.**

- [Official product page](https://www.ti.com/product/UCC27211A)
- [Official datasheet](https://www.ti.com/lit/ds/symlink/ucc27211a.pdf)

Datasheet screening facts: one high-side and one low-side N-channel MOSFET per driver; VDD operating range 8–17 V; independent high/low inputs; integrated bootstrap diode; high/low undervoltage lockout; 3.7 A source / 4.5 A sink peak output capability.

Two drivers are required for a four-switch bridge if this architecture is retained.

**Important:** UCC27211A independent inputs do not themselves create complementary signals or dead time. External control logic must guarantee non-overlap. Verify exact package pinout, bootstrap capacitor, driver bypassing, absolute maximum ratings and MOSFET gate-charge compatibility before schematic capture.

## 4. Control and dead-time

The controller must generate four gate commands:

- Positive polarity: Q1 + Q4 ON.
- Negative polarity: Q2 + Q3 ON.
- Between states: all four commanded OFF for a designed non-overlap interval.

Sequence: turn the active pair OFF, wait the calculated dead time, then turn the opposite diagonal pair ON. Dead time must be derived from MOSFET turn-off behaviour, driver propagation delays, gate resistors, temperature and measured switching waveforms. Do not insert an arbitrary number.

See [bridge switching sequence](../diagrams/h-bridge-switching-timing.mmd).

## 5. NE555 relationship

Proposed chain: NE555 clock → divide-by-two toggle flip-flop → dead-time/interlock logic → two half-bridge drivers → four MOSFET gates.

A divide-by-two stage creates opposite-phase 50% references but does not insert dead time.

If divided by two, NE555 frequency is twice the bridge frequency. TI recommends the standard NE555 astable connection at 100 kHz or below to reduce distortion. This proposed architecture therefore limits the bridge frequency to about 50 kHz or below. If the required bridge frequency is higher, use a different clock/controller architecture or a suitable CMOS timer and check its datasheet.

## 6. DC-link and protection

The detailed schematic must include input fuse, local low-ESR bulk and ceramic capacitors, short commutation loops, gate pull-downs, gate resistors, gate clamps if needed, snubber/clamp selected from measured ringing, current sensing, fast shutdown, undervoltage handling and thermal provisions.

Do not connect the coil until gate and switch-node waveforms have been inspected with an oscilloscope and appropriate probing.

## 7. Sizing still required

No MOSFET, gate resistor, snubber or dead-time value is selected. Required inputs include operating frequency, peak and RMS tank current, MOSFET gate charge, allowed losses, bus transients, thermal path and measured turn-off behaviour. Resonant circulating current may differ substantially from DC input current.

## 8. Verification sequence

1. Simulate logic and bridge in LTspice.
2. Add realistic MOSFET models and driver delays.
3. Verify all gate signals for overlap.
4. Check switching-node overshoot and ringing.
5. Check peak/RMS current and losses.
6. Test initially with a controlled non-inductive load, not the final coil.
7. Validate thermal performance before sustained 24 W operation.

## 9. References

- TI, UCC27211A datasheet: https://www.ti.com/lit/ds/symlink/ucc27211a.pdf
- TI, UCC27211A product page: https://www.ti.com/product/UCC27211A
- TI, NE555 datasheet: https://www.ti.com/lit/ds/symlink/ne555.pdf
