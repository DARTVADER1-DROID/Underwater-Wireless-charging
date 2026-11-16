# Equations reported by Chen et al. (2024) underwater WPT paper

**Source:** Xiaotong Chen, Kun Li, Qing Liu and Zheng Gong, “Design of tile shaped coil structure for wireless power transmission for underwater vehicle,” *Measurement and Control*, Vol. 58, Issue 1, pp. 60–67. First published online 4 May 2024. DOI: https://doi.org/10.1177/00202940241226590

SAGE article page: https://journals.sagepub.com/doi/10.1177/00202940241226590

SAGE identifies this article as CC BY 4.0. This note attributes and summarizes the equations; consult the paper for the original notation, assumptions and full derivation.

## 1. Series-series resonance condition — paper equation (1)

The paper uses series compensation on both transmitter and receiver sides:

\[
C_1=\frac{1}{\omega_d^2L_P}
\qquad
C_2=\frac{1}{\omega_d^2L_S}
\]

where \(L_P\) and \(L_S\) are the primary and secondary self-inductances and \(\omega_d\) is the selected resonant angular frequency.

Equivalent frequency form:

\[
\omega_d=2\pi f_d
\]

\[
C=\frac{1}{(2\pi f_d)^2L}
\]

**Applicability to our design:** not yet applied. Our operating frequency and compensation topology have not been selected, and our air-core inductance estimates need verification in the final coil environment.

## 2. Equivalent impedances — paper equation (2)

The paper writes the primary and secondary resonant impedances as:

\[
Z_1=R_1+j\omega_dL_P+\frac{1}{j\omega_dC_1}
\]

\[
Z_2=R_2+R_0+j\omega_dL_S+\frac{1}{j\omega_dC_2}
\]

The symbols represent the coil resistances, load and series LC branch impedances in the paper's model. This is a circuit-model equation, not a coil-geometry equation.

## 3. Coupled-loop circuit equations — paper equation (3)

The paper uses the mutual-inductance term in the primary/secondary equations:

\[
U_1=Z_1I_1-j\omega_dMI_2
\]

\[
Z_2I_2=j\omega_dMI_1
\]

The sign of the mutual term depends on the chosen dot convention and reference directions. Use a consistent polarity convention in simulation.

## 4. Important source distinction

The paper's equations are reported here as research-reference equations. They do not establish that our project must use series-series compensation. The compensation network remains undecided.

The paper's reported coil and operating parameters, including its tile-shaped geometry and 30 kHz seawater simulation, are summarized separately in [the paper note](../papers/chen-2024-tile-shaped-underwater-wpt.md).