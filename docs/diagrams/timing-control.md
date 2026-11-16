# NE555 Timing and Bridge Control

```mermaid
flowchart TD
    VCC["Timer supply"] --> RA["RA"]
    RA --> DIS["Pin 7 · DISCH"]
    DIS --> RB["RB"]
    RB --> TIMENODE["Pins 2 and 6 joined"]
    TIMENODE --> CT["Timing capacitor"]
    CT --> GND["Ground"]
    TIMENODE --> P2["Pin 2 · TRIG"]
    TIMENODE --> P6["Pin 6 · THRES"]
    VCC --> P8["Pin 8 · VCC"]
    VCC --> P4["Pin 4 · RESET"]
    GND --> P1["Pin 1 · GND"]
    P3["Pin 3 · OUT"] --> LOGIC["Bridge switching logic"]
    LOGIC --> DEAD["Dead-time interlock"]
    DEAD --> DRV["Two half-bridge drivers"]
    DRV --> GATES["Four MOSFET gates"]
```

Astable timing equations:

- tH = 0.693 × (RA + RB) × C
- tL = 0.693 × RB × C
- f = 1.44 ÷ [(RA + 2RB) × C]

The NE555 output is a clock/reference, not four independent gate signals. The exact relationship between timer frequency and bridge frequency depends on the logic between the timer and gate drivers.
