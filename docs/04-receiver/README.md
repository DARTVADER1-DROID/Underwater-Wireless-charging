# Receiver

The receiver consists of the RX resonant coil/capacitor, a high-frequency bridge rectifier, optional output filtering and a resistive load.

## Rectifier design requirements

The rectifier must be selected using the actual measured secondary waveform, not the nominal battery voltage. Determine:

- Peak and RMS secondary voltage.
- Peak and RMS secondary current.
- Reverse-voltage requirement including resonant transients.
- Switching/reverse-recovery behaviour at the operating frequency.
- Forward loss and thermal dissipation.
- Whether an output capacitor is required and its ripple-current rating.

At a 30 kHz-class operating frequency, do not assume an ordinary mains-frequency rectifier is suitable. Fast-recovery or Schottky devices may be candidates, but the correct choice depends on the actual voltage and current.

## Resistive load

For a resistive DC load:

- Rload = Vout ÷ Iout
- Pload = Vout × Iout = Vout² ÷ Rload

The required receiver DC voltage and output power are not yet fixed. Therefore, no load resistance or rectifier part number is locked.
