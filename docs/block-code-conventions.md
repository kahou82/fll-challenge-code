# Block Code Conventions

Simple rules to keep everyone's SPIKE Prime projects consistent and easy to hand off.

## Ports (pick once, keep consistent across missions if possible)

| Device | Port |
|---|---|
| Left drive motor | A |
| Right drive motor | B |
| Attachment motor 1 | C |
| Attachment motor 2 | D |
| Color/light sensor | E |
| Distance sensor | F |

Update this table to match your actual robot build, then keep it consistent so templates can be reused without rewiring blocks every time.

## Naming programs

`missionN-shortname.llsp3`, e.g. `mission1-cargo-drop.llsp3`, `mission5-solar-panel.llsp3`.

## Structure every mission program should have

1. **Reset** — reset yaw angle (gyro) and any motor position/timers at the very start.
2. **Drive to mission** — using drive-straight or turn templates.
3. **Do the mission** — attachment motor moves, sensor waits, etc.
4. **Return / reset** — drive back or position for the next run, so the next mission program can start from a known state.

## Comment blocks

Use the SPIKE app's comment blocks liberally to note *why* a number was chosen (e.g. "600mm = distance from base to mission table edge, measured 2026-08-20") — future you (or a teammate) won't remember why `587` was the magic number.

## Testing checklist before checking in an export

- [ ] Runs 3 times in a row with the same result
- [ ] Works starting from the actual competition mat position, not just the practice table
- [ ] Battery was reasonably charged during testing (behavior changes on low battery)
