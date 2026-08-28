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

## Why it's built this way

- **Why wait for a button at all (step 2)?** It splits "load the program" from "start the run." The driver can select the program, carefully place the robot against its alignment jig with both hands, get clear, *then* trigger it — instead of the robot lurching the instant the program loads.
- **Why the hub button and not the app's play button?** The play button is on the tablet, which is usually not within reach of the robot's start position, and tapping it can nudge the table. The hub button is right there on the robot on the table, so the same person who places the robot starts it, with consistent timing.
- **Why show text before and after (steps 1, 3, 6)?** The hub gives no other feedback. "Waiting" text confirms the program actually loaded and is armed; "GO" confirms the press registered; clearing the display at the end signals the run is complete, so the driver knows when to grab the robot without staring at it the whole time.
- **Why reset yaw *after* the button, not at the top of the program (step 4)?** The gyro drifts slightly while sitting idle, and the robot might get bumped during placement. Resetting at the moment the run actually begins — with the robot already in its final placed position — means every heading in the mission is measured from the true start pose.
- **Why "wait until pressed" and not "when button pressed" (a hat/event block)?** This template is a wrapper: the mission code needs to run *in sequence* right after the press, in a known order. `wait until` blocks the one running script at that line; an event block would start a separate parallel stack, which is harder to reason about for a linear mission run.

## Why button-start instead of just pressing the SPIKE app's "play" button

- The app's play button starts the program the instant you tap it on the tablet/phone, which is awkward when you also need both hands to place the robot on the mat.
- Hub-button start lets one person place the robot, then press the hub's button right there on the table — more consistent timing, and it's what most competitive teams do.

## Python reference

See `python-reference/wait_for_button.py` for the equivalent logic.
