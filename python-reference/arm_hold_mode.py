"""
Reference logic for programs/templates/arm-hold-mode.md
Not meant to run standalone -- this documents the SPIKE Python API shape
so the block-code version can be planned/checked against it.

Verified against the SPIKE App 3 Python API: motor.run_to_relative_position()
takes a `stop` parameter with constants motor.COAST / BRAKE / HOLD / CONTINUE
/ SMART_COAST / SMART_BRAKE. HOLD actively maintains position under load
after the move finishes, unlike BRAKE which only resists briefly.
"""
from hub import port
import motor
import runloop

ARM_PORT = port.C
LIFT_POSITION = 90   # degrees from the zeroed position (see arm_zero_stall.py)
LIFT_SPEED = 40

async def lift_and_hold():
    await motor.run_to_relative_position(
        ARM_PORT, LIFT_POSITION, LIFT_SPEED, stop=motor.HOLD
    )
    # Arm actively holds LIFT_POSITION here, resisting gravity, until the
    # motor is given another command (e.g. to release/lower it later).


async def release():
    # Let it fall/swing freely instead of fighting it back down against Hold.
    await motor.run_to_relative_position(ARM_PORT, 0, LIFT_SPEED, stop=motor.COAST)


async def main():
    await lift_and_hold()
    # ... do the rest of the mission while the arm holds ...
    await release()

runloop.run(main())
