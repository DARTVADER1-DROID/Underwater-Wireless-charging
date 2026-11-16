# TX/RX Coil Design — Geometry and Inductance Calculation

**Document status:** Preliminary analytical baseline  
**Calculation date:** 2026-11-16  
**Scope:** Wire dimensions, circular planar coil geometry, self-inductance, mutual inductance and coupling coefficient.

> **Important:** This document records a reproducible first-pass analytical model. It does not claim that the coils are optimized, that the calculated values are measured, or that the air-core model represents operation in saltwater.

## 1. System requirements and design assumptions

| Item | Value | Status / interpretation |
|---|---:|---|
| DC input | 12 V | User requirement |
| Target transferred power | 24 W | User requirement |
| TX inverter | Full H-bridge | Selected architecture |
| TX current target | 2 A AC | RMS definition and measurement point not yet specified |
| TX coil outer diameter | 70 mm | Provisional design dimension |
| RX coil outer diameter | 70 mm | Provisional design dimension |
| TX/RX inner opening | 20 mm | Assumed for this calculation |
| TX/RX turns | 7 | Selected for this calculation |
| Coil separation | 20–40 mm | Design range |
| Reference coil-plane separation | 30 mm | Calculation case |
| Medium | Artificial saltwater | Intended test medium |
| Target salinity | Approximately 35 g/kg | Test target; conductivity must be measured |
| Wire construction | Solid, single-core copper | Prototype assumption |
| Wire insulation | PVC | Datasheet reference; not immersion-rated |

No operating frequency or compensation topology is selected. The 2 A AC target is not used to calculate geometric inductance.

## 2. Wire reference and manufacturer data

Reference product: **Nuhas Oman H05V-U, 1.0 mm², Class 1 solid copper, PVC insulated**.

Manufacturer catalogue:  
https://www.nuhasoman.com/wp-content/uploads/2023/07/Building-Wires-Flexible-Cables-1.pdf

The H05V-U table specifies:

| Datasheet item | Manufacturer value |
|---|---:|
| Nominal copper cross-section | 1.0 mm² |
| Conductor class | 1 (solid) |
| Nominal PVC insulation thickness | 0.6 mm |
| Nominal overall diameter | 2.7 mm |
| Maximum operating temperature | 70 °C |
| H05V-U rated voltage | 300/500 V |

The catalogue describes the cable application as dry rooms, apparatus, switch/distribution boards and fixed installation. It is **not a direct-immersion underwater cable specification**. A waterproof encapsulation or sealed coil enclosure is required for underwater testing, and compatibility of the insulation/encapsulant must be checked.

### 2.1 Copper diameter from nominal conductor area

The manufacturer gives conductor area, not a bare conductor diameter. For a nominal circular 1.0 mm² copper section:

\[
A=\frac{\pi d_{\mathrm{Cu}}^2}{4}
\]

\[
d_{\mathrm{Cu}}=\sqrt{\frac{4A}{\pi}}
=\sqrt{\frac{4(1.0)}{\pi}}
=1.12838\ \mathrm{mm}
\]

This is the equivalent diameter calculated from the nominal area. It is not a separate manufacturer diameter tolerance.

### 2.2 Which diameter is used for winding geometry?

Use the **2.7 mm nominal overall insulated diameter**, because adjacent insulated wires occupy physical winding space. Do not use the 1.128 mm copper diameter to calculate the winding pitch.

## 3. Geometric derivation

### 3.1 Boundary dimensions

- Coil outer boundary diameter: \(D_o=70\ \mathrm{mm}\)
- Inner clear opening diameter: \(D_i=20\ \mathrm{mm}\)
- Insulated wire diameter: \(d_w=2.7\ \mathrm{mm}\)
- Number of turns: \(N=7\)

Wire radius:

\[
r_w=\frac{d_w}{2}=\frac{2.7}{2}=1.35\ \mathrm{mm}
\]

### 3.2 Outermost wire centreline

The outermost wire centreline is one wire radius inside the outside boundary on each side of the diameter:

