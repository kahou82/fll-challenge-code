# Template: Turn to Angle (Gyro)

Turns the robot to an exact heading using the gyro, which is far more repeatable than "turn for N degrees of motor rotation" because it doesn't drift with battery level or wheel slip.

## Blocks (in order)

1. **Motion → Reset yaw angle to 0** (do this once at the start of the whole mission run, not before every turn — turns should usually be relative to the original heading)
2. **Control → repeat until** `get yaw angle` is within tolerance of `target_angle`
   - Inside the loop:
     - `error = target_angle - yaw angle`
     - **Motion → Start moving with steering:**
       - steering = 100 if error > 0, else -100 (turn in place: one motor forward, one back — "start moving with steering 100/-100" does this)
       - speed = `turn_speed` (slow down as error gets small to avoid overshoot — optional: scale speed by error)
3. **Motion → Stop moving** once within tolerance

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
