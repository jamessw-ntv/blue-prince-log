# blue-prince-log

Data store for my **Blue Prince** room & item log.

This repository holds a single source of truth — [`data.json`](./data.json) — that
records the rooms, items, puzzles, and notes I discover while playing
[Blue Prince](https://blueprince.wiki.gg/). It is **public on purpose** so that a
read-only viewer can fetch it without authentication.

## How it fits together

```
┌─────────────────────────────┐         GitHub API (no token)        ┌────────────────────────────┐
│ jamessw-ntv/blue-prince-log │  ── reads data.json live, on load ─▶ │  Viewer (read-only HTML)   │
│  (this repo, public)        │                                      │  jamessw-ntv/ntv-prod      │
│  • data.json  ← edited here │                                      │  docs/blue-prince/         │
│  • README.md  ← these rules │                                      │  GitHub Pages /blue-prince/│
└─────────────────────────────┘                                      └────────────────────────────┘
```

- **This repo** stores the data. All edits land on the `main` branch.
- **The viewer** lives in `jamessw-ntv/ntv-prod` at `docs/blue-prince/` and is
  served via GitHub Pages at `/blue-prince/`. On page load it calls the public
  GitHub API and reads `data.json` from `main` of this repo — **no token, no build
  step**. Because the read is live, anything committed to `main` here shows up in
  the viewer on the next refresh.

## Logging workflow

The logging itself is done from a **separate normal Claude chat** (not from inside
this repo's automation). The flow is:

1. Tell the assistant what you found, e.g.
   *"Log a room: Aquarium — green, Standard, 2 doors, has a dig spot."*
2. The assistant edits `data.json`, keeping it valid and consistent with the
   schema below.
3. The assistant commits the change to `main` and pushes.
4. Refresh the viewer to see it.

### Rules for whoever (or whatever) edits `data.json`

- **Keep it valid JSON.** No comments, no trailing commas. Validate before
  committing (`python3 -c "import json; json.load(open('data.json'))"`).
- **Keep the top-level shape.** The file is always an object with these keys:
  `meta`, `rooms`, `items`, `puzzles`, `notes`. The viewer depends on them.
- **One entry per thing; dedupe by `id`.** If a room/item already exists, update
  it in place instead of adding a duplicate.
- **`id` is a lowercase kebab-case slug** derived from the name
  (`"Boiler Room"` → `"boiler-room"`). It must be unique within its array and
  should not change once set.
- **Dates are ISO `YYYY-MM-DD`.** Use the date you logged it; `null` if unknown.
- **Bump `meta.updated`** to today's date on every edit.
- **Stick to the enumerated values** for `color`, `rarity`, item `type`, and
  puzzle `status` (see below). If something genuinely doesn't fit, add it to the
  schema here in the README first, then use it.
- **Leave unknown fields empty** (`""`, `null`, `[]`, or `0`) rather than
  omitting them — consistent shapes keep the viewer simple.
- **Commit messages**: short and descriptive, e.g. `Add Aquarium room`,
  `Mark Observatory puzzle solved`.

## `data.json` schema

Top-level object:

```jsonc
{
  "meta":    { ... },   // info about the log itself
  "rooms":   [ ... ],   // rooms discovered in the house
  "items":   [ ... ],   // items, resources, tools, documents
  "puzzles": [ ... ],   // puzzles / codes / secrets, open or solved
  "notes":   [ ... ]    // free-form dated notes
}
```

### `meta`

| Field           | Type   | Notes                                                   |
| --------------- | ------ | ------------------------------------------------------- |
| `game`          | string | Always `"Blue Prince"`.                                 |
| `title`         | string | Display title for the viewer.                           |
| `schemaVersion` | number | Bump only if the schema shape changes.                  |
| `updated`       | string | ISO date of the last edit — **update on every commit**. |
| `source`        | string | This repo's URL.                                        |
| `viewer`        | string | The deployed viewer URL.                                |
| `note`          | string | Human note about the file.                              |

### `rooms[]`

| Field        | Type            | Allowed / notes                                                                                   |
| ------------ | --------------- | ------------------------------------------------------------------------------------------------ |
| `id`         | string          | Unique kebab-case slug.                                                                           |
| `name`       | string          | Room name as shown in game.                                                                       |
| `color`      | string          | One of `blue`, `orange`, `green`, `purple`, `yellow`, `red`, `black` (see **Room colors** below). |
| `rarity`     | string          | One of `Commonplace`, `Standard`, `Unusual`, `Rare`.                                              |
| `doors`      | number \| null  | Number of doorways, if known.                                                                     |
| `cost`       | object          | `{ "gems": n, "coins": n, "keys": n }` — resources to draft/enter (special rooms usually cost Gems). |
| `digSpot`    | boolean         | `true` if the room has a Dig Spot (common in green rooms).                                        |
| `effect`     | string          | What the room does / why it matters.                                                              |
| `tags`       | string[]        | Free-form labels for filtering (e.g. `"connector"`, `"shop"`, `"ability"`).                       |
| `notes`      | string          | Personal notes.                                                                                   |
| `discovered` | boolean         | Whether you've actually seen it in a run.                                                         |
| `firstSeen`  | string \| null  | ISO date first encountered.                                                                       |

**Room colors** (border color = category):

| Color    | Meaning                                                                             |
| -------- | ---------------------------------------------------------------------------------- |
| `blue`   | Blueprints — neutral/beneficial; the most common rooms (the core 46 of the house). |
| `orange` | Hallways — connectors; influence what you draft from them.                         |
| `green`  | Gardens / outdoor — usually have Dig Spots that reward Gems.                        |
| `purple` | Bedrooms — rooms of the Sinclair family & staff; tend to grant extra Steps.        |
| `yellow` | Shops — spend Coins to buy items/services.                                         |
| `red`    | Red rooms — usually detrimental (dead ends or negative effects).                   |
| `black`  | Blackprints — rare/archaic precursor to blue.                                      |

### `items[]`

| Field       | Type           | Allowed / notes                                                      |
| ----------- | -------------- | ------------------------------------------------------------------- |
| `id`        | string         | Unique kebab-case slug.                                             |
| `name`      | string         | Item name.                                                          |
| `type`      | string         | One of `Resource`, `Key`, `Tool`, `Consumable`, `Document`, `Other`. |
| `effect`    | string         | What it does.                                                       |
| `location`  | string         | Where it's found / how it's obtained.                               |
| `value`     | object         | `{ "coins": n }` — shop price if applicable, else `null`.          |
| `tags`      | string[]       | Free-form labels.                                                  |
| `notes`     | string         | Personal notes.                                                    |
| `found`     | boolean        | Whether you've obtained it.                                        |
| `firstSeen` | string \| null | ISO date first obtained.                                           |

The three main currencies are **Keys** (unlock doors), **Gems** (draft special
rooms), and **Coins / Gold** (buy from shops). **Ivory Dice** redraw floorplans
during drafting.

### `puzzles[]`

| Field      | Type     | Allowed / notes                                 |
| ---------- | -------- | ----------------------------------------------- |
| `id`       | string   | Unique kebab-case slug.                         |
| `name`     | string   | Puzzle name / short description.                |
| `location` | string   | Where it appears.                               |
| `status`   | string   | `open` or `solved`.                             |
| `clues`    | string[] | Clues gathered so far.                          |
| `solution` | string   | The answer (spoiler) — leave `""` until solved. |
| `tags`     | string[] | Free-form labels.                               |
| `notes`    | string   | Personal notes.                                 |

### `notes[]`

| Field  | Type     | Allowed / notes           |
| ------ | -------- | ------------------------- |
| `id`   | string   | Unique slug (e.g. dated). |
| `date` | string   | ISO date.                 |
| `text` | string   | The note.                 |
| `tags` | string[] | Free-form labels.         |

## Seed data

`data.json` ships with a small set of example rooms and the four core resources so
the viewer has something to render. Entries tagged `"example"` (and the
`example-*` ids) are placeholders — delete or overwrite them as real logging
begins.