\[
D_{o,CL}=D_o-2r_w=70-2(1.35)
\]

\[
\boxed{D_{o,CL}=67.3\ \mathrm{mm}}
\]

### 3.3 Innermost wire centreline

The innermost wire centreline is one wire radius outside the opening boundary on each side:

\[
D_{i,CL}=D_i+2r_w=20+2(1.35)
\]

\[
\boxed{D_{i,CL}=22.7\ \mathrm{mm}}
\]

### 3.4 Centreline radii and radial span

\[
R_o=\frac{67.3}{2}=33.65\ \mathrm{mm}
\]

\[
R_i=\frac{22.7}{2}=11.35\ \mathrm{mm}
\]

The radial centreline span is:

\[
c=R_o-R_i=33.65-11.35
\]

\[
\boxed{c=22.3\ \mathrm{mm}}
\]

### 3.5 Turn pitch and clear spacing

Seven turns create six centreline intervals:

\[
p=\frac{R_o-R_i}{N-1}
=\frac{22.3}{6}
\]

\[
\boxed{p=3.7166667\ \mathrm{mm}}
\]

Clear insulation-to-insulation spacing:

\[
s=p-d_w=3.7166667-2.7
\]

\[
\boxed{s=1.0166667\ \mathrm{mm}}
\]

This replaces the earlier trial value of 0.5 mm. A 0.5 mm clear gap cannot coexist with all the currently specified boundary dimensions and seven equally spaced turns.

### 3.6 Individual turn centreline radii

For turn index \(i=1,\ldots,7\), ordered outermost to innermost:

\[
R_i=R_o-(i-1)p
\]

| Turn | Centreline radius (mm) |
|---:|---:|
| 1 (outermost) | 33.650000 |
| 2 | 29.933333 |
| 3 | 26.216667 |
| 4 | 22.500000 |
| 5 | 18.783333 |
| 6 | 15.066667 |
| 7 (innermost) | 11.350000 |

These radii define the idealised filament paths used for the mutual-inductance calculation.

### 3.7 Mean radius used by Wheeler

Mean diameter of the innermost and outermost turn centrelines:

\[
D_{\mathrm{avg}}=\frac{D_{o,CL}+D_{i,CL}}{2}
=\frac{67.3+22.7}{2}=45.0\ \mathrm{mm}
\]

Mean radius:

\[
a=\frac{D_{\mathrm{avg}}}{2}
=\boxed{22.5\ \mathrm{mm}}
\]

Radial width for Wheeler's spiral formula:

\[
c=\boxed{22.3\ \mathrm{mm}}
\]

The variable \(c\) here means radial winding width, not conductor cross-sectional area.

## 4. Self-inductance estimate — Wheeler single-layer spiral formula

### 4.1 Source and formula

Harold A. Wheeler, “Simple Inductance Formulas for Radio Coils,” *Proceedings of the IRE*, Vol. 16, No. 10, October 1928, pp. 1398–1400.

Original paper copy:  
https://physlab-wiki.com/_media/phylabs/lab_courses/phys-120_130-wiki-home/winter-experiments/simple_inductance_formulas_for_radio_coils.pdf

Wheeler's equation (3) for a single-layer spiral is:

\[
\boxed{L(\mu H)=\frac{a^2N^2}{8a+11c}}
\]

For this equation, \(a\) and \(c\) are in inches. \(a\) is the mean radius and \(c\) is the radial width of the winding. \(N\) is the turn count.

Wheeler states an approximately 5% accuracy condition for \(c>0.2a\), but also warns that accuracy can be worse when there are too few turns, turn spacing is too large, skin effect is significant, or distributed capacitance matters. Therefore, the stated 5% is **not a guaranteed error bound for this seven-turn coil**.

### 4.2 Convert dimensions to inches

\[
a=\frac{22.5}{25.4}=0.8858267717\ \mathrm{in}
\]

\[
c=\frac{22.3}{25.4}=0.8779527559\ \mathrm{in}
\]

### 4.3 Check Wheeler's stated geometric condition

