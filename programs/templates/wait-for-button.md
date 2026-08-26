# Template: Start-on-Button Program Wrapper

Wraps a mission program so it doesn't start moving the instant it's launched — gives the driver time to place the robot and step back, and gives a consistent, repeatable start trigger.

## Blocks (in order)

Translated directly from `python-reference/wait_for_button.py`:

1. **Light → write text `"..."`** on the hub display *(the Python version scrolls literal text; if your app version's Light category doesn't have a "write text" block, substitute a "light up pixels" waiting icon instead — e.g. a single lit pixel or hourglass pattern)*
2. **Control → wait until** `(Sensor → left button is pressed?)`
3. **Light → write text `"GO"`**
4. **Motion → Reset yaw angle to 0** (reset gyro right at launch, at the actual starting position on the mat)
5. Run the actual mission logic (drive/turn/attachment blocks) — this is the `# ... mission logic goes here ...` comment in the Python
6. **Light → turn off display** (clears it, so the driver knows the run finished without needing to watch the robot the whole time)

## Why button-start instead of just pressing the SPIKE app's "play" button

- The app's play button starts the program the instant you tap it on the tablet/phone, which is awkward when you also need both hands to place the robot on the mat.
- Hub-button start lets one person place the robot, then press the hub's button right there on the table — more consistent timing, and it's what most competitive teams do.

## Python reference

See `python-reference/wait_for_button.py` for the equivalent logic.
