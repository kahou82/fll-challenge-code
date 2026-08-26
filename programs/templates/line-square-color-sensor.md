# Template: Square Up on a Line (Color/Light Sensor)

Drives forward slowly until a color sensor detects a black line, giving a repeatable, precise stopping/alignment point on the mat regardless of small drive errors earlier in the run.

## Blocks (in order)

1. **Motion → Start moving**, speed = `approach_speed` (slow, e.g. 20)
2. **Control → repeat until** `Light sensor → reflected light` on the chosen sensor port < `line_threshold`
   - (leave the loop body empty — just keep driving until the condition trips)
3. **Motion → Stop moving**
4. Optional: **Sound → beep** or **Light → light up display** to confirm alignment during testing

## Inputs to expose as variables

| Variable | Meaning | Typical starting value |
|---|---|---|
| `approach_speed` | Speed while looking for the line | 15–20 (too fast = overshoot past the line before the sensor reads it) |
| `line_threshold` | Reflected light % that counts as "on the black line" | test on your mat — read the sensor value sitting on white vs. on the black line, pick a value in between |

## Tuning tips

- Test reflected-light values on the actual competition mat, not a printout — mat material/lighting affects sensor readings.
- Mount the sensor close to the mat (within the recommended range in the sensor's spec) for reliable readings.
- If using two color sensors (one per side) to square up straight against a line, run both loops in parallel (two sensor blocks side by side) and stop each motor independently when its sensor trips.

## Python reference

See `python-reference/line_square_color_sensor.py` for the equivalent logic.
