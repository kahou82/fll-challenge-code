# M10 — Fragile Microhabitats

**Model(s):** spider habitat, snail habitat
**Location:** see [field-map.md](../field-map.md)

## Objective
Move the robot through the area **without** disturbing the tiny habitats. This is a "don't touch" mission — points for leaving things alone.

## Scoring
- The spider habitat is in its original starting position — **10**
- The snail habitat is in its original starting position — **10**

## Constraints & gotchas
- These points are **free at match start** and are *lost* if the robot nudges a habitat. Any run that drives near here risks them.
- Effectively a routing constraint: keep attachments and the chassis clear of both habitats, or approach from a direction that can't clip them.

## Setup / starting state
Both habitats in place. Goal is to keep them there.

## Our approach
- templates: [../../../programs/templates/drive-straight-gyro.md](../../../programs/templates/drive-straight-gyro.md) / [turn-gyro.md](../../../programs/templates/turn-gyro.md) — plan paths that avoid this zone
- attachment: n/a (avoidance)
- launch area / run: consider on every run that passes nearby

## Status
not started

## Reference
Rulebook p.11 · missions video @ TBD
