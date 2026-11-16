# TX and RX Coil Design — Calculation Record

**Revision:** 16 November 2026  
**Status:** Preliminary analytical estimate; not yet validated by physical measurement or a full-field electromagnetic solver.

This document deliberately writes equations in plain text, defines every symbol and shows the numerical substitutions. No calculation should require the reader to interpret raw LaTeX source.

## 1. Design inputs and assumptions

| Item | Value | Status |
|---|---:|---|
| DC input | 12 V | User requirement |
| Target transferred power | 24 W | User requirement |
| TX coil outer diameter | 70 mm | Current design dimension |
| RX coil outer diameter | 70 mm | Current design dimension |
| Clear inner opening | 20 mm | Current design dimension |
| Turns per coil | 7 | Current design iteration |
| Insulated wire diameter | 2.7 mm | H05V-U reference value; verify exact purchased product |
| Coil plane separation | 30 mm | Reference calculation |
| Alignment | Coaxial and parallel | Analytical assumption |
| Medium in this calculation | Free space / air-core | Simplifying assumption |

The current model excludes finite copper cross-section, lead wires, ferrite, nearby structures, encapsulation, lateral misalignment and conductive saltwater losses. H05V-U building wire is not immersion-rated; waterproofing must be engineered separately.

## 2. Coil geometry

### 2.1 Convert physical boundaries to wire-centreline boundaries

Wire radius = 2.7 mm / 2 = **1.35 mm**.

The outermost wire centreline must sit one wire radius inside the physical outer boundary:

Outer centreline diameter = 70.0 − 2 × 1.35 = **67.3 mm**.

The innermost wire centreline must sit one wire radius outside the clear opening:

Inner centreline diameter = 20.0 + 2 × 1.35 = **22.7 mm**.

Therefore:

- Outer centreline radius = 67.3 / 2 = **33.65 mm**.
- Inner centreline radius = 22.7 / 2 = **11.35 mm**.
- Radial winding width = 33.65 − 11.35 = **22.30 mm**.

### 2.2 Derive pitch and clear spacing

Seven turns create six equal centreline intervals.

Centreline pitch = radial width / (turns − 1)  
= 22.30 mm / 6  
= **3.7166667 mm**.

Clear insulation-to-insulation gap = pitch − insulated wire diameter  
= 3.7166667 − 2.7  
= **1.0166667 mm**.

This gap is derived from the chosen boundaries and turn count. It is not an arbitrary 0.5 mm value.

### 2.3 Turn centreline radii

| Turn, outermost to innermost | Radius |
|---:|---:|
| 1 | 33.650000 mm |
| 2 | 29.933333 mm |
| 3 | 26.216667 mm |
| 4 | 22.500000 mm |
| 5 | 18.783333 mm |
| 6 | 15.066667 mm |
| 7 | 11.350000 mm |

Average radius for Wheeler's formula = (33.65 + 11.35) / 2 = **22.50 mm**.

Radial winding width for Wheeler's formula = **22.30 mm**.

Convert to inches (1 inch = 25.4 mm):

- Average radius a = 22.50 / 25.4 = **0.8858267717 in**.
- Radial width c = 22.30 / 25.4 = **0.8779527559 in**.

## 3. Self-inductance of TX and RX coils

### 3.1 Formula and source

Harold A. Wheeler, “Simple Inductance Formulas for Radio Coils,” *Proceedings of the IRE*, Vol. 16, No. 10, 1928, equation (3).

For a single-layer flat spiral:

**L (µH) = (N × N × a × a) / (8 × a + 11 × c)**

Definitions and units:

- L = estimated self-inductance in microhenries (µH).
- N = number of turns.
- a = average winding radius in inches.
- c = radial winding width in inches.

The dimensions must be in inches for this version of the equation.

### 3.2 Substitute the actual design values

N = 7  
a = 0.8858267717 in  
c = 0.8779527559 in

Numerator:

7 × 7 × 0.8858267717 × 0.8858267717  
= **38.4497644**.

Denominator:

(8 × 0.8858267717) + (11 × 0.8779527559)  
= 7.08661417 + 9.65748031  
= **16.74409449**.

Divide:

L = 38.4497644 / 16.74409449  
= **2.29631793 µH**.

The TX and RX geometry is identical in this model, so:

- TX self-inductance estimate = **2.29631793 µH**.
- RX self-inductance estimate = **2.29631793 µH**.

### 3.3 Accuracy warning