\[
0.2a=0.2(22.5)=4.5\ \mathrm{mm}
\]

\[
c=22.3\ \mathrm{mm}>4.5\ \mathrm{mm}
\]

The stated width condition is satisfied. This alone does not guarantee 5% accuracy because Wheeler lists additional limitations, including low turn count and excessive spacing.

### 4.4 Substitute values

\[
L=\frac{(0.8858267717)^2(7)^2}
{8(0.8858267717)+11(0.8779527559)}
\]

Numerator:

\[
a^2N^2=38.446\ \text{(approximately)}
\]

Denominator:

\[
8a+11c=16.744\ \text{(approximately)}
\]

\[
\boxed{L_{\mathrm{Wheeler}}=2.29631793\ \mu H}
\]

For identical TX and RX geometry:

\[
\boxed{L_{TX}=L_{RX}=2.29631793\ \mu H\quad\text{(estimate)}}
\]

This is an air-core analytical estimate. It is not a measured value.

## 5. Mutual inductance — Maxwell formula for coaxial circular filaments

### 5.1 Source and scope

The mutual-inductance expression for two coaxial circular filaments is Maxwell's elliptic-integral formula, documented by Edward B. Rosa and Louis Cohen in:

- E. B. Rosa and L. Cohen, *The Mutual Inductance of Two Circular Coaxial Coils of Rectangular Section*, Bulletin of the Bureau of Standards, 1906, section “Mutual Inductance of Two Coaxial Circles — Maxwell's Formula in Elliptic Integrals,” p. 360.
- E. B. Rosa and L. Cohen, *Formulae and Tables for the Calculation of Mutual and Self-Inductance*, Bulletin of the Bureau of Standards, Vol. 5, 1908, formulae section, pp. 6–7.

1906 scan:  
https://digital.library.unt.edu/ark:/67531/metadc66517/m1/2/

1908 NIST archive:  
https://nistdigitalarchives.contentdm.oclc.org/digital/api/collection/p16009coll6/id/15319/download

The equation is for two ideal circular filament loops with radii \(a_i\) and \(b_j\), coaxial and separated by axial distance \(h\). For SI units, use radii and distance in metres and \(\mu_0=4\pi\times10^{-7}\ \mathrm{H/m}\).

### 5.2 One turn-pair equation

Define the elliptic-integral modulus:

\[
q_{ij}=\frac{2\sqrt{a_i b_j}}
{\sqrt{(a_i+b_j)^2+h^2}}
\]

Let \(m=q_{ij}^2\). Let \(K(m)\) and \(E(m)\) denote complete elliptic integrals of the first and second kinds, respectively, using parameter \(m\).

Then:

\[
\boxed{
M_{ij}=\mu_0\sqrt{a_i b_j}
\left[
\left(\frac{2}{q_{ij}}-q_{ij}\right)K(q_{ij}^2)
-\frac{2}{q_{ij}}E(q_{ij}^2)
\right]
}
\]

The result is in henries.

### 5.3 Coil-to-coil sum

Each coil has seven turns. The total mutual inductance is the sum of the 49 turn-pair contributions:

\[
\boxed{M=\sum_{i=1}^{7}\sum_{j=1}^{7}M_{ij}}
\]

Assumptions for this calculation:

- TX and RX are coaxial and parallel.
- Both coils have identical turn radii listed in Section 3.6.
- Axial separation between coil planes is \(h=30\ \mathrm{mm}=0.030\ \mathrm{m}\).
- Air/free-space permeability is used.
- Each turn is approximated as a thin circular filament at the wire centreline.

### 5.4 Worked example: outer TX turn to outer RX turn

\[
a_1=b_1=33.65\ \mathrm{mm}=0.03365\ \mathrm{m}
\]

\[
h=0.030\ \mathrm{m}
\]

\[
q_{11}=
\sqrt{
\frac{4(0.03365)(0.03365)}
{(0.03365+0.03365)^2+(0.030)^2}
}
\]

\[
\boxed{q_{11}=0.9133633}
\]

