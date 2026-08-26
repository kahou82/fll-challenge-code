"""
Reference logic for programs/templates/backing-square-wall.md
Not meant to run standalone -- this documents the SPIKE Python API shape
so the block-code version can be planned/checked against it.

Uses a fixed backing time rather than stall detection, since stall
detection isn't exposed here in a way worth hard-coding -- check your
SPIKE App version's Motor sensor blocks if you want to use that instead.
"""
from hub import motion_sensor, port
import motor_pair
import runloop

BACK_SPEED = -25       # negative = backward; keep this low
BACK_TIME_MS = 1500     # tune: time to guarantee reaching the wall from base, +buffer
SETTLE_TIME_MS = 200    # let the robot stop bouncing before reading yaw

async def backing_square():
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    motor_pair.move(motor_pair.PAIR_1, 0, velocity=BACK_SPEED)
    await runloop.sleep_ms(BACK_TIME_MS)
    motor_pair.stop(motor_pair.PAIR_1)

    await runloop.sleep_ms(SETTLE_TIME_MS)
    motion_sensor.reset_yaw(0)


async def main():
    await backing_square()
    # ... mission logic starts here, now with a known-good heading ...

runloop.run(main())
