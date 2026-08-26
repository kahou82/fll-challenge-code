# Template: Drive Straight (Gyro-Corrected)

Drives the robot in a straight line for a set distance, using the gyro to correct drift instead of relying on both motors spinning at exactly the same speed (they never do).

## Blocks (in order)

Translated directly from `python-reference/drive_straight_gyro.py`:

1. **Variables → Make a Variable**: `wheel_diameter_mm`, `target_distance_mm`, `base_speed`, `steering_gain`, `wheel_circumference`, `target_degrees`, `angle`, `correction`
2. **Motion → Reset yaw angle to 0**
3. **Variables → set `wheel_circumference` to** `(3.14159 × [wheel_diameter_mm])` *(Operators → multiply; no built-in π block, so use the literal)*
4. **Variables → set `target_degrees` to** `(([target_distance_mm] ÷ [wheel_circumference]) × 360)`
5. **Motion → Set left motor's position to 0**
6. **Control → repeat until** `[left motor position] ≥ [target_degrees]` *(simplification: dropped Python's `abs()` — this assumes forward-only movement)*
   - Inside the loop:
     7. **Variables → set `angle` to** `(Motion → yaw angle)` *(the block reporter already returns degrees — no `÷10` needed, that was only in the raw Python sensor call)*
     8. **Variables → set `correction` to** `(round([angle] × [steering_gain]))`
     9. **Motion → Start moving with steering `[correction]` at speed `[base_speed]`%**
10. **Motion → Stop moving**

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
