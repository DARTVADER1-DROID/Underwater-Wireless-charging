#!/usr/bin/env python3
"""Reproduce the preliminary air-core TX/RX coil calculations.

Dependencies:
    python -m pip install scipy

Model:
- Seven identical, coaxial, circular filament turns per coil.
- Maxwell coaxial circular-loop mutual-inductance expression.
- Wheeler 1928 single-layer spiral self-inductance approximation.
- Air/free-space permeability; no seawater, ferrite, finite-wire, or lead model.

This script is a calculation aid, not a validated electromagnetic solver.
"""

from __future__ import annotations

import math
from scipy.special import ellipk, ellipe

MU0 = 4.0 * math.pi * 1e-7  # H/m

# Explicit design inputs
OUTER_DIAMETER_MM = 70.0
INNER_OPENING_DIAMETER_MM = 20.0
INSULATED_WIRE_DIAMETER_MM = 2.7
TURNS = 7
COIL_PLANE_GAP_MM = 30.0

# Boundary-to-centreline conversion
wire_radius_mm = INSULATED_WIRE_DIAMETER_MM / 2.0
outer_cl_diameter_mm = OUTER_DIAMETER_MM - 2.0 * wire_radius_mm
inner_cl_diameter_mm = INNER_OPENING_DIAMETER_MM + 2.0 * wire_radius_mm

outer_radius_mm = outer_cl_diameter_mm / 2.0
inner_radius_mm = inner_cl_diameter_mm / 2.0
radial_width_mm = outer_radius_mm - inner_radius_mm

if TURNS < 2:
    raise ValueError("This equally spaced endpoint geometry requires at least two turns.")

pitch_mm = radial_width_mm / (TURNS - 1)
clear_gap_mm = pitch_mm - INSULATED_WIRE_DIAMETER_MM
if clear_gap_mm < 0:
    raise ValueError("Turns overlap: increase radial space or reduce wire diameter.")

turn_radii_m = [
    (outer_radius_mm - i * pitch_mm) / 1000.0
    for i in range(TURNS)
]

# Wheeler formula (3): a and c are inches, output is microhenries.
mean_radius_mm = (outer_radius_mm + inner_radius_mm) / 2.0
a_in = mean_radius_mm / 25.4
c_in = radial_width_mm / 25.4
L_self_uH = (TURNS**2 * a_in**2) / (8.0 * a_in + 11.0 * c_in)


def mutual_of_two_coaxial_filaments(a_m: float, b_m: float, h_m: float) -> float:
    """Return Maxwell mutual inductance in henries.

    scipy.special.ellipk/ellipe take the elliptic parameter m = q**2.
    """
    q = 2.0 * math.sqrt(a_m * b_m) / math.sqrt((a_m + b_m) ** 2 + h_m**2)
    m = q * q
    K = float(ellipk(m))
    E = float(ellipe(m))
    return MU0 * math.sqrt(a_m * b_m) * (
        (2.0 / q - q) * K - (2.0 / q) * E
    )


gap_m = COIL_PLANE_GAP_MM / 1000.0
matrix_uH = [
    [
        mutual_of_two_coaxial_filaments(a, b, gap_m) * 1e6
        for b in turn_radii_m
    ]
    for a in turn_radii_m
]
row_sums_uH = [sum(row) for row in matrix_uH]
M_total_uH = sum(row_sums_uH)

# Coupling coefficient from the approximate self-L and filament-pair M.
k = M_total_uH / math.sqrt(L_self_uH * L_self_uH)
energy_determinant_uH2 = L_self_uH * L_self_uH - M_total_uH**2

# Numerical/physical sanity checks.
assert all(value > 0.0 for row in matrix_uH for value in row)
assert all(
    math.isclose(matrix_uH[i][j], matrix_uH[j][i], rel_tol=1e-12, abs_tol=1e-15)
    for i in range(TURNS)
    for j in range(TURNS)
)
assert 0.0 <= abs(k) <= 1.0
assert energy_determinant_uH2 >= 0.0

print("GEOMETRY")
print(f"Outer centreline diameter: {outer_cl_diameter_mm:.7f} mm")
print(f"Inner centreline diameter: {inner_cl_diameter_mm:.7f} mm")
print(f"Outer centreline radius:   {outer_radius_mm:.7f} mm")
print(f"Inner centreline radius:   {inner_radius_mm:.7f} mm")
print(f"Mean radius:               {mean_radius_mm:.7f} mm")
print(f"Radial width:              {radial_width_mm:.7f} mm")
print(f"Centreline pitch:          {pitch_mm:.7f} mm")
print(f"Clear insulated gap:       {clear_gap_mm:.7f} mm")
print("Turn radii (mm):", ", ".join(f"{r * 1000:.7f}" for r in turn_radii_m))

print("\nSELF-INDUCTANCE (Wheeler, air-core estimate)")
print(f"L_TX = L_RX = {L_self_uH:.10f} uH")

print("\nMUTUAL-INDUCTANCE MATRIX (uH)")
for row in matrix_uH:
    print(" ".join(f"{value:.9f}" for value in row))
print("Row sums (uH):", ", ".join(f"{value:.9f}" for value in row_sums_uH))
print(f"M_total = {M_total_uH:.10f} uH")

print("\nCOUPLING")
print(f"k = {k:.10f}")
print(f"L_TX * L_RX - M^2 = {energy_determinant_uH2:.10f} uH^2")
print("Checks passed: symmetric M matrix, positive pair terms, |k| <= 1, non-negative energy determinant.")
