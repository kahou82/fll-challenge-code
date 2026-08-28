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

## Why it's built this way

- **Why the gyro instead of just "drive forward"?** The two drive motors are never perfectly matched — tiny differences in friction, gearing, tire wear, and battery load make one side push slightly harder, so "full power to both" curves. The gyro measures the actual heading the robot is pointing and lets the code push back, so straightness comes from a real measurement, not from hoping the hardware is symmetric.
- **Why reset yaw to 0 first (step 2)?** The correction math steers toward "yaw = 0". Resetting at the start makes 0 mean "the direction I'm facing right now," so the robot holds *this* line rather than some leftover heading from an earlier move.
- **Why measure distance with the motor, not the gyro?** The gyro only knows rotation, not how far you've travelled. The left motor's rotation counter is the odometer. Converting the target distance into motor degrees up front (steps 3–4) lets the loop exit on "have I gone far enough?" using `wheel_circumference = π × diameter`, then `degrees = distance ÷ circumference × 360`.
- **Why `correction = angle × steering_gain` (proportional control)?** A little drift gets a little steering; a lot of drift gets a lot. A fixed correction would over-fight small errors (wobble) and under-fight big ones (slow to recover). Multiplying by the error scales the response to how wrong we currently are — this is the "P" in a PID controller.
- **Why a loop that re-steers every tick instead of one big move?** Drift builds up gradually during the drive. Checking and correcting many times per second keeps the error small the whole way, instead of discovering at the end that the robot wandered.
- **Why `round()` the correction?** The steering input takes a whole number; rounding avoids throwing away the fractional part inconsistently and keeps small corrections from being dropped to zero.

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
