"""
Reference logic for programs/templates/arm-zero-stall.md
Not meant to run standalone -- this documents the SPIKE Python API shape
so the block-code version can be planned/checked against it.

Verified against the SPIKE App 3 Python API: motor.run_for_degrees() is
awaitable and returns one of motor.READY / RUNNING / STALLED / CANCELED /
ERROR / DISCONNECTED. Driving into a hard mechanical stop and checking for
STALLED gives a repeatable zero point regardless of where the arm was left
after the previous mission.
"""
from hub import port
import motor
import runloop

ARM_PORT = port.C
ARM_SPEED = 25            # magnitude only; direction from sign of degrees
OVERSHOOT_DEGREES = 720    # far more than the arm could ever need to travel
SETTLE_TIME_MS = 150

async def zero_arm():
    status = await motor.run_for_degrees(ARM_PORT, -OVERSHOOT_DEGREES, ARM_SPEED)

    if status != motor.STALLED:
        # Didn't hit a clean stall -- check the end-stop is a hard limit
        # and OVERSHOOT_DEGREES is large enough for the arm's full range.
        pass

    await runloop.sleep_ms(SETTLE_TIME_MS)
    motor.reset_relative_position(ARM_PORT, 0)


async def main():
    await zero_arm()
    # ... from here, motor.run_to_relative_position(ARM_PORT, position, velocity)
    # moves are all measured from this zero point ...

runloop.run(main())
