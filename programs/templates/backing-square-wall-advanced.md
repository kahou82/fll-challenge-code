# Template: Backing Square — Advanced (Motor Stall Detection)

Advanced version of `backing-square-wall.md` that stops backing up the instant the robot actually contacts the wall, using motor stall detection, instead of a fixed guessed time. This avoids grinding against the wall on runs where the robot started close to it, and doesn't need a "worst case" time buffer re-tuned if the robot's starting position in base changes.

Use this instead of the fixed-time version once you've confirmed your app/robot supports stall detection reliably (test it a few times in a row first — see Tuning tips).

## Blocks (in order)

1. **Motion → Reset yaw angle to 0** is done *after* squaring (step 5), not here — don't reset yet.
2. **Motion → Move [motor pair] for a large number of degrees** (backward, steering 0) at `back_speed` — pick a degree count far larger than the robot could ever actually need to travel to reach the wall from base (it will never complete this move normally; it's a target the stall will interrupt).
   - If your Word Blocks palette has a **"wait until [Motor] is stalled?"** sensor block, use that instead: **Motion → Start moving** backward at `back_speed`, then **Control → wait until → [Motor A] is stalled?**
3. **Motion → Stop moving**
4. **Control → wait** ~200 ms (`settle_time_ms`) to let the robot stop bouncing
5. **Motion → Reset yaw angle to 0**

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
