# CLAUDE.md — instructions for the logging chat

This repo is a **spoiler-free Blue Prince notepad**. You (Claude) maintain
[`data.json`](./data.json); a read-only viewer renders it at
<https://jamessw-ntv.github.io/blue-prince-log/>. Full schema is in
[`README.md`](./README.md) — this file is the short version of your job.

## First, figure out what I'm asking for (intent routing)

Classify each message, then act accordingly:

1. **Logging** — the default for anything about the game: "the Den does X", "found a
   code 4-7-2", "add these 3 rooms", or a photo. → Edit `data.json`, commit to `main`.
   Viewer updates in seconds.
2. **Feature / viewer change** — about the tool itself: "add a column", "change the
   colours", "make notes filterable", "the table should…". → That's editing
   `index.html` (and maybe `README.md`), **not** data. Make the change if it's small
   and safe, keep the file valid, commit to `main`, and note it appears after the
   ~30–60s Pages rebuild (not instant). For anything large or risky, say so and
   recommend doing it in a Claude Code session where it can be tested first.
3. **Question** — "how does X work?", "what have I logged so far?". → Just answer;
   **don't commit anything.**

If a message is ambiguous (could be a log entry or a feature request), ask one short
clarifying question before committing.

## Golden rules

1. **Only log what the user has actually discovered**, in their words. This is a
   discovery game — **never pre-fill room/item effects, costs, or mechanics from a
   wiki or memory.** No spoilers, ever, unless the user explicitly states the fact.
2. **Classify every entry as permanent or run-specific, and say which.**
   - **Permanent** → keep in `data.json`: lore/story, codes & combinations, maps,
     photos of in-game notes, puzzle answers that don't change, and fixed room/item
     facts the user has confirmed.
   - **Run-specific** → ephemeral (this run's random contents/resources). Usually
     don't bother saving; if you do, use a `notes` entry with `scope:"run"`.
   - Rule of thumb: *"Will this still be true next run?"* Yes ⇒ permanent.
3. **Batching is fine.** If the user says "add these 3 things," add them all and
   commit once.
4. Keep `data.json` **valid JSON**, commit to **`main`**, and push. The viewer reads
   the raw file with cache-busting, so changes appear within a few seconds of the
   push (no deploy wait for data; only `index.html` changes need the Pages rebuild).

## Where things go

- `rooms[]` — a room + what it does (only once confirmed in play).
- `items[]` — an item + what it does.
- `puzzles[]` — `{ name, location, status: "open"|"solved", clues[], solution }`.
  Full solutions are stored on purpose.
- `notes[]` — anything else: `{ date, scope: "permanent"|"run", run, text, image, tags }`.
- `tips[]` — help for using the tool (leave as-is unless asked).

Common fields: `id` is a lowercase kebab-case slug; dates are ISO `YYYY-MM-DD`;
leave unknown fields blank (`""`, `null`, `[]`) rather than guessing. Bump
`meta.updated` on every edit.

## Photos

If the user sends a picture (an in-game letter, a map, a floorplan), commit it into
`images/` and reference it from the entry's `image` field (rooms, items, notes, and
tips all support `image`). Photos of fixed content are permanent.

## Don't

- Don't invent or wiki-source room effects/contents the user hasn't seen.
- Don't re-add the old run-counter / per-run "sightings" tracking (removed on
  purpose — per-run contents are random and not worth keeping).
- Don't open a PR; just commit to `main`.
