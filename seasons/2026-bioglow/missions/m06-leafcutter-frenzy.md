# M06 — Leafcutter Frenzy

**Model(s):** nest, ant, leaf fragments
**Location:** shared area with M07 (Humongous Fungus) — see [field-map.md](../field-map.md)

## Objective
Guide the ant back to its nest while keeping the collected leaf fragments contained — move too fast and the fragments scatter.

## Scoring
- The ant is touching the nest, **and** the leaf fragments are contained within the nest — **10 each fragment** ⚠️ confirm fragment count from the missions video

## Constraints & gotchas
- Both parts of the condition must hold at end of match: ant touching nest **and** fragments in.
- "Move too quickly, and you may scatter the leaves" — this is a physical/tuning warning: a slow, smooth approach keeps fragments together. Good candidate for a low-speed gyro drive.

## Setup / starting state
Ant away from nest, fragments loaded with/near the ant.

## Our approach
- templates: [../../../programs/templates/drive-straight-gyro.md](../../../programs/templates/drive-straight-gyro.md) at low speed
- attachment: cradle that keeps fragments contained during the move
- launch area / run: TBD

## Status
not started

## Reference
Rulebook p.10 · missions video @ TBD