This is an empirical approximation, not a finite-wire field solution. Wheeler discusses conditions for approximate accuracy, but the stated 5% condition is not a guaranteed ±5% bound for this seven-turn coil. Low turn count, spacing, leads, frequency-dependent conductor effects and nearby materials can all matter. The displayed digits preserve calculation traceability; they do not imply measurement accuracy.

## 4. Mutual inductance between TX and RX

### 4.1 What is being calculated?

Each TX turn couples magnetically to every RX turn. With seven turns on each side, there are 7 × 7 = **49 turn-pair contributions**.

The coil-to-coil mutual inductance is the sum of those 49 contributions, assuming all turns have the same winding sense and the coils are coaxial.

### 4.2 Formula for one coaxial circular turn pair

This is Maxwell's coaxial circular-filament formula, derived from the Neumann mutual-inductance integral and documented in the Bureau of Standards publications by Rosa and Cohen.

For a TX turn radius r1, RX turn radius r2 and axial separation h:

Step 1 — calculate the elliptic-integral parameter:

m = (4 × r1 × r2) / ((r1 + r2) × (r1 + r2) + h × h).

Step 2 — calculate q:

q = square root of m.

Step 3 — obtain two standard complete elliptic-integral values:

- K(m): complete elliptic integral of the first kind.
- E(m): complete elliptic integral of the second kind.

Step 4 — calculate the mutual inductance of this one turn pair:

M-pair = µ0 × square root(r1 × r2) × ([(2 / q) − q] × K(m) − (2 / q) × E(m)).

Here µ0 = 4π × 10⁻⁷ H/m. Use metres for r1, r2 and h. The result is in henries; multiply by 1,000,000 to obtain microhenries.

**Notation warning:** q is the elliptic modulus and m = q × q is the elliptic parameter. Software functions such as SciPy's ellipk and ellipe expect m, not q. This q is not the coil coupling coefficient.

### 4.3 Fully worked outermost-turn example

For the outermost pair:

- r1 = 33.65 mm = 0.03365 m.
- r2 = 33.65 mm = 0.03365 m.
- h = 30 mm = 0.03000 m.

Calculate m:

Numerator = 4 × 0.03365 × 0.03365 = 0.00452929.

Denominator = (0.03365 + 0.03365)² + 0.03000²  
= 0.06730² + 0.03000²  
= 0.00452929 + 0.00090000  
= 0.00542929.

Therefore:

m = 0.00452929 / 0.00542929  
= **0.8342324687**.

q = square root(0.8342324687)  
= **0.9133632731**.

Numerically evaluated elliptic integrals:

- K(m) = **2.3429814649**.
- E(m) = **1.1547837741**.

Substituting these values into the turn-pair equation gives:

M-pair = **1.95282019 × 10⁻⁸ H**  
= **0.0195282019 µH**.

That is one pair only. It is not the complete coil-to-coil mutual inductance.

### 4.4 Add all 49 turn-pair contributions

The matrix below gives each turn-pair contribution in µH. Rows are TX turns and columns are RX turns; both are ordered outermost to innermost.

| TX turn / RX turn | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.01952820 | 0.01681235 | 0.01383990 | 0.01079494 | 0.00786994 | 0.00524020 | 0.00304894 |
| 2 | 0.01681235 | 0.01474162 | 0.01235673 | 0.00980120 | 0.00725100 | 0.00488670 | 0.00286983 |
| 3 | 0.01383990 | 0.01235673 | 0.01055599 | 0.00853043 | 0.00641997 | 0.00439077 | 0.00260898 |
| 4 | 0.01079494 | 0.00980120 | 0.00853043 | 0.00702889 | 0.00539092 | 0.00375044 | 0.00226026 |
| 5 | 0.00786994 | 0.00725100 | 0.00641997 | 0.00539092 | 0.00421606 | 0.00298812 | 0.00183017 |
| 6 | 0.00524020 | 0.00488670 | 0.00439077 | 0.00375044 | 0.00298812 | 0.00215784 | 0.00134448 |
| 7 | 0.00304894 | 0.00286983 | 0.00260898 | 0.00226026 | 0.00183017 | 0.00134448 | 0.00085163 |

Row sums:

| TX turn | Sum of its seven pair contributions (µH) |
|---:|---:|
| 1 | 0.07713448 |
| 2 | 0.06871943 |
| 3 | 0.05870276 |
| 4 | 0.04755709 |
| 5 | 0.03596616 |
| 6 | 0.02475855 |
| 7 | 0.01481429 |

