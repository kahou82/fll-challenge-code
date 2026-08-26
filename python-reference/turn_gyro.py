"""
Reference logic for programs/templates/turn-gyro.md
Not meant to run standalone -- this documents the SPIKE Python API shape
so the block-code version can be planned/checked against it.
"""
from hub import motion_sensor, port
import motor_pair
import runloop

async def turn_to_angle(target_angle, turn_speed=35, tolerance=2):
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    while True:
        yaw = motion_sensor.tilt_angles()[0] / 10
        error = target_angle - yaw
        if abs(error) <= tolerance:
            break
        steering = 100 if error > 0 else -100
        speed = turn_speed if abs(error) > 20 else max(15, turn_speed // 2)
        motor_pair.move(motor_pair.PAIR_1, steering, velocity=speed)

    motor_pair.stop(motor_pair.PAIR_1)


async def main():
    motion_sensor.reset_yaw(0)
    await turn_to_angle(target_angle=90, turn_speed=35, tolerance=2)

runloop.run(main())