\[
q_{11}^2=0.8342325
\]

Numerical complete elliptic-integral values:

\[
K(q_{11}^2)\approx2.3429815
\]

\[
E(q_{11}^2)\approx1.1547838
\]

Substitution into the turn-pair equation gives:

\[
M_{11}\approx1.95282019\times10^{-8}\ \mathrm{H}
\]

\[
\boxed{M_{11}=0.0195282019\ \mu H}
\]

### 5.5 All 49 turn-pair contributions

Rows are TX turns; columns are RX turns. Both are ordered outermost to innermost. Units are microhenries.

| TX \ RX | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.019528202 | 0.016812348 | 0.013839901 | 0.010794945 | 0.007869940 | 0.005240204 | 0.003048939 |
| 2 | 0.016812348 | 0.014741621 | 0.012356730 | 0.009801204 | 0.007250998 | 0.004886697 | 0.002869834 |
| 3 | 0.013839901 | 0.012356730 | 0.010555992 | 0.008530434 | 0.006419966 | 0.004390765 | 0.002608977 |
| 4 | 0.010794945 | 0.009801204 | 0.008530434 | 0.007028891 | 0.005390917 | 0.003750438 | 0.002260259 |
| 5 | 0.007869940 | 0.007250998 | 0.006419966 | 0.005390917 | 0.004216059 | 0.002988116 | 0.001830170 |
| 6 | 0.005240204 | 0.004886697 | 0.004390765 | 0.003750438 | 0.002988116 | 0.002157843 | 0.001344482 |
| 7 | 0.003048939 | 0.002869834 | 0.002608977 | 0.002260259 | 0.001830170 | 0.001344482 | 0.000851630 |

The matrix is symmetric, \(M_{ij}=M_{ji}\), as expected for reciprocal mutual inductance.

Row totals:

| TX row | Row sum (µH) |
|---:|---:|
| 1 | 0.07713448 |
| 2 | 0.06871943 |
| 3 | 0.05870276 |
| 4 | 0.04755709 |
| 5 | 0.03596616 |
| 6 | 0.02475855 |
| 7 | 0.01481429 |

Sum of all 49 contributions:

\[
\boxed{M=0.3276527625\ \mu H}
\]

This reproduces the numerical result from the accompanying Python model.

## 6. Coupling coefficient — derive and verify

### 6.1 Definition

For two coupled inductors:

\[
\boxed{k=\frac{M}{\sqrt{L_{TX}L_{RX}}}}
\]

For identical TX and RX self-inductance estimates:

\[
L_{TX}=L_{RX}=2.2963179303\ \mu H
\]

Therefore:

\[
\sqrt{L_{TX}L_{RX}}=2.2963179303\ \mu H
\]

Substitute the mutual-inductance result:

\[
k=\frac{0.3276527625}{2.2963179303}
\]

\[
\boxed{k=0.14268615\approx0.1427}
\]

### 6.2 Physical consistency checks

For passive coupled inductors, the magnitude of coupling must satisfy:

\[
0\leq |k|\leq1
\]

Our result:

\[
0<0.14268615<1
\]

The inductance matrix must also be positive semidefinite:

\[
L_{TX}L_{RX}-M^2\geq0
\]

Using the values above:

\[
(2.2963179303)^2-(0.3276527625)^2
\approx5.16571970\ \mu H^2>0
\]

Both mathematical checks pass.

**Approximation caveat:** self-inductance uses Wheeler's empirical finite-coil approximation, while mutual inductance uses a sum of ideal filament-loop interactions. Thus the calculated \(k\) is a useful first-pass estimate, not a fully self-consistent finite-conductor field solution. A field solver or measurement of the completed pair is required before treating it as final.

## 7. Reference-gap sensitivity

The same model can be evaluated at the ends of the requested gap range. These are ideal aligned air-core estimates, not seawater results.

| Coil-plane separation | Mutual inductance (µH) | Coupling coefficient (using the same Wheeler self-L) |
|---:|---:|---:|
| 20 mm | 0.5652 | 0.2462 |
| 30 mm | 0.3276528 | 0.142686 |
| 40 mm | 0.2012 | 0.0876 |

