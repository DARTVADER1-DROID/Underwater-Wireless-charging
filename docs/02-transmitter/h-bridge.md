# Full H-Bridge Inverter

## Function

The four-switch full bridge converts the nominal 12 V battery DC bus into a bipolar square-wave voltage across the TX resonant branch.

## Switching states

Q1/Q2 form leg A. Q3/Q4 form leg B. The resonant TX branch is connected between switch nodes A and B.

| State | Q1 | Q2 | Q3 | Q4 | Ideal V(A) − V(B) |
|---|---|---|---|---|---:|
| Positive polarity | ON | OFF | OFF | ON | +VDC |
| Negative polarity | OFF | ON | ON | OFF | −VDC |
| Dead time | OFF | OFF | OFF | OFF | Determined by resonant current and diode paths |

For an ideal 12 V DC bus, the differential output alternates between +12 V and −12 V. This is a 24 V peak-to-peak bipolar square wave, with 12 V RMS for an ideal symmetrical waveform.

Never command Q1 and Q2 ON together, or Q3 and Q4 ON together. Either condition shorts the DC bus through one bridge leg (shoot-through).

## Driver architecture

The intended control chain is:

NE555 timing reference → switching logic / interlock / dead-time generation → two half-bridge gate drivers → four MOSFET gates.

A single NE555 output cannot safely serve as four independent gate signals. The high-side gate drivers must generate gate voltage relative to each switching MOSFET source. Gate-source pull-downs, suitable gate resistors and a hardware all-gates-OFF fault state are required.

A half-bridge driver such as TI UCC27211A may be evaluated as a candidate for each bridge leg; it is not yet a locked component choice. Product information: https://www.ti.com/product/UCC27211A. Datasheet: https://www.ti.com/lit/ds/symlink/ucc27211a.pdf.

## Frequency

The 30 kHz target applies to the bridge differential waveform / resonant link unless later clarified. If the chosen logic divides a clock by two, the NE555 clock must be twice the desired bridge frequency. Verify the frequency on an oscilloscope at both the bridge output and coil current.

## Battery and protection

A suitable 12 V lead-acid battery can supply a 2 A load; this is not a demanding current for many battery sizes. That alone does not determine runtime or battery capacity. Battery current rises above 2 A if 24 W is required at the receiver because the system has losses.

Use a fuse close to battery positive, current-limited bench supply during development, local DC-link bypassing, short switching loops, overcurrent protection and thermal checks. Size the fuse, wiring, capacitors and MOSFETs only after peak and RMS current and transient voltage have been established.

## Validation sequence

1. Simulate control logic and bridge in LTspice.
2. Verify complementary signals and dead time at both bridge legs.
3. Add selected gate-driver and MOSFET models.
4. Check switching-node ringing, MOSFET voltage stress and gate-source voltage.
5. Calculate and measure peak and RMS resonant current.
6. Test from a current-limited supply with a dummy load before connecting the coil.
7. Measure temperature rise and verify protection before sustained operation.

