# Research note — Chen et al., tile-shaped underwater WPT coil

## Bibliographic record

Xiaotong Chen, Kun Li, Qing Liu and Zheng Gong, “Design of tile shaped coil structure for wireless power transmission for underwater vehicle,” *Measurement and Control*, Volume 58, Issue 1, pages 60–67.

- First published online: 4 May 2024.
- Issue publication: January 2025.
- DOI: https://doi.org/10.1177/00202940241226590
- Publisher page: https://journals.sagepub.com/doi/10.1177/00202940241226590
- Licence stated by SAGE: Creative Commons Attribution 4.0 (CC BY 4.0).

This note summarizes the paper for engineering comparison. It does not reproduce the paper in full. Attribute the original authors and DOI when reusing its reported findings.

## 1. Research objective and coil concept

The authors propose a tile-shaped transmitter and receiver suitable for fitting to the outer shell of an autonomous underwater vehicle. The dock-side transmitter is larger than the vehicle-side receiver. They use HFSS simulation to study the effect of relative coil position and seawater/air environment, then build and test an underwater prototype.

This is a **tile-shaped coil research design**, not the same geometry as our circular planar spiral prototype.

## 2. Parameters reported in the paper

### HFSS model and environment

The paper describes:

| Parameter | Paper-reported value |
|---|---:|
| TX coil diameter | 72 mm |
| RX coil size | 0.8 × TX size = 57.6 mm |
| Coil separation in the simulation setup | 30 mm |
| Copper wire diameter in model | 2 mm |
| Seawater relative permittivity | 81 |
| Seawater electrical conductivity | 4 S/m |
| Seawater relative permeability | 0.999991 |
| Reported preferred seawater operating frequency | 30 kHz |

The paper compares air, fresh water and seawater and explains that seawater conductivity causes high-frequency eddy-current losses.

### Fabricated experimental coil

The paper reports:

| Parameter | Paper-reported value |
|---|---:|
| Winding | 6 turns |
| Inter-turn gap | 1 mm |
| Conductor | Litz wire |
| Litz construction | 500 strands × 0.1 mm |
| Ferrite shielding sheet thickness | 0.05 mm |
| Ferrite relative permeability | 200 |

The experimental coils were installed with magnetic shielding plates in a water tank. The reported prototype is not a bare PVC building-wire coil.

### Table 2 circuit values

| Parameter | Paper-reported value |
|---|---:|
| Input DC voltage range | 6–12 V |
| Output DC voltage | 10 V |
| TX self-inductance \(L_P\) | 8.86 µH |
| RX self-inductance \(L_S\) | 13.2 µH |
| TX matching capacitor \(C_1\) | 536 nF |
| RX matching capacitor \(C_2\) | 360 nF |
| Load \(R_0\) | 12 Ω |

## 3. Reported performance

The authors report that the underwater prototype reached approximately 30 W output and 68.5% transmission efficiency under their optimal alignment condition. They also report that a 10 mm radial offset reduced output power by about 16.7%.

These results belong to the paper's own tile-shaped coils, Litz conductors, ferrite arrangement, circuit and test conditions. They are not predicted performance for our prototype.

## 4. Important frequency consistency check

The article text states that 30 kHz was selected as the best operating frequency in its seawater simulation. However, the inductance and capacitor values in Table 2 imply a different ideal LC resonance if paired directly:

\[
f_0=\frac{1}{2\pi\sqrt{LC}}
\]

Using the reported primary values:

\[
L_P=8.86\ \mu H,\quad C_1=536\ nF
\]

\[
f_{0,P}\approx73.03\ kHz
\]

Using the reported secondary values:

\[
L_S=13.2\ \mu H,\quad C_2=360\ nF
\]

\[
f_{0,S}\approx73.01\ kHz
\]

This is an apparent discrepancy between the article's 30 kHz seawater optimum statement and the simple ideal LC resonance implied by Table 2. The paper may be reporting parameters from different conditions or a distinction not explicit in the extracted text. Do not combine the 30 kHz claim and Table 2 LC values as though they describe the same resonance without checking the full experimental context.

## 5. Relevance to our project

Useful research guidance:

1. The water medium must be included in the electromagnetic model; conductivity can create eddy-current losses.
2. Axial gap, radial offset and angular misalignment all influence transfer performance.
3. Ferrite backing can change coupling and field distribution, but it is an additional design variable and must be modelled/tested.
4. A Litz conductor was used in the experiment, unlike our current solid-wire prototype.
5. The paper's 30 mm reference separation is a useful comparison point, not proof that it is optimal for our geometry.

Not transferable without new analysis:

- 30 kHz as our operating frequency.
- 6 turns as our turn count.
- 72 mm / 57.6 mm as our coil diameters.
- 8.86 µH / 13.2 µH as our self-inductances.
- 536 nF / 360 nF as our compensation capacitors.
- 68.5% as our expected efficiency.

## 6. Equations from the paper

The paper's series-series resonance and coupled-circuit equations are summarized with definitions and applicability notes in [Chen paper equations](../formulas/chen-2024-paper-equations.md).

## 7. Reference

Chen, X., Li, K., Liu, Q., & Gong, Z. (2024; issue 2025). Design of tile shaped coil structure for wireless power transmission for underwater vehicle. *Measurement and Control*, 58(1), 60–67. https://doi.org/10.1177/00202940241226590

Publisher article: https://journals.sagepub.com/doi/10.1177/00202940241226590