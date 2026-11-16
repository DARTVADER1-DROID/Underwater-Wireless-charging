#!/usr/bin/env python3
"""Generate the parameterized LTspice netlist for the UWLPT resonant link.

Run:
    python tools/schematic_generator/generate_resonant_link.py

The generated netlist is circuits/uwlpt-resonant-link.cir.
No third-party Python packages are required.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "circuits" / "uwlpt-resonant-link.cir"

NETLIST = r"""* UWLPT coupled-resonant link - first-pass LTspice testbench
* This is an AC-link model, NOT a complete charger or a production schematic.
* Ideal bipolar source represents the differential output of a 12 V full bridge.
* RX return is weakly referenced to ground only to avoid a floating-node singularity.
* The 1 GOhm reference is a numerical aid, not a physical galvanic connection.

.param FSW=30k
.param VBUS=12
.param LTX=2.29631793u
.param LRX=2.29631793u
.param KCOUP=0.1426861491
.param CTX=12.27u
.param CRX=12.27u
.param RLOAD=12

* Ideal full-bridge differential output: -VBUS to +VBUS, 50% duty
VBRIDGE n_drive 0 PULSE(-{VBUS} {VBUS} 0 20n 20n {0.5/FSW} {1/FSW})

* Transmitter series-series compensated loop
CTX1 n_drive n_tx {CTX}
LTX1 n_tx 0 {LTX}

* Receiver series-series compensated loop; electrically isolated in this model
LRX1 n_rx n_rx_cap {LRX}
CRX1 n_rx_cap n_load {CRX}
RLOAD1 n_load n_rx_return {RLOAD}
RREF n_rx_return 0 1G

* Coupling coefficient between the two coils
KTXRX LTX1 LRX1 {KCOUP}

* Analysis
.tran 0 5m 0 100n
.options plotwinsize=0
.save V(n_drive) V(n_tx) V(n_rx) V(n_load) I(LTX1) I(LRX1)

.end
"""

if __name__ == "__main__":
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(NETLIST, encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
