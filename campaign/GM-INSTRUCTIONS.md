# Game Master — Live Mode

Main menu / hub: the projects hub at `../` (this dashboard lives at `/campaign/`).
Full rules: `./AI-DUNGEON-MASTER.md` in this folder (and the Notion hub if connected).

**Live loop:** after any state change, overwrite `./state.json` in this folder and
commit + push (short message, e.g. `turn: ...`); the dashboard refreshes ~1 min. Keep
the human-readable checkpoint in Notion.

Schema + map characters: see `./AI-DUNGEON-MASTER.md` section 14.

## Self-improvement loop (run on every save)
On each save / end of session, run the **After-Action Review** in `./SELF-IMPROVEMENT.md`
and append a dated entry to `./LEARNINGS.md`: what worked, where the rules/logic were
ambiguous or diverged, and concrete proposed refinements. When the player says
`apply learnings`, fold the accepted items into canon and mark them Done. The engine should
get a little better every time it is played.

## Quick engine test
For a ~5-minute sanity check that the engine + branching work end-to-end, run
`./adventures/the-crossroads-test.md` ("The Ember Key" — a pure decision tree).