Adding the seven row sums:

M-total = 0.07713448 + 0.06871943 + 0.05870276 + 0.04755709 + 0.03596616 + 0.02475855 + 0.01481429  
= **0.3276527625 µH**.

The underlying calculation uses unrounded values; displayed matrix entries and row sums are rounded for readability.

### 4.5 Independent numerical cross-check

The same mutual inductance was evaluated a second way, by numerically integrating the Neumann line-integral expression after exploiting rotational symmetry for coaxial circular loops. This is a separate numerical implementation, not a physical measurement.

Results:

- Maxwell elliptic-integral pair summation: **0.327652762514934 µH**.
- Direct Neumann angular quadrature: **0.327652762514934 µH**.
- Difference at displayed precision: less than **1 × 10⁻¹² µH**.

The agreement checks the elliptic-integral implementation and the 49-pair sum. It does not validate the ideal-filament approximation or the Wheeler self-inductance estimate.

## 5. Coupling coefficient — fresh derivation

### 5.1 Definition

The coupling coefficient describes the magnetic coupling between two inductors. It has no unit.

General equation:

**k = M / square root(L-TX × L-RX)**

Where:

- k = coupling coefficient (dimensionless).
- M = mutual inductance.
- L-TX = transmitter self-inductance.
- L-RX = receiver self-inductance.

All three inductances must use the same unit. Here they are all in µH, so the units cancel.

### 5.2 Simplify for identical coils

The present model uses identical TX and RX coils:

L-TX = L-RX = 2.2963179303 µH.

Therefore:

square root(L-TX × L-RX)  
= square root(2.2963179303 × 2.2963179303) µH  
= **2.2963179303 µH**.

So the general equation reduces to:

**k = M / L**.

### 5.3 Substitute the verified mutual-inductance sum

M = 0.327652762514934 µH.

L = 2.296317930279877 µH.

k = 0.327652762514934 / 2.296317930279877  
= **0.1426861491**.

Rounded appropriately for an analytical estimate:

**k ≈ 0.1427 (dimensionless).**

If expressed as 100 × k, this is 14.2686%. This is not 14.2686% power-transfer efficiency. Coupling coefficient and power-transfer efficiency are different quantities.

### 5.4 Verify by rearranging the equation

Rearranged equation:

M-check = k × square root(L-TX × L-RX).

Substitute:

M-check = 0.1426861491 × 2.2963179303 µH  
= **0.3276527625 µH** (rounding only).

This reproduces the mutual inductance used in the calculation.

### 5.5 Physical consistency checks

For passive coupled inductors, the magnitude must satisfy:

**0 ≤ |k| ≤ 1**.

Our result is 0.1426861491, which is within the physical bound.

A second equivalent inductance-matrix check is:

L-TX × L-RX − M² must be greater than or equal to zero.

Using the current values:

(2.2963179303 × 2.2963179303) − (0.3276527625 × 0.3276527625)  
= approximately **5.16571970 µH²**, which is positive.

Both checks pass. These checks establish mathematical consistency, not experimental accuracy.

### 5.6 Important model limitation

The self-inductance uses Wheeler's empirical flat-spiral approximation. Mutual inductance uses ideal circular-filament turn pairs. Since the two values come from different approximations, their ratio is only a preliminary coupling estimate. A final value should come from one consistent finite-conductor field model or from measurements of the completed coils.

## 6. Verified result summary

| Quantity | Value | Status |
|---|---:|---|
| TX self-inductance | 2.29631793 µH | Wheeler estimate |
| RX self-inductance | 2.29631793 µH | Wheeler estimate |
| Mutual inductance at 30 mm | 0.3276527625 µH | 49-pair Maxwell sum; independently quadrature-checked |
| Coupling coefficient | 0.1426861491 | Derived from the above estimates; dimensionless |

Only the 30 mm mutual-inductance case is included as a fully rechecked numerical result in this revision. Other gap values should not be treated as verified until recalculated with the same audited model.

## 7. What remains to be validated

1. Measure each coil's self-inductance with a stated test frequency and fixture.
2. Measure mutual inductance with a series-aiding / series-opposing test or a validated impedance method.
3. Calculate k from measured L-TX, L-RX and M at the same frequency.
4. Repeat with the actual enclosure and surrounding materials.
5. Measure saltwater conductivity at the test temperature and include it in the field model.
6. Evaluate AC resistance, skin effect, proximity effect and temperature rise.
7. Only after these checks, choose the compensation topology and calculate resonant capacitors.
