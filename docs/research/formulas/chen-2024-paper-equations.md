# Equations from Chen et al. (2024) Underwater WPT Paper

**Source:** Xiaotong Chen, Kun Li, Qing Liu and Zheng Gong, “Design of tile shaped coil structure for wireless power transmission for underwater vehicle,” *Measurement and Control*, Volume 58, Issue 1, pages 60–67. First published online 4 May 2024. DOI: https://doi.org/10.1177/00202940241226590

Publisher page: https://journals.sagepub.com/doi/10.1177/00202940241226590

This note summarizes the paper's equations in readable text. Consult the original article for its complete notation, derivations and assumptions.

## 1. Series-series resonance condition (paper equation 1)

The paper uses a series compensation capacitor on both transmitter and receiver.

For the transmitter:

**C1 = 1 / (ωd² × LP)**

For the receiver:

**C2 = 1 / (ωd² × LS)**

Definitions:

- C1 and C2 = transmitter and receiver compensation capacitance, in farads.
- LP and LS = primary and secondary coil self-inductance, in henries.
- ωd = selected resonant angular frequency, in radians per second.

Angular frequency is related to ordinary frequency by:

**ωd = 2π × fd**.

Therefore, the equivalent frequency form is:

**C = 1 / [(2π × fd)² × L]**.

**Applicability to our prototype:** not applied yet. Our operating frequency, measured coil inductances and compensation topology are not finalized.

## 2. Equivalent circuit impedances (paper equation 2)

The primary-side impedance is written as:

**Z1 = R1 + jωdLP + 1 / (jωdC1)**.

The secondary-side impedance is written as:

**Z2 = R2 + R0 + jωdLS + 1 / (jωdC2)**.

Definitions:

- R1 and R2 = primary and secondary coil resistances in the paper's model.
- R0 = load resistance.
- j = imaginary unit, square root of −1.
- ωd = angular operating frequency.
- LP and LS = coil self-inductances.
- C1 and C2 = series compensation capacitors.

These are circuit impedance equations, not coil geometry formulas.

## 3. Coupled-loop circuit equations (paper equation 3)

The paper includes mutual inductance in the primary and secondary circuit equations:

**U1 = Z1 × I1 − jωd × M × I2**

**Z2 × I2 = jωd × M × I1**

Definitions:

- U1 = primary input phasor voltage.
- I1 and I2 = primary and secondary current phasors.
- M = mutual inductance.
- Z1 and Z2 = equivalent impedances defined above.

The sign of the mutual term depends on the winding-dot convention and reference current directions. Keep the polarity convention consistent between schematic, simulation and hardware.

## 4. Research equation versus project design decision

These equations are reported from the paper as research reference. They do not prove that this prototype must use series-series compensation. The topology remains a design decision.

The paper's geometry, conductor, ferrite and performance data are documented separately in [the research-paper note](../papers/chen-2024-tile-shaped-underwater-wpt.md). Do not substitute those values for the present seven-turn circular coil calculations.
