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

## Why it's built this way

- **What the three stop modes actually do:** *Coast* cuts power and lets the motor spin freely. *Brake* shorts the motor terminals so it resists being turned, but only passively — a steady pull (gravity on a raised arm) slowly wins and the arm creeps down. *Hold* keeps the control loop running after the move finishes: it watches the position and drives the motor back whenever it slips, like Drive-Straight's correction loop but for "stay put" instead of "stay straight."
- **Why this matters for a loaded arm:** the arm has to stay exactly where the earlier move placed it while the rest of the mission runs. Brake is "good enough" only for light or balanced loads; anything gravity or a spring is fighting needs the active correction that Hold provides.
- **Why Hold is a dropdown, not extra blocks:** it's not a separate behavior you program — it's just telling the *existing* "run to position" block what to do once it arrives. Keeping it on the same block means the holding position is always exactly the position you just commanded, with nothing to get out of sync.
- **Why step 5 deliberately switches to Coast:** when you *want* the arm to drop or swing free (releasing an object), Hold would fight the fall and stall the motor against gravity. Coast removes all resistance so the arm moves under gravity as intended. The choice of mode always follows intent: "keep this exactly" → Hold, "let this go" → Coast.
- **Why not just Hold everything all match?** Hold burns current continuously to fight the load, which heats the motor and drains the battery. It's a tool for the specific window where a position must be kept, not a default — hence the "When NOT to use" list below.
- **Why `lift_position` / `lift_speed` are variables:** the same arm gets moved to the same place from several missions; naming the values once means a re-tune (arm geometry changed, load changed) is one edit, not a hunt through every mission program.

## When NOT to use Hold

- On a motor that isn't fighting a load (e.g. driving on flat ground with nothing pulling it back) — Hold draws continuous current for no benefit, and adds unnecessary motor heat over a long match.
- Right before you want the arm to *release* and fall/swing freely (e.g. dropping a held object under gravity on purpose) — Hold will fight that; use Coast at that moment instead.
- For extended periods across an entire match — Hold keeps the motor actively working the whole time, which drains battery and can heat the motor. Only hold for as long as you actually need that position kept.

## Tuning tips

- Test how long you can hold under load before the motor noticeably heats up or the hub throttles it — for most FLL loads (well within motor torque spec) this isn't an issue, but very heavy attachments are worth checking.
- If the arm still creeps slightly even in Hold, the load may be exceeding the motor's holding torque — that's a mechanical/gearing problem (add a ratchet, gear down further), not something a code change fixes.

## Python reference

See `python-reference/arm_hold_mode.py`. Uses `motor.run_to_relative_position(port, position, velocity, stop=motor.HOLD)` — the same move function as always, with `stop=motor.HOLD` instead of the default `motor.BRAKE`.
