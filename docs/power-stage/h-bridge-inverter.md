# 12 V Full H-Bridge Inverter

**Status:** Topology selected; device-level design pending.

## 1. Purpose

Convert 12 V lead-acid battery DC into a bipolar square-wave voltage for the TX resonant capacitor and TX coil.

## 2. Four-switch bridge

Q1/Q2 form left leg A. Q3/Q4 form right leg B. The TX resonant branch connects between switch nodes A and B.

| State | Q1 | Q2 | Q3 | Q4 | Ideal V(A)-V(B) |
|---|---|---|---|---|---:|
| Positive | ON | OFF | OFF | ON | +Vbattery |
| Negative | OFF | ON | ON | OFF | −Vbattery |
| Dead time | OFF | OFF | OFF | OFF | Set by current/freewheel paths |

The diagonal pairs alternate. Never turn on Q1 and Q2 together, or Q3 and Q4 together: this causes DC-bus shoot-through.

At a 12 V bus, ideal bridge differential output switches between +12 V and −12 V. This is 24 V peak-to-peak and 12 V RMS for a symmetrical bipolar waveform.

## 3. Control and gate drive

The NE555 produces one timing waveform. It is not a complete four-channel bridge controller and must not directly drive all four MOSFET gates.

The bridge needs complementary commands for each leg, non-overlap dead time, high-side gate drive referenced to each high-side MOSFET source, and hardware disable that forces all gates OFF on reset/fault. A practical architecture uses logic/control circuitry followed by two half-bridge gate drivers, one per leg.

## 4. Frequency definition

The target resonant/coil excitation is 30 kHz. Measure this at H-bridge differential output and coil current.

If a toggle flip-flop divides a timer clock by two, the timer must run at 60 kHz to produce a 30 kHz bridge cycle. A 30 kHz timer clock divided by two produces 15 kHz bridge operation. Do not confuse timer clock frequency with bridge output frequency.

TI recommends standard NE555 astable operation at 100 kHz or below to reduce distortion; a 60 kHz clock is within that guidance. Datasheet: https://www.ti.com/lit/ds/symlink/ne555.pdf.

## 5. Candidate gate driver

Candidate for evaluation: TI UCC27211A, a half-bridge driver for one high-side and one low-side N-channel MOSFET. Product: https://www.ti.com/product/UCC27211A. Datasheet: https://www.ti.com/lit/ds/symlink/ucc27211a.pdf. Two devices would serve two bridge legs. This remains a candidate, not a finalized BOM selection. Confirm supply range, logic thresholds, input behaviour, bootstrap circuit, gate current and package ratings from the datasheet.

## 6. Battery-side input

A lead-acid battery can supply 2 A in many practical sizes; capacity and runtime depend on Ah rating, condition, discharge rate and system losses. Do not size fuse or wiring from nominal 2 A alone. Determine maximum DC input current, including startup and fault current.

## 7. Protection and validation

Fuse close to battery positive; use current-limited bench supply during development; place DC-link bulk and ceramic capacitors close to bridge; minimize switching-loop inductance; add gate-source pull-downs, suitable gate resistors, overcurrent shutdown and thermal protection. Select snubbers from measured ringing.

Simulate logic and bridge in LTspice, verify non-overlap, add MOSFET/driver models, check ringing and device stress, then test from a current-limited supply and dummy load before connecting the coil.
