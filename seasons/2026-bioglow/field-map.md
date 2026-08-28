# BIOGLOW — Field Map & Table

Sources: [Field Setup Reference Guide](links.md), [Table Building Instructions](links.md), [Field Setup Video](links.md). The setup guide is diagram-only, so exact per-model coordinates below are **to be measured on our table** — the guide gives regions, not numbers.

## Mat & field dimensions

| | Inches | mm |
|---|---|---|
| Mat printed area | ~91⅞ × 44½ | ~2332 × 1130 |
| Inside wall-to-wall length **L** | 93 ± ⅛ | 2362 ± 3 |
| Inside wall-to-wall width **W** | 45 ± ⅛ | 1143 ± 3 |
| Border wall height **H** (all walls equal) | 2½ min – 4 max | 64–102 |
| Border wall thickness | ≤ 2.0 | ≤ 51 |
| Gap at "top" short wall after mat is placed | ~0.35 | ~9 |
| Equipment margin each side of mat | ~7.15 × 45 | ~181 × 1143 |

Expect regional variation at events: wall height anywhere in the 2.5–4" range, thickness up to 2". Design attachments that reach over the wall to tolerate this.

## Coordinate convention (ours)

Not defined by FIRST — this is what we use in mission files and programs so everyone means the same thing:

- **Origin (0, 0):** bottom-left inside corner of the field (where the left long wall meets the bottom short wall — the wall the mat is slid against).
- **+X** → toward the right wall (0 to ~1143 mm).
- **+Y** → toward the far / "top" wall, away from Home (0 to ~2362 mm).
- **Units:** mm for positions and distances. 1 LEGO stud = 8 mm; 1 module = 8 mm.
- **Headings:** degrees, 0 = facing +Y (down the table, away from Home), clockwise positive — matches the SPIKE gyro after a reset while pointing down-table.

Base/Home is along the **Y = 0** edge.

## Home & launch areas

- **Home** runs along the bottom edge, split into two sections: **Left Launch Area** and **Right Launch Area**.
- The robot + anything it will move must fit **completely inside one launch area** at launch.
- Fitting *all* equipment into a single launch area under 305 mm tall = **20 pt inspection bonus**.
- Returning robots may extend past the Home walls without penalty.
- One sheet of notebook paper per Home area is allowed for program notes (not equipment).

> TODO: measure and record each launch area's width and depth from our table.

## Interchangeable dock system (Missions 13–15)

Three docks, secured with Dual Lock: **mine**, **city**, **farm**. Before each match we place the M13 / M14 / M15 models onto docks in whatever arrangement we choose.

- M15 "Environmental Bonus" (+10) is earned only if the model on a dock matches that dock's greatest ecological need:
  - **mine dock** → nesting canopy
  - **city dock** → garden skylight
  - **farm dock** → compost hatch

> TODO: record dock positions (X, Y, heading) once measured. See [strategy.md](strategy.md) for which model goes where.

## Mission model placement

Fill in as measured. Region column is from the setup guide's diagram; coordinates are ours to measure.

| # | Model(s) | Region | Center (X, Y) mm | Heading | Notes |
|---|---|---|---|---|---|
| 01 | Drone Survey — drone, stalk, LiDAR map, scan marker | far side | | | |
| 02 | Exploding Seeds — seed pod, seeds, stalk | | | | green tube orientation may vary at events |
| 03 | Flip the Rock — rock, research flag | | | | |
| 04 | Lucky Leaves — nest, 2 leaves, katydid | | | | **katydid + leaf positions randomized by the ref at match start** |
| 05 | Reaching Roots — plant root (extends across the forest boundary) | | | | spans toward opponent side |
| 06 | Leafcutter Frenzy — nest, ant, leaf fragments | shared w/ M07 | | | |
| 07 | Humongous Fungus — mycelium, plant root | shared w/ M06 | | | cross-table interaction with opponent |
| 08 | Tangled — vine, tree | shared w/ M09 | | | |
| 09 | Research Platform — platform, camera trap, seed | shared w/ M08 | | | |
| 10 | Fragile Microhabitats — spider habitat, snail habitat | | | | score = leaving them undisturbed |
| 11 | Window to the Past — root cover | | | | |
| 12 | Forest Elder — cane, support tie, post | | | | |
| 13 | Keystone Species — restoration platform, young trees | dock | | | team-built keystone model |
| 14 | Seeds of Renewal — replantation station, seeds | dock | | | |
| 15 | Biocentric Architecture — nesting canopy, garden skylight, compost hatch | dock | | | |

## Build your own practice table

From the official [Table Building Instructions](https://firstinspires.blob.core.windows.net/fll/challenge/2026-27/fll-challenge-bioglow-table-building-instructions.pdf). Basic woodworking; ~half a day.

### Cut list

| Part | Material | Size | Qty |
|---|---|---|---|
| A — base board | Sanded plywood, smooth face up, min ⅜" (10 mm) thick | 96 × 48" (2438 × 1219 mm) | 1 |
| B — long walls | 2×3 lumber (actual 1.5 × 2.5") | 96" (2438 mm) | 2 |
| C — short walls | 2×3 lumber (actual 1.5 × 2.5") | 45" (1143 mm) | 2 |
| — | Wood screws | 2.5" (64 mm) | ~1 lb |
| — | Matte black paint | walls only | ~1 qt |

Lumber to buy: **3 × 8-foot 2×3**. Two are the long walls as-is; the third cuts into both 45" short walls.

### Assembly

1. Lay the long walls (B) along the **full 96" length** of the two long plywood edges, flush to the ends, sitting **on top of** the plywood.
2. Drop the short walls (C, 45") **between** the long walls at each end.
3. Screw everything down, then verify with a tape: **inside L = 93 ± ⅛"**, **inside W = 45 ± ⅛"**. The geometry checks itself — 48" − 2 × 1.5" = 45" wide; 96" − 2 × 1.5" = 93" long.
4. Paint the wall inner faces matte black. Leave the plywood floor bare and smooth (sand/vacuum any bumps).
5. Support the table at **24–36" (610–915 mm)** off the floor — sawhorses or banquet tables.

### Mat placement

- Slide the mat tight against **one short wall** ("bottom" = Home edge), centered left-to-right.
- Leave the **~9 mm gap at the opposite short wall** — that's where a second table butts for head-to-head.
- Tape edges with thin matte-black gaffer tape; keep the mat's printed color border at least partly visible.

### Notes

- **2×3 hard to find?** 2×4 on edge works: 1.5" thick (≤ 2" ✓), 3.5" tall (within 2.5–4" ✓); inside-dimension math unchanged. Never lay a 2×4 flat — 3.5" thick exceeds the 2" wall limit.
- A 2×3 wall is the **minimum** legal height (2.5"). If you later add a second table for head-to-head, both must have the **same** wall height and the same 3.0–4.0" (76–102 mm) span between wall pairs.
- Don't attach anything to the tops of the border walls (not allowed at events unless all teams are notified).
