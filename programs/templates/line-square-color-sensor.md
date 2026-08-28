# Template: Square Up on a Line (Color/Light Sensor)

Drives forward slowly until a color sensor detects a black line, giving a repeatable, precise stopping/alignment point on the mat regardless of small drive errors earlier in the run.

## Blocks (in order)

Translated directly from `python-reference/line_square_color_sensor.py`:

1. **Variables → Make a Variable**: `approach_speed`, `line_threshold`
2. **Variables → set** `approach_speed` to `18`, `line_threshold` to `20`
3. **Motion → Start moving**, speed = `[approach_speed]`%, steering `0`
4. **Control → repeat until** `(Color sensor → reflected light [port E]) < [line_threshold]`
   - (leave the loop body empty — just keep driving until the condition trips; no explicit wait block needed, the sensor block is polled automatically)
5. **Motion → Stop moving**
6. Optional: **Sound → beep** or **Light → light up display** to confirm alignment during testing

## Why it's built this way

- **Why a sensor instead of just driving a fixed distance?** Dead reckoning (drive X mm) carries forward every small error from earlier in the run — a slightly-off turn, a bit of wheel slip. The line is printed on the mat at a known spot, so stopping *on the line* throws all that accumulated error away and re-references the robot to the mat itself. This is why it's used as an alignment/reset point mid-run.
- **Why "reflected light" and not "color"?** Reflected light is a single fast number (how much light bounced back: high on white, low on black). Color detection is slower and can be fooled by lighting. For "am I over the dark line yet?" a brightness threshold is simpler and more reliable.
- **Why a threshold *between* the white and black readings?** The sensor never reads a clean 0 or 100 — white might read ~80, the black line ~12. Picking a value in the gap (e.g. 20) means "clearly darker than the mat" trips reliably without false triggers from shadows or printing variation. That's why the tuning step is "measure both, pick the middle."
- **Why approach *slowly* (step 3)?** The sensor is read a few dozen times a second. At high speed the robot travels several millimetres between reads and can roll past the line before a read lands on it, so it stops late and inconsistently. Slow approach keeps the stopping point tight.
- **Why an empty loop body?** The only job is "keep driving until the condition trips." `Start moving` sets the wheels going once; the loop just re-checks the sensor each tick. Putting a movement block inside the loop would restart the motors every tick and can stutter.
- **Why two sensors for a straight square-up (tuning tip)?** One sensor stops the robot at a point but doesn't fix its angle. Running the left and right motors independently until *each* side's sensor hits the line makes both front corners land on the line — so the robot ends up parallel to it, not just touching it.

**Translation note:** the Python version has an explicit `sleep_ms(10)` inside the loop to yield control between sensor checks — that's a Python/asyncio requirement, not a behavior you need to add in Word Blocks, since the loop block already re-checks its condition each tick on its own.

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
