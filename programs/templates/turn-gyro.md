# Template: Turn to Angle (Gyro)

Turns the robot to an exact heading using the gyro, which is far more repeatable than "turn for N degrees of motor rotation" because it doesn't drift with battery level or wheel slip.

## Blocks (in order)

Translated directly from `python-reference/turn_gyro.py`:

1. **Variables → Make a Variable**: `target_angle`, `turn_speed`, `tolerance`, `slow_speed`, `error`, `steering`, `speed`
2. **Motion → Reset yaw angle to 0** (do this once at the start of the whole mission run, not before every turn — turns should usually be relative to the original heading)
3. **Variables → set** `target_angle` to `90`, `turn_speed` to `35`, `tolerance` to `2`, `slow_speed` to `15` *(example values — match your mission)*
4. **Control → repeat until** `(absolute value of ([target_angle] − (Motion → yaw angle))) ≤ [tolerance]`
   - Inside the loop:
     5. **Variables → set `error` to** `([target_angle] − (Motion → yaw angle))`
     6. **Control → if/else**: if `[error] > 0` → **set `steering` to `100`**, else → **set `steering` to `-100`** *(turn in place: one motor forward, one back)*
     7. **Control → if/else**: if `(absolute value of [error]) > 20` → **set `speed` to `[turn_speed]`**, else → **set `speed` to `[slow_speed]`**
     8. **Motion → Start moving with steering `[steering]` at speed `[speed]`%**
9. **Motion → Stop moving** (loop exits once within tolerance)

## Why it's built this way

- **Why the gyro instead of "turn for N motor degrees"?** A motor-degree turn assumes a fixed relationship between wheel rotation and robot rotation. That relationship changes with battery voltage (more power = more wheel slip), tire grip, and how the weight is sitting on the wheels that run. The gyro measures how far the *robot* actually rotated, so the same code lands on 90° whether the battery is full or half-drained.
- **Why reset yaw once at the start of the run, not before each turn (step 2)?** Every turn's `target_angle` is measured from that one reset point, so headings stay absolute (e.g. "face 90° from start") and errors don't accumulate turn to turn. Resetting before each turn would make each one relative to wherever the last one happened to stop — including its error.
- **Why a `repeat until within tolerance` loop?** The robot can't stop on an exact value — it has momentum. The loop keeps nudging and re-checking until the heading is "close enough," which is what `tolerance` defines. Without a tolerance the loop could chase a value it can never hit exactly and never exit.
- **Why `error = target − yaw`, and steer by its sign (step 6)?** The sign of the error says which way to turn: positive means "not far enough, keep going the same way," negative means "overshot, come back." Recomputing it every tick means a small overshoot self-corrects instead of being permanent.
- **Why the two-speed setup — `turn_speed` far out, `slow_speed` near the target (step 7)?** Turning fast is good for saving match time but makes overshoot worse because of momentum. Dropping to a slow speed inside the last 20° lets the robot creep into tolerance and settle instead of oscillating back and forth past the target.
- **Why steering ±100 (turn in place)?** ±100 drives one wheel forward and one back, so the robot pivots around its own centre without translating. That keeps the turn from also shoving the robot sideways off its mark.

**Translation note:** the Python version computes the slow-down speed dynamically as `max(15, turn_speed // 2)`. Word Blocks' Operators category doesn't have a built-in "max" or integer-floor-divide block, so this simplifies to a separate tunable `slow_speed` variable instead — same intent (slow down near the target to avoid overshoot), simpler to build.

## Inputs to expose as variables

| Variable | Meaning | Typical starting value |
|---|---|---|
| `target_angle` | Desired heading in degrees, relative to reset point | mission-specific |
| `turn_speed` | Turning speed | 30–40 |
| `tolerance` | Acceptable error in degrees | 2 |

## Tuning tips

- If the robot overshoots and oscillates around the target, lower `turn_speed` or add a slow-down zone (e.g. half speed when error < 20°).
- Always reset yaw at the *same known starting position* on the mat at the start of a run — otherwise turns will be relative to the wrong heading.

## Python reference

See `python-reference/turn_gyro.py` for the equivalent logic.
