"""
Reference logic for programs/templates/wait-for-button.md
Not meant to run standalone -- this documents the SPIKE Python API shape
so the block-code version can be planned/checked against it.
"""
from hub import button, light_matrix, motion_sensor
import runloop

async def wait_for_launch():
    light_matrix.write("...")  # waiting pattern
    await button.wait_until_pressed(button.LEFT)
    light_matrix.write("GO")
    motion_sensor.reset_yaw(0)


async def run_mission():
    await wait_for_launch()
    # ... mission logic goes here ...
    light_matrix.clear()


async def main():
    await run_mission()

runloop.run(main())
