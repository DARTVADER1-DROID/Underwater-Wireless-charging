#!/usr/bin/env python3
"""Reproduce and cross-check the preliminary air-core TX/RX coil calculations.

Dependencies:
    python -m pip install scipy

Model:
- Seven identical, coaxial, circular filament turns per coil.
- Maxwell coaxial circular-loop mutual-inductance expression.
- Independent direct Neumann angular quadrature for mutual-inductance check.
- Wheeler 1928 single-layer spiral self-inductance approximation.
- Air/free-space permeability; no seawater, ferrite, finite-wire, or lead model.

This is an analytical calculation aid, not a validated electromagnetic solver.
"""

from __future__ import annotations

import math
from scipy.integrate import quad
from scipy.special import ellipe, ellipk

MU0 = 4.0 * math.pi * 1e-7  # H/m

# Explicit design inputs
OUTER_DIAMETER_MM = 70.0
INNER_OPENING_DIAMETER_MM = 20.0
INSULATED_WIRE_DIAMETER_MM = 2.7
TURNS = 7
COIL_PLANE_GAP_MM = 30.0


def wheeler_single_layer_spiral_uH(
    turns: int, mean_radius_mm: float, radial_width_mm: float
) -> float:
    """Wheeler 1928 equation (3), with dimensions converted to inches."""
    mean_radius_in = mean_radius_mm / 25.4
    radial_width_in = radial_width_mm / 25.4
    return (
        turns**2 * mean_radius_in**2
        / (8.0 * mean_radius_in + 11.0 * radial_width_in)
    )


def mutual_maxwell_h(a_m: float, b_m: float, h_m: float) -> float:
    """Maxwell coaxial circular-filament formula; return henries.

    scipy.special.ellipk/ellipe take the elliptic parameter m = q**2.
    """
    q = 2.0 * math.sqrt(a_m * b_m) / math.sqrt((a_m + b_m) ** 2 + h_m**2)
    m = q * q
    K = float(ellipk(m))
    E = float(ellipe(m))
    return MU0 * math.sqrt(a_m * b_m) * (
        (2.0 / q - q) * K - (2.0 / q) * E
    )


def mutual_neumann_quadrature_h(
    a_m: float, b_m: float, h_m: float
) -> tuple[float, float]:
    """Direct angular reduction of the Neumann double-line integral.

    Returns (mutual inductance in henries, estimated quadrature error in H).
    """
    def integrand(phi: float) -> float:
        distance = math.sqrt(
            a_m**2 + b_m**2 + h_m**2 - 2.0 * a_m * b_m * math.cos(phi)
        )
        return math.cos(phi) / distance

    integral, error = quad(
        integrand,
        0.0,
        2.0 * math.pi,
        epsabs=1e-12,
        epsrel=1e-12,
        limit=500,
    )
    return MU0 * a_m * b_m * integral / 2.0, MU0 * a_m * b_m * error / 2.0


def main() -> None:
    if TURNS < 2:
        raise ValueError("This equally spaced endpoint geometry requires at least two turns.")

    # Boundary-to-centreline conversion
    wire_radius_mm = INSULATED_WIRE_DIAMETER_MM / 2.0
    outer_cl_diameter_mm = OUTER_DIAMETER_MM - 2.0 * wire_radius_mm
    inner_cl_diameter_mm = INNER_OPENING_DIAMETER_MM + 2.0 * wire_radius_mm

    outer_radius_mm = outer_cl_diameter_mm / 2.0
    inner_radius_mm = inner_cl_diameter_mm / 2.0
    radial_width_mm = outer_radius_mm - inner_radius_mm
    pitch_mm = radial_width_mm / (TURNS - 1)
    clear_gap_mm = pitch_mm - INSULATED_WIRE_DIAMETER_MM

    if clear_gap_mm < 0.0:
        raise ValueError("Turns overlap: increase radial space or reduce wire diameter.")

    turn_radii_m = [
        (outer_radius_mm - i * pitch_mm) / 1000.0
        for i in range(TURNS)
    ]

    mean_radius_mm = (outer_radius_mm + inner_radius_mm) / 2.0
    L_self_uH = wheeler_single_layer_spiral_uH(
        TURNS, mean_radius_mm, radial_width_mm
    )

    gap_m = COIL_PLANE_GAP_MM / 1000.0
    maxwell_matrix_uH = [
        [
            mutual_maxwell_h(a, b, gap_m) * 1e6
            for b in turn_radii_m
        ]
        for a in turn_radii_m
    ]
    neumann_matrix_uH = [
        [
            mutual_neumann_quadrature_h(a, b, gap_m)[0] * 1e6
            for b in turn_radii_m
        ]
        for a in turn_radii_m
    ]

    M_maxwell_uH = sum(map(sum, maxwell_matrix_uH))
    M_neumann_uH = sum(map(sum, neumann_matrix_uH))
    M_difference_uH = M_maxwell_uH - M_neumann_uH

    # Identical TX/RX coils, using the same approximate self-inductance.
    k = M_maxwell_uH / math.sqrt(L_self_uH * L_self_uH)
    energy_determinant_uH2 = L_self_uH**2 - M_maxwell_uH**2

    # Numerical and physical consistency checks.
    assert all(v > 0.0 for row in maxwell_matrix_uH for v in row)
    assert all(
        math.isclose(
            maxwell_matrix_uH[i][j],
            maxwell_matrix_uH[j][i],
            rel_tol=1e-12,
            abs_tol=1e-15,
        )
        for i in range(TURNS)
        for j in range(TURNS)
    )
    assert abs(M_difference_uH) < 1e-10
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
    print(f"L_TX = L_RX = {L_self_uH:.12f} uH")

    print("\nMUTUAL-INDUCTANCE MATRIX (Maxwell, uH)")
    for row in maxwell_matrix_uH:
        print(" ".join(f"{value:.9f}" for value in row))
    print(f"M_Maxwell = {M_maxwell_uH:.12f} uH")
    print(f"M_Neumann = {M_neumann_uH:.12f} uH")
    print(f"Difference = {M_difference_uH:.3e} uH")

    print("\nCOUPLING")
    print(f"k = {k:.12f}")
    print(f"L_TX * L_RX - M^2 = {energy_determinant_uH2:.12f} uH^2")
    print("All numerical and physical consistency checks passed.")


if __name__ == "__main__":
    main()
