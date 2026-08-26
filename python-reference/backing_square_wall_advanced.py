"""
Reference logic for programs/templates/backing-square-wall-advanced.md
Not meant to run standalone -- this documents the SPIKE Python API shape
so the block-code version can be planned/checked against it.

Verified against the SPIKE App 3 Python API: motor_pair.move_for_degrees()
is awaitable and returns one of motor.READY / RUNNING / STALLED / CANCELED /
ERROR / DISCONNECTED when it completes. Commanding a move far larger than
the robot could ever need, then checking for motor.STALLED, lets the wall
itself decide when to stop -- no guessed fixed time needed.
"""
from hub import motion_sensor, port
import motor
import motor_pair
import runloop

BACK_SPEED = 25          # magnitude only; direction comes from the sign of degrees
OVERSHOOT_DEGREES = 3600  # far more than needed -- the stall should interrupt this early
SETTLE_TIME_MS = 200

async def backing_square_advanced():
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    status = await motor_pair.move_for_degrees(
        motor_pair.PAIR_1, -OVERSHOOT_DEGREES, 0, velocity=BACK_SPEED
    )

    if status != motor.STALLED:
        # Didn't detect a clean stall (e.g. finished the full overshoot
        # distance without hitting anything) -- something's off with
        # positioning or the stall isn't triggering reliably on this build.
        # Fall back to backing_square_wall.py's fixed-time version instead.
        pass

    await runloop.sleep_ms(SETTLE_TIME_MS)
    motion_sensor.reset_yaw(0)


async def main():
    await backing_square_advanced()
    # ... mission logic starts here, now with a known-good heading ...

runloop.run(main())
