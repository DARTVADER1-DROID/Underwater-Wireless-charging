# Research Note — Chen et al., Tile-Shaped Underwater WPT Coil

## Bibliographic record

Xiaotong Chen, Kun Li, Qing Liu and Zheng Gong, “Design of tile shaped coil structure for wireless power transmission for underwater vehicle,” *Measurement and Control*, Volume 58, Issue 1, pages 60–67.

- First published online: 4 May 2024.
- Issue publication: January 2025.
- DOI: https://doi.org/10.1177/00202940241226590
- Publisher page: https://journals.sagepub.com/doi/10.1177/00202940241226590
- Licence stated by SAGE: Creative Commons Attribution 4.0 (CC BY 4.0).

## 1. Research objective

The authors propose tile-shaped transmitter and receiver coils designed to fit the outer shell of an autonomous underwater vehicle. The paper uses electromagnetic simulation to study coil position and underwater effects, then describes an underwater prototype.

This is a tile-shaped research design, not the same geometry as this project's circular planar spiral.

## 2. Parameters reported by the paper

### Simulation geometry and medium

| Parameter | Paper-reported value |
|---|---:|
| TX coil diameter | 72 mm |
| RX coil size | 0.8 × TX size = 57.6 mm |
| Coil separation in simulation | 30 mm |
| Copper wire diameter in model | 2 mm |
| Seawater relative permittivity | 81 |
| Seawater conductivity | 4 S/m |
| Seawater relative permeability | 0.999991 |
| Preferred seawater simulation frequency stated in the paper | 30 kHz |

### Experimental winding and magnetic material

| Parameter | Paper-reported value |
|---|---:|
| Winding turns | 6 |
| Inter-turn gap | 1 mm |
| Conductor | Litz wire |
| Litz construction | 500 strands × 0.1 mm |
| Ferrite shielding sheet thickness | 0.05 mm |
| Ferrite relative permeability | 200 |

### Table 2 circuit values

| Parameter | Paper-reported value |
|---|---:|
| Input DC voltage range | 6–12 V |
| Output DC voltage | 10 V |
| TX self-inductance LP | 8.86 µH |
| RX self-inductance LS | 13.2 µH |
| TX matching capacitor C1 | 536 nF |
| RX matching capacitor C2 | 360 nF |
| Load R0 | 12 Ω |

These values describe the paper's own prototype and model. They are not this project's design values.

## 3. Performance reported by the paper

The authors report approximately 30 W output and 68.5% transmission efficiency under their optimal alignment condition. They also report that a 10 mm radial offset reduced output power by about 16.7%.

These results belong to the paper's tile-shaped coils, Litz conductors, ferrite arrangement, circuit and test conditions. They are not predicted performance for this prototype.

## 4. Readable frequency consistency calculation

For an ideal LC resonant branch:

**f0 = 1 / [2π × square root(L × C)]**.

Using the primary values from Table 2:

- LP = 8.86 µH = 8.86 × 10⁻⁶ H.
- C1 = 536 nF = 536 × 10⁻⁹ F.

Substitute:

f0 = 1 / [2π × square root((8.86 × 10⁻⁶) × (536 × 10⁻⁹))]  
≈ **73.03 kHz**.

Using the secondary values:

- LS = 13.2 µH = 13.2 × 10⁻⁶ H.
- C2 = 360 nF = 360 × 10⁻⁹ F.

f0 = 1 / [2π × square root((13.2 × 10⁻⁶) × (360 × 10⁻⁹))]  
≈ **73.01 kHz**.

The paper also states that 30 kHz was selected as the best operating frequency in its seawater simulation. This creates an apparent difference between that statement and the simple ideal LC resonance implied by the Table 2 values. The article may be describing different operating conditions or a distinction not explicit in the extracted text. Do not assume the 30 kHz statement and Table 2 values refer to the same resonant condition without checking the full paper.

## 5. Relevance to this project

Useful guidance:

1. Conductive seawater must be included in the electromagnetic model because it can cause eddy-current losses.
2. Axial gap, radial offset and angular misalignment influence transfer.
3. Ferrite backing changes magnetic-field distribution and must be modelled or measured.
4. The paper uses Litz wire, unlike this project's initial solid-wire reference.
5. Its 30 mm gap is a comparison point, not proof that 30 mm is optimal for our coil.

Do not directly transfer the paper's operating frequency, turn count, dimensions, inductance, capacitance or efficiency to this prototype.

## 6. Equation note

The paper's series-series resonance and coupled-circuit equations are transcribed in readable form in [Chen paper equations](../equations/chen-2024-paper-equations.md). The project's Wheeler, Maxwell/Neumann and coupling equations are documented separately in [formula provenance](../formula-provenance.md).

## 7. Reference

Chen, X., Li, K., Liu, Q., & Gong, Z. (2024; issue 2025). Design of tile shaped coil structure for wireless power transmission for underwater vehicle. *Measurement and Control*, 58(1), 60–67. https://doi.org/10.1177/00202940241226590
