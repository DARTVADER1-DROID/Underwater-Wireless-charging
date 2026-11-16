# Formula provenance and applicability

This note identifies the source and correct use of the equations in the current TX/RX coil calculation.

## 1. Wheeler single-layer spiral self-inductance

**Primary source:** H. A. Wheeler, “Simple Inductance Formulas for Radio Coils,” *Proceedings of the IRE*, Vol. 16, No. 10, October 1928, equation (3), pp. 1399–1400.

Source scan:  
https://physlab-wiki.com/_media/phylabs/lab_courses/phys-120_130-wiki-home/winter-experiments/simple_inductance_formulas_for_radio_coils.pdf

For a single-layer spiral (or a short single-layer helical coil), Wheeler gives:

\[
L(\mu H)=\frac{a^2N^2}{8a+11c}
\]

- \(a\): mean winding radius, inches.
- \(c\): radial winding width, inches.
- \(N\): number of turns.
- \(L\): microhenries.

Wheeler states the formula is correct to within about 5% for \(c>0.2a\). In the same paper, he cautions that accuracy may be worse with too few turns, excessive turn spacing, skin effect or distributed capacitance. Therefore, the 5% statement is not a blanket ±5% guarantee for any coil satisfying only the width inequality.

**Project use:** preliminary self-inductance estimate for the 7-turn, 70 mm OD / 20 mm opening spiral. The result is not a measurement and needs field-solver or LCR verification.

## 2. Neumann integral and Maxwell's coaxial circular-loop equation

The general Neumann integral for two closed current paths is:

\[
M=\frac{\mu_0}{4\pi}
\oint_{C_1}\oint_{C_2}
\frac{d\boldsymbol{\ell}_1\cdot d\boldsymbol{\ell}_2}{R}
\]

where \(R\) is the distance between differential path elements. This is the general magnetostatic mutual-inductance formulation for filamentary closed circuits in a linear homogeneous medium.

For two coaxial circular filament loops, evaluating the integral gives Maxwell's complete-elliptic-integral expression. Rosa and Cohen reproduce and discuss it in their Bureau of Standards publications:

- 1906 report, p. 360: https://digital.library.unt.edu/ark:/67531/metadc66517/m1/2/
- 1908 NBS Bulletin, formulae 1–3, pp. 6–7: https://nistdigitalarchives.contentdm.oclc.org/digital/api/collection/p16009coll6/id/15319/download

In SI units:

\[
M_{ij}=\mu_0\sqrt{a_i b_j}
\left[
\left(\frac{2}{q_{ij}}-q_{ij}\right)K(q_{ij}^2)
-\frac{2}{q_{ij}}E(q_{ij}^2)
\right]
\]

\[
q_{ij}=\frac{2\sqrt{a_i b_j}}
{\sqrt{(a_i+b_j)^2+h^2}}
\]

- \(a_i,b_j,h\) must be in metres.
- \(\mu_0=4\pi\times10^{-7}\ \mathrm{H/m}\).
- \(K(m)\), \(E(m)\) are complete elliptic integrals with parameter \(m=q^2\).
- The output is henries.

For multi-turn coils modelled as separate circular filaments:

\[
M_{\mathrm{coil}}=\sum_i\sum_j M_{ij}
\]

This pairwise summation assumes thin filament paths, coaxial circular turns and a homogeneous free-space medium in the current calculation. Finite conductor cross-section, ferrite, conductive seawater and nearby structures are not included.

## 3. Coupling coefficient

For two coupled inductors:

\[
k=\frac{M}{\sqrt{L_1L_2}}
\]

- \(M\): mutual inductance.
- \(L_1,L_2\): self-inductances.
- \(k\): dimensionless signed coupling coefficient; for the aligned same-polarity convention, the magnitude is between 0 and 1.

This equation defines magnetic coupling; it is not a power-transfer efficiency formula. For an ideal passive two-coil inductance matrix:

\[
L_1L_2-M^2\geq0
\]

or equivalently \(|k|\leq1\).

## 4. Experimental mutual-inductance check

For two coils measured in series:

\[
M=\frac{L_{\mathrm{aiding}}-L_{\mathrm{opposing}}}{4}
\]

This assumes the aiding and opposing measurements use the same coil connections except for the polarity reversal, and the meter is measuring the same frequency-dependent inductance model. Then calculate \(k=M/\sqrt{L_1L_2}\) using self-inductances measured at the same frequency and configuration.

## 5. Formula not yet selected for this design

The resonant capacitor formula \(C=1/(\omega_0^2L)\) applies to a chosen ideal series LC resonant branch. It should not be used to select components until the operating frequency, actual in-environment inductance, and compensation topology are decided. The Chen paper's series-series equations are documented separately in [chen-2024-paper-equations.md](chen-2024-paper-equations.md).