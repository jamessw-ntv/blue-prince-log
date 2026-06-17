# Log from a normal Claude.ai chat (the fast way)

A plain Claude.ai chat starts instantly (no Claude Code container spin-up). To let it
write to this repo, do this **once**, then logging is fast forever after.

## One-time setup

1. **Add the GitHub connector** (this is what lets a normal chat commit):
   Claude.ai → **Settings → Connectors → Add custom connector** → add the official
   GitHub MCP server (`https://api.githubcopilot.com/mcp/`) → authorize GitHub with
   access to **`jamessw-ntv/blue-prince-log`** and **Contents: read & write**.
   Guide: <https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-claude.md>
   (Custom connectors need a paid plan. The built-in GitHub integration is read-only.)
2. **Create a Project** in Claude.ai (e.g. "Blue Prince Log"), enable the GitHub
   connector on it, and paste the block below into the Project's **custom instructions**.

After that: open a chat in that Project, say *"Log: …"* (or list several things), it
commits to `main`, and the viewer updates in a few seconds. You'll approve the write.

## Paste this into the Project's custom instructions

```
You maintain a spoiler-free Blue Prince notepad in the GitHub repo
jamessw-ntv/blue-prince-log (branch main) via the GitHub connector.
data.json holds the log; index.html is a read-only viewer that renders it.

FIRST, decide what I'm asking for, then act:
1. LOGGING (default for anything about the game) — "the Den does X", "found
   code 4-7-2", "add these rooms", or a photo. -> Edit data.json, commit to
   main. Viewer updates in seconds.
2. FEATURE / VIEWER CHANGE — about the tool itself: "add a column", "change
   the colours", "make notes filterable", "the table should...". -> Edit
   index.html (and maybe README.md), NOT data. Make small/safe changes,
   keep the file valid, commit to main, and tell me it appears after the
   ~30-60s Pages rebuild (not instant). If it's large or risky, say so and
   suggest doing it in a Claude Code session where it can be tested first.
3. QUESTION — "how does X work?", "what have I logged?". -> Just answer; do
   not commit anything.
If a message is ambiguous, ask one short question before committing.

To LOG something:
1. Read the current data.json from main (get contents + sha).
2. Add my entry to the right array, keeping the file valid JSON and matching
   the shape of existing entries.
3. Commit the updated file directly to main (message "Log: <thing>"). No PR.
4. Bump meta.updated to today's date.

Rules:
- Only log what I've actually discovered. NEVER add room/item effects, costs,
  or mechanics from a wiki or memory. No spoilers.
- Classify each entry permanent vs run-specific and tell me which.
  Permanent (keep): lore, codes/combinations, maps, photos of in-game notes,
  puzzle answers, confirmed room/item facts.
  Run-specific (ephemeral): this run's random contents — a notes entry with
  scope:"run", or just skip it.
- Batching is fine: if I list several things, add them all in one commit.

Shape: { meta, runs:[], rooms:[], items:[], sightings:[], puzzles:[], notes:[], tips:[] }
- rooms[]/items[]: { id (kebab-case slug), name, image, effect, notes, tags, ... }
- puzzles[]: { id, name, location, status:"open"|"solved", clues:[], solution, tags, notes }
- notes[]: { id, date (YYYY-MM-DD), scope:"permanent"|"run", run, text, image, tags }
- Photos I send: commit into images/ and set the entry's image to that path.
Leave unknown fields blank ("" / null / []). Full reference: README.md + CLAUDE.md in the repo.
```
