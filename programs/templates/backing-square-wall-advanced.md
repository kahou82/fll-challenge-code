# Template: Backing Square — Advanced (Motor Stall Detection)

Advanced version of `backing-square-wall.md` that stops backing up the instant the robot actually contacts the wall, using motor stall detection, instead of a fixed guessed time. This avoids grinding against the wall on runs where the robot started close to it, and doesn't need a "worst case" time buffer re-tuned if the robot's starting position in base changes.

Use this instead of the fixed-time version once you've confirmed your app/robot supports stall detection reliably (test it a few times in a row first — see Tuning tips).

## Blocks (in order)

Translated directly from `python-reference/backing_square_wall_advanced.py`:

**Translation note:** Python's version awaits `motor_pair.move_for_degrees(...)` and inspects the returned status for `motor.STALLED` — Word Blocks doesn't have that "await + check a return value" pattern. The practical block equivalent uses an explicit **"wait until is stalled?"** sensor reporter instead, which is functionally the same idea (stop when stall is detected) built a different way.

1. **Variables → Make a Variable**: `back_speed`, `settle_time_ms`
2. **Variables → set** `back_speed` to `25`, `settle_time_ms` to `200`
3. **Motion → Start moving**, direction = backward, speed = `[back_speed]`%, steering `0`
4. **Control → wait until** `([Motor A] is stalled?)` *(look for this under Motor sensor blocks — if it's not in your app version, use `backing-square-wall.md`'s fixed-time version instead)*
5. **Motion → Stop moving**
6. **Control → wait `[settle_time_ms]` milliseconds**
7. **Motion → Reset yaw angle to 0**

## Inputs to expose as variables

| Variable | Meaning | Typical starting value |
|---|---|---|
| `back_speed` | Backing speed while approaching the wall | 20–30 |
| `settle_time_ms` | Pause after stopping, before trusting the yaw reading | 200 |

## Why this is "advanced"

It relies on the hub detecting that a motor is being commanded to turn but physically can't — this needs real, sustained resistance (the wall) to trigger reliably. Very light robots, slippery mat surfaces, or soft/springy bumpers can sometimes fail to produce enough resistance for a clean stall reading, in which case the fixed-time version in `backing-square-wall.md` is the safer default.

## Tuning tips

- Test stall detection 5+ times in a row from different starting distances — it should trigger consistently, not randomly miss or trigger early.
- A completely rigid, flat contact surface on the back of the robot gives a cleaner stall than a springy or angled one.
- If stall detection is flaky on your build, don't fight it — fall back to the fixed-time version. A reliable simple technique beats a flaky fancy one at competition.

## Python reference

See `python-reference/backing_square_wall_advanced.py`. This uses the SPIKE Python API's `motor_pair.move_for_degrees(...)`, which is awaitable and returns one of `motor.READY / RUNNING / STALLED / CANCELED / ERROR / DISCONNECTED` when it finishes — the technique is to command a move far larger than needed and check for `motor.STALLED` as the result.
