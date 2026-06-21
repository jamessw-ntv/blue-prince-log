# Blue Prince — project rules

A **spoiler-free Blue Prince notepad**. Claude maintains `blue-prince/data.json`;
the read-only viewer (`blue-prince/index.html`) renders it at
<https://jamessw-ntv.github.io/blue-prince/>. Full schema is in the repo README.

## Intent routing

1. **Logging** (default for anything about the game): "the Den does X", "found a
   code 4-7-2", a photo. → Edit `blue-prince/data.json`, commit to `main`.
2. **Viewer change** ("add a column", "change colours"): → edit
   `blue-prince/index.html`; appears after the ~30–60s Pages rebuild.
3. **Question** → just answer; don't commit.

If a message is ambiguous, ask one short clarifying question before committing.

## Golden rules

1. **Only log what the user has actually discovered**, in their words. This is a
   discovery game — **never pre-fill room/item effects, costs, or mechanics from
   a wiki or memory.** No spoilers unless the user explicitly states the fact.
2. **Classify every entry permanent vs run-specific, and say which.**
   - **Permanent** (keep): lore/story, codes & combinations, maps, photos of
     in-game notes, puzzle answers, fixed room/item facts the user confirmed.
   - **Run-specific** (ephemeral): this run's random contents. Usually skip; if
     kept, use a `notes` entry with `scope:"run"`.
   - Rule of thumb: *"Will this still be true next run?"* Yes ⇒ permanent.
3. **Batching is fine.** Add several things in one commit.
4. Keep `data.json` valid JSON, commit to `main`, push. Bump `meta.updated`.

## Where things go

- `rooms[]` / `items[]` — a room/item + what it does (only once confirmed).
- `puzzles[]` — `{ name, location, status:"open"|"solved", clues[], solution }`.
- `notes[]` — anything else: `{ date, scope:"permanent"|"run", run, text, image, tags }`.
- `tips[]` — help for using the tool (leave as-is unless asked).

`id` is a kebab-case slug; dates are ISO `YYYY-MM-DD`; leave unknown fields blank.

## Photos

If the user sends a picture, commit it into `blue-prince/images/` and reference
it from the entry's `image` field. Photos of fixed content are permanent.

## Don't

- Don't invent or wiki-source content the user hasn't seen.
- Don't re-add per-run "sightings" tracking (removed on purpose).
- Don't open a PR; just commit to `main`.
