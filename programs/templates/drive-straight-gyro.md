# Template: Drive Straight (Gyro-Corrected)

Drives the robot in a straight line for a set distance, using the gyro to correct drift instead of relying on both motors spinning at exactly the same speed (they never do).

## Blocks (in order)

1. **Motion → Move → Start moving with steering** is NOT used here — instead build it manually for gyro correction:
2. **Motion → Reset yaw angle to 0**
3. **My Blocks / loop:** `repeat until` distance traveled ≥ target
   - Inside the loop:
     - `angle = get yaw angle`
     - `correction = angle × steering_gain` (start with gain = 1)
     - **Motion → Start moving with steering (correction)**, speed = `base_speed`
4. When distance reached: **Motion → Stop moving**

## Inputs to expose as variables

| Variable | Meaning | Typical starting value |
|---|---|---|
| `target_distance_mm` | How far to drive | mission-specific |
| `base_speed` | Drive speed, -100 to 100 | 40–50 for accuracy, 70+ for speed runs |
| `steering_gain` | How hard to correct drift | 1 (increase if robot still drifts, decrease if it oscillates/wobbles) |

## Tuning tips

- If the robot curves consistently one direction even with correction on, check that both drive motors are actually in the ports you think they are, and that wheels aren't slipping.
- Higher `steering_gain` fixes drift faster but can cause wobble — increase in small steps (0.5 at a time).
- Distance-to-degrees: SPIKE motor "move for degrees" needs a wheel-diameter calculation. Measure wheel diameter (mm), then:
  `degrees = (target_distance_mm / (π × wheel_diameter_mm)) × 360`

## Python reference

See `python-reference/drive_straight_gyro.py` for the equivalent logic.
