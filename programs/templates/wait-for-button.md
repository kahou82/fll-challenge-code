# Template: Start-on-Button Program Wrapper

Wraps a mission program so it doesn't start moving the instant it's launched — gives the driver time to place the robot and step back, and gives a consistent, repeatable start trigger.

## Blocks (in order)

1. **Light → light up hub display** with a "waiting" pattern (e.g. a single lit pixel or hourglass icon), so it's visually obvious the robot is idle
2. **Control → wait until** hub's left button (or right button) is pressed
3. **Light → light up hub display** with a "go" pattern (e.g. full display lit, or a checkmark), and optionally a short beep
4. **Motion → Reset yaw angle to 0** (reset gyro right at launch, at the actual starting position on the mat)
5. Run the actual mission logic (drive/turn/attachment blocks)
6. At the end: **Light → light up hub display** with a "done" pattern (e.g. all off, or a distinct color) so the driver knows it finished without needing to watch the robot the whole time

## Why button-start instead of just pressing the SPIKE app's "play" button

- The app's play button starts the program the instant you tap it on the tablet/phone, which is awkward when you also need both hands to place the robot on the mat.
- Hub-button start lets one person place the robot, then press the hub's button right there on the table — more consistent timing, and it's what most competitive teams do.

## Python reference

See `python-reference/wait_for_button.py` for the equivalent logic.
