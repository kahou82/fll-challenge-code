# Template: Backing Square (Align at Start Using the Border Wall)

Squares the robot's heading and position at the start of a run by driving backward into the field's raised border wall, instead of relying on a human placing the robot perfectly by eye. The wall becomes the reference, not your hands — this is why it stays reliable even on a different table at competition (see note at the bottom).

Use this **at the very start of a mission run**, right after the robot is placed roughly in position in base and before the driver walks away.

## Blocks (in order)

Translated directly from `python-reference/backing_square_wall.py` (the fixed-time version — see `backing-square-wall-advanced.md` for the stall-detection version):

1. **Variables → Make a Variable**: `back_speed`, `back_time_ms`, `settle_time_ms`
2. **Variables → set** `back_speed` to `25`, `back_time_ms` to `1500`, `settle_time_ms` to `200`
3. **Motion → Start moving**, direction = backward (toward the wall), speed = `[back_speed]`%, steering `0`
4. **Control → wait `[back_time_ms]` milliseconds** — long enough that the robot is guaranteed to reach the wall even from the farthest likely starting spot, but not so long it grinds against the wall
5. **Motion → Stop moving**
6. **Control → wait `[settle_time_ms]` milliseconds** (let the robot settle/stop bouncing off the wall)
7. **Motion → Reset yaw angle to 0** — this is the moment the "true" heading gets locked in, using the wall's angle, not wherever the robot happened to be pointed
8. (Optional) **Motion → move forward** a short fixed distance to clear the wall/border before starting the actual mission drive, if your first movement needs clearance

## Why it's built this way

- **Why square against the wall instead of trusting hand placement?** A person eyeballing the robot into base is accurate to maybe a few degrees, and that error multiplies over a long drive into a big miss at the mission. The border wall is a straight, fixed edge — driving flat into it forces the robot's back edge parallel to the wall, giving a mechanical alignment that doesn't depend on the driver's aim.
- **Why *back* into the wall rather than drive forward into something?** Base is against the border, so the wall is already right behind the robot in most starting positions — no separate jig needed. Backing also keeps front-mounted attachments away from the collision.
- **Why the yaw reset happens at step 7, after contact and settling?** That's the whole point of the maneuver: the reset defines "straight ahead," and we want it defined by the wall's angle, not by however the robot was pointing when placed. Reset any earlier and you've just locked in the placement error you were trying to remove.
- **Why a settle wait between stopping and resetting (step 6)?** Hitting the wall makes the robot rock/bounce slightly, and the gyro reads that motion as heading change. Pausing ~200 ms lets it come to rest so the reset captures the true resting heading, not a mid-bounce value.
- **Why a fixed time (step 4) and not "drive exactly to the wall"?** The code doesn't know how far the robot is from the wall — that varies with placement. So it drives backward long enough to reach the wall from the *worst-case* farthest start, then keeps gently pushing. Once against the wall the wheels just slip; the extra time is harmless as long as speed is low. The advanced template swaps this guess for stall detection.
- **Why low `back_speed`?** A fast slam bounces the robot off the wall (undoing the square) and stresses anything hanging off the back. Slow contact stays planted against the wall.
- **Why this survives moving to a different table:** nothing here assumes the wall is at a known coordinate — it drives until it hits whatever wall is actually present and references off that contact. Only the *downstream* distances (wall to mission) need re-checking at competition.

## Inputs to expose as variables

| Variable | Meaning | Typical starting value |
|---|---|---|
| `back_speed` | Backing speed while approaching the wall | 20–30 (low — protects attachments and gears) |
| `back_time_ms` | Fallback fixed backing time if not using stall detection | test empirically: time from farthest realistic base position to the wall, +30% buffer |

## Tuning tips

- Make sure whatever touches the wall first is a rigid, straight edge spanning as much of the robot's back width as possible — if only one corner or an attachment arm hits the wall first, the robot will square up crooked instead of straight.
- Keep `back_speed` low. A hard, fast backing motion can bounce the robot off the wall (undoing the squaring) or stress attachments hanging off the back.
- If using stall detection, test it a few times in a row — some motors report "stalled" a beat late or early depending on gearing; fixed-time is simpler and fine if stall detection is fussy on your build.

## Does this break if the practice table's wall isn't identical to the competition table's wall?

No — that's the point of this technique. It doesn't assume the wall is in a specific known position; it drives until it *finds* whatever wall is actually there, then zeros out from that contact point. So it works the same way on your school table and the competition table. What you *do* still need to re-tune at competition (regardless of squaring technique) is everything downstream: the distances/degrees driven after leaving the wall to reach each mission, since mat printing and table build can vary slightly table to table. Use the official practice rounds at competition to re-check those numbers.

## Python reference

See `python-reference/backing_square_wall.py` for the equivalent logic (fixed-time version, since stall detection isn't exposed in a way worth hard-coding here — check your SPIKE App version's blocks if you want to use it instead).
