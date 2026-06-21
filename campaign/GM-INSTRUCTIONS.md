# Game Master — Live Mode

Main menu / hub: the projects hub at `../` (this dashboard lives at `/campaign/`).
Full rules: `./AI-DUNGEON-MASTER.md` in this folder (and the Notion hub if connected).

**Live loop:** after any state change, overwrite `./state.json` in this folder and
commit + push (short message, e.g. `turn: ...`); the dashboard refreshes ~1 min. Keep
the human-readable checkpoint in Notion.

Schema + map characters: see `./AI-DUNGEON-MASTER.md` section 14.
