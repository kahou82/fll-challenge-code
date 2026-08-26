# Template: Hold Mode for a Loaded Arm

Prevents a gravity-loaded attachment (a raised lift arm, a holding gate, anything gravity or a spring is pulling against) from sagging back down after the motor stops moving. The default stop behavior ("Brake") only resists motion for a moment — under sustained load, the arm can still creep. "Hold" actively fights that using the motor's own control loop, for as long as the motor is powered.

Use this any time an attachment needs to stay exactly where it was placed, after the move that placed it there is done — for example, holding a lifted object until a later step releases it.

## Blocks

Translated directly from `python-reference/arm_hold_mode.py`:

1. **Variables → Make a Variable**: `lift_position`, `lift_speed`
2. **Variables → set** `lift_position` to `90`, `lift_speed` to `40`
3. **Motion → Run [attachment motor] to position `[lift_position]` at speed `[lift_speed]`%** — on this block, find the **stop mode dropdown** and set it to **Hold** instead of the default Brake or Coast
4. *(...rest of the mission runs here, while the arm holds...)*
5. **Motion → Run [attachment motor] to position `0` at speed `[lift_speed]`%** — stop mode dropdown set to **Coast** this time, so it releases/falls freely instead of fighting its way down against Hold

That's the whole technique: steps 3 and 5 are the same block you're already using for any positioned move — Hold vs. Coast is just a dropdown choice on it, not a separate block.

## When NOT to use Hold

- On a motor that isn't fighting a load (e.g. driving on flat ground with nothing pulling it back) — Hold draws continuous current for no benefit, and adds unnecessary motor heat over a long match.
- Right before you want the arm to *release* and fall/swing freely (e.g. dropping a held object under gravity on purpose) — Hold will fight that; use Coast at that moment instead.
- For extended periods across an entire match — Hold keeps the motor actively working the whole time, which drains battery and can heat the motor. Only hold for as long as you actually need that position kept.

## Tuning tips

- Test how long you can hold under load before the motor noticeably heats up or the hub throttles it — for most FLL loads (well within motor torque spec) this isn't an issue, but very heavy attachments are worth checking.
- If the arm still creeps slightly even in Hold, the load may be exceeding the motor's holding torque — that's a mechanical/gearing problem (add a ratchet, gear down further), not something a code change fixes.

## Python reference

See `python-reference/arm_hold_mode.py`. Uses `motor.run_to_relative_position(port, position, velocity, stop=motor.HOLD)` — the same move function as always, with `stop=motor.HOLD` instead of the default `motor.BRAKE`.
