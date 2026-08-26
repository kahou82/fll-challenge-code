"""
Reference logic for programs/templates/drive-straight-gyro.md
Not meant to run standalone -- this documents the SPIKE Python API shape
so the block-code version can be planned/checked against it.
"""
from hub import motion_sensor, port
import motor_pair
import motor
import runloop
import math

WHEEL_DIAMETER_MM = 56  # measure your actual wheel and update this

async def drive_straight(target_distance_mm, base_speed=50, steering_gain=1.0):
    motion_sensor.reset_yaw(0)
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    wheel_circumference = math.pi * WHEEL_DIAMETER_MM
    target_degrees = (target_distance_mm / wheel_circumference) * 360

    motor.reset_relative_position(port.A, 0)

    while abs(motor.relative_position(port.A)) < target_degrees:
        angle = motion_sensor.tilt_angles()[0] / 10  # yaw in degrees
        correction = int(angle * steering_gain)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity=base_speed)

    motor_pair.stop(motor_pair.PAIR_1)


async def main():
    await drive_straight(target_distance_mm=500, base_speed=50, steering_gain=1.0)

runloop.run(main())
