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

## Why it's built this way

- **Why zero the arm at all?** "Run to position X" is measured from wherever the motor's counter happened to be when the program started. After a previous mission, a hand-nudge in base, or the arm sagging under gravity, that starting count is unknown — so "position 90" could be anywhere. Re-zeroing at the start of each run makes every later "run to position" land in the same real place.
- **Why drive into a hard stop instead of just "set position to 0" where it sits?** Setting 0 in place only works if the arm is already in a known spot, which is the thing we can't guarantee. A physical end-stop *is* a known spot — the arm can only be in one place when it's jammed against it — so running to the stop first gives the reset something real to reference.
- **Why detect the stop with a stall (step 4)?** Same reason as the advanced backing-square: the hub can tell the motor is commanded to move but physically can't. That's a reliable "I've reached the mechanical limit" signal without needing a separate switch or sensor on the attachment.
- **Why low `arm_speed`?** This move deliberately jams a motor against a hard limit on *every single run*. Fast means a hard impact into your own gear train every time — over a season that strips gears or pops axles. Slow is a gentle bump that still stalls cleanly.
- **Why the settle wait before zeroing (step 6)?** The arm springs back slightly off the stop after the motor cuts. Pausing lets it come to rest against the stop so 0 is set at the true limit position, not mid-bounce.
- **Why "right after backing-square, before the mission drive"?** It's part of putting the *whole* robot into a known state at the start — drive base squared by the wall, gyro zeroed, each arm zeroed against its stop. Do it before driving so the arm is at a known height for the first mission and isn't dragging or catching on the way there.
- **Why this mirrors backing-square:** both replace an unknown starting reference (hand placement / leftover motor count) with a physical one the robot can find on its own (the border wall / the end-stop). Same idea, one for the drive base and one for an arm.

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
