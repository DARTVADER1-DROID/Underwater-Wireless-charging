# Full H-Bridge Topology

```mermaid
flowchart TB
    VBUS["+12 V DC bus"] --> Q1["Q1 · high-side MOSFET"]
    VBUS --> Q3["Q3 · high-side MOSFET"]
    Q1 --> A["Switch node A"]
    Q2["Q2 · low-side MOSFET"] --> A
    Q3 --> B["Switch node B"]
    Q4["Q4 · low-side MOSFET"] --> B
    A <-->|"TX resonant branch"| B
    Q2 --> GND["Battery negative / DC return"]
    Q4 --> GND

    CTRL["NE555 timing reference"] --> LOGIC["Bridge logic · interlock · dead time"]
    LOGIC --> DA["Half-bridge driver A"]
    LOGIC --> DB["Half-bridge driver B"]
    DA -. "High-side and low-side outputs" .-> Q1
    DA -.-> Q2
    DB -. "High-side and low-side outputs" .-> Q3
    DB -.-> Q4
```

| Bridge state | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| Positive | ON | OFF | OFF | ON |
| Dead time | OFF | OFF | OFF | OFF |
| Negative | OFF | ON | ON | OFF |
| Dead time | OFF | OFF | OFF | OFF |

The two MOSFETs in the same leg must never be commanded ON simultaneously.
