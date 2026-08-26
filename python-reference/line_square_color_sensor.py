"""
Reference logic for programs/templates/line-square-color-sensor.md
Not meant to run standalone -- this documents the SPIKE Python API shape
so the block-code version can be planned/checked against it.
"""
from hub import port
import color_sensor
import motor_pair
import runloop

LINE_THRESHOLD = 20  # reflected light %, tune on your actual mat

async def square_up_on_line(approach_speed=18, line_threshold=LINE_THRESHOLD):
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=approach_speed)

    while color_sensor.reflection(port.E) >= line_threshold:
        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)


async def main():
    await square_up_on_line()

runloop.run(main())
