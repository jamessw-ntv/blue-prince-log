# CLAUDE.md — instructions for the logging chat

This repo is a **spoiler-free Blue Prince notepad**. You (Claude) maintain
[`data.json`](./data.json); a read-only viewer renders it at
<https://jamessw-ntv.github.io/blue-prince-log/>. Full schema is in
[`README.md`](./README.md) — this file is the short version of your job.

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