The 30 mm case is the current reference calculation.

## 8. Current calculation summary

| Quantity | Current result | Status |
|---|---:|---|
| Wire nominal copper area | 1.0 mm² | Datasheet |
| Wire nominal insulated diameter | 2.7 mm | Datasheet |
| TX/RX outer diameter | 70 mm | Provisional design assumption |
| TX/RX inner opening | 20 mm | Assumption used for calculation |
| TX/RX turns | 7 | Selected calculation baseline |
| Derived clear turn spacing | 1.0166667 mm | Geometry |
| TX/RX Wheeler self-inductance | 2.29631793 µH | Approximation |
| Reference axial separation | 30 mm | Provisional |
| Mutual inductance | 0.32765276 µH | Maxwell filament-pair sum |
| Coupling coefficient | 0.14268615 | Derived estimate |

## 9. What is not yet calculated or validated

- Actual self-inductance and AC resistance at the chosen operating frequency.
- Seawater-induced eddy-current loss and change in complex coil impedance.
- Measured mutual inductance and coupling under water.
- Lateral and angular misalignment sensitivity.
- Ferrite backing/shielding influence.
- Coil temperature rise and conductor suitability at the eventual frequency/current.
- Resonant capacitors, because frequency and compensation topology are not yet selected.
- Delivered DC power and overall efficiency.

The reference research paper reports a seawater conductivity of 4 S/m in its medium comparison. Our artificial saltwater conductivity must be measured at the actual test temperature; 35 g/kg salinity alone is not enough to define the electromagnetic model.

## 10. Verification procedure for fabricated coils

1. Measure each coil's self-inductance with an LCR meter at a recorded test frequency and test level.
2. Measure the coils separately in air, then in the intended sealed/immersed arrangement.
3. Measure series-aiding and series-opposing inductance with the coils in the intended alignment:
   \[
   M=\frac{L_{\mathrm{aiding}}-L_{\mathrm{opposing}}}{4}
   \]
4. Calculate:
   \[
   k=\frac{M}{\sqrt{L_{TX}L_{RX}}}
   \]
5. Record the coil-plane gap, lateral offset, angular alignment, water conductivity and temperature for every test.
6. Compare measured values with the analytical estimate and update the model.

Do not treat an LCR meter result as frequency-independent; record the measurement frequency and equivalent-series model.

## 11. Sources

1. Nuhas Oman, *PVC & LSOH Building Wires / Flexible Cables*, H05V-U table, page 2: https://www.nuhasoman.com/wp-content/uploads/2023/07/Building-Wires-Flexible-Cables-1.pdf
2. H. A. Wheeler, “Simple Inductance Formulas for Radio Coils,” *Proceedings of the IRE*, Vol. 16, No. 10, October 1928, pp. 1398–1400: https://physlab-wiki.com/_media/phylabs/lab_courses/phys-120_130-wiki-home/winter-experiments/simple_inductance_formulas_for_radio_coils.pdf
3. E. B. Rosa and L. Cohen, “The Mutual Inductance of Two Circular Coaxial Coils of Rectangular Section,” *Bulletin of the Bureau of Standards*, 1906, p. 360: https://digital.library.unt.edu/ark:/67531/metadc66517/m1/2/
4. E. B. Rosa and L. Cohen, *Formulae and Tables for the Calculation of Mutual and Self-Inductance*, *Bulletin of the Bureau of Standards*, Vol. 5, 1908, formulae for coaxial circles, pp. 6–7: https://nistdigitalarchives.contentdm.oclc.org/digital/api/collection/p16009coll6/id/15319/download
5. X. Chen, K. Li, Q. Liu and Z. Gong, “Design of tile shaped coil structure for wireless power transmission for underwater vehicle,” *Measurement and Control*, Vol. 58, Issue 1, pp. 60–67, first published online 4 May 2024, DOI: https://doi.org/10.1177/00202940241226590