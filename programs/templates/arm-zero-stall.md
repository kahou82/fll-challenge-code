# Template: Zero an Attachment Arm Against a Hard Stop (Stall)

Establishes a reliable "zero" position for an attachment arm at the start of a run, the same idea as backing-square but for an arm motor instead of the drive base. Run the arm into a physical end-stop (a mechanical limit built into the attachment) until it stalls, then treat that position as 0. Every later move (`run to position X`) is then accurate for the rest of the run, regardless of small drift from a previous mission.

Do this once per attachment, right after backing-square, before the mission drive starts.

## Blocks (in order)

Translated directly from `python-reference/arm_zero_stall.py`:

**Translation note:** same as the advanced backing-square template — Python checks the return status of an awaited move for `motor.STALLED`; the block equivalent is an explicit **"wait until is stalled?"** sensor reporter.

1. **Variables → Make a Variable**: `arm_speed`, `settle_time_ms`
2. **Variables → set** `arm_speed` to `25`, `settle_time_ms` to `150`
3. **Motion → Start [attachment motor] moving** toward the end-stop, speed = `[arm_speed]`%
4. **Control → wait until** `([attachment motor] is stalled?)` *(if this block isn't available in your app version, substitute a fixed **wait `X` milliseconds** long enough to guarantee contact, similar to `backing-square-wall.md`'s fallback)*
5. **Motion → Stop motor**
6. **Control → wait `[settle_time_ms]` milliseconds** to let it stop bouncing off the stop
7. **Motion → Set [attachment motor]'s position to 0** (the block equivalent of the Python `reset_relative_position` call — look for it under Motion or Motor sensor blocks; exact wording varies by app version)

From here on, use **"run motor to position X"** blocks for this attachment — they're now measured from this zero, so they land in the same real-world spot every time.

## Inputs to expose as variables

| Variable | Meaning | Typical starting value |
|---|---|---|
| `arm_speed` | Speed while driving into the end-stop | 20–30 (low — this is a controlled bump against your own mechanism) |
| `settle_time_ms` | Pause after stopping, before zeroing | 150 |

## Tuning tips

- The end-stop should be a hard mechanical limit (a tab, a wall in the gearbox, the arm hitting the robot frame) — not something soft/springy, or the stall won't be clean.
- Don't use high speed here — you're intentionally jamming a motor against a mechanical limit every single run; keep it gentle to avoid stripping gears over a season.
- If this attachment moves under load when the robot is placed in base (e.g. gravity pulling it down before the program starts), zero it *before* backing-square if that changes the robot's footprint/weight distribution against the wall — otherwise order doesn't usually matter.

## Python reference

See `python-reference/arm_zero_stall.py`. Uses `motor.run_for_degrees(port, degrees, velocity)` (awaited, checked for `motor.STALLED`) followed by `motor.reset_relative_position(port, 0)`.
