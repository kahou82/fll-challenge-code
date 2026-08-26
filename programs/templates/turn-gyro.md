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
