# Formula Provenance — Human-Readable Reference

This file explains where each formula comes from, what its symbols mean and how it is used. Equations are written in plain text with words and units so that readers do not need to interpret raw LaTeX.

## 1. Wheeler flat-spiral self-inductance approximation

**Source:** Harold A. Wheeler, “Simple Inductance Formulas for Radio Coils,” *Proceedings of the IRE*, Volume 16, Number 10, October 1928, equation (3).

For a single-layer flat spiral:

**L in microhenries = (N × N × a × a) / (8 × a + 11 × c)**

Definitions:

- L = self-inductance estimate, in microhenries (µH).
- N = number of turns.
- a = average winding radius, in inches.
- c = radial winding width, in inches.

The dimensions must be entered in inches for this version of the formula. The equation is an approximation. Wheeler's discussion includes accuracy conditions and cautions about few turns, spacing, skin effect and distributed capacitance. Do not treat the often-quoted 5% condition as a guaranteed tolerance for every coil.

## 2. Neumann mutual-inductance integral

The general Neumann equation can be read as:

**M = (µ0 / 4π) × the sum over every pair of small conductor elements of [(element 1 direction dot element 2 direction) / distance between the elements].**

In mathematical notation, the differential line elements are dℓ1 and dℓ2, and their separation is R. The double integral runs around both closed current paths.

Definitions:

- M = mutual inductance, in henries.
- µ0 = permeability of free space, 4π × 10⁻⁷ H/m.
- dℓ1, dℓ2 = infinitesimal directed lengths along the two conductors.
- R = distance between those two small conductor elements.

This is the general magnetostatic starting point for mutual inductance between filamentary closed circuits.

**Primary reference:** Edward B. Rosa and Louis Cohen, *Formulae and Tables for the Calculation of Mutual and Self-Inductance*, U.S. Bureau of Standards Bulletin 5 (1908).

NIST digital archive: https://nistdigitalarchives.contentdm.oclc.org/digital/api/collection/p16009coll6/id/15319/download

## 3. Maxwell equation for two coaxial circular filament loops

For two coaxial circular loops with radii r1 and r2 and axial separation h:

**Step 1 — elliptic parameter**

m = (4 × r1 × r2) / [(r1 + r2)² + h²].

**Step 2 — elliptic modulus**

q = square root(m).

**Step 3 — complete elliptic integrals**

- K(m) = complete elliptic integral of the first kind.
- E(m) = complete elliptic integral of the second kind.

**Step 4 — mutual inductance of one loop pair**

M-pair = µ0 × square root(r1 × r2) × {[(2 / q) − q] × K(m) − (2 / q) × E(m)}.

Use metres for r1, r2 and h. Use µ0 = 4π × 10⁻⁷ H/m. The answer is in henries.

**Notation warning:** q is the elliptic modulus; m = q² is the parameter passed to K and E. Numerical libraries such as SciPy use the parameter m. Do not confuse q with the coupling coefficient k.

**Reference:** Rosa and Cohen, U.S. Bureau of Standards publications (1906 and 1908), which document Maxwell's elliptic-integral formula for coaxial circular filaments.

- 1906 scan: https://digital.library.unt.edu/ark:/67531/metadc66517/m1/2/
- 1908 NIST archive: https://nistdigitalarchives.contentdm.oclc.org/digital/api/collection/p16009coll6/id/15319/download

## 4. Multi-turn mutual inductance

For two coils represented by individual circular turns:

**Total mutual inductance = add the mutual inductance of every TX-turn / RX-turn pair.**

For two seven-turn coils, calculate 7 × 7 = 49 pair contributions and add all 49 values. The sign of each term depends on winding direction. In the current aligned same-winding-sense model, the contributions add.

## 5. Coupling coefficient

General equation:

**k = M / square root(L1 × L2)**

Definitions:

- k = coupling coefficient; dimensionless.
- M = mutual inductance.
- L1 = self-inductance of coil 1.
- L2 = self-inductance of coil 2.

Use the same unit for all inductances; the units cancel.

For equal coils where L1 = L2 = L:

**k = M / L**.

For passive coupled inductors, the magnitude of k cannot exceed 1. This is a mathematical/physical consistency condition, not proof that a numerical model is accurate.

## 6. Experimental mutual-inductance measurement

If both coils are connected in series, measure the total inductance in series-aiding and series-opposing configurations:

**M = (L-aiding − L-opposing) / 4**.

This relationship assumes the two measurements use the same coils and test frequency, with only the relative polarity changed. Measure each coil's self-inductance under the same frequency and fixture conditions, then calculate:

**k = M / square root(L1 × L2)**.

Record meter model, test frequency, fixture compensation, coil position, temperature and surrounding medium.

## 7. Resonance formula — not yet applied to this design

For an ideal LC resonant branch:

**f0 = 1 / [2π × square root(L × C)]**.

Rearranged for capacitance:

**C = 1 / [(2π × f0)² × L]**.

This formula must not be used to select capacitors until operating frequency, measured in-environment inductance and compensation topology are selected. Research-paper equations are summarized separately in [Chen et al. paper equations](chen-2024-paper-equations.md).
