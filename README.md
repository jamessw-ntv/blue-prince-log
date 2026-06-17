# blue-prince-log

Data store for my **Blue Prince** room & item log.

This repository holds a single source of truth — [`data.json`](./data.json) — that
records the rooms, items, puzzles, runs, and notes I discover while playing
[Blue Prince](https://blueprince.wiki.gg/). It is **public on purpose** so that a
read-only viewer can fetch it without authentication.

> **Public repo / spoilers:** everything in `data.json` is world-readable, and by
> choice this log **stores full puzzle solutions and spoilers**. Don't put anything
> private in here.

## How it fits together

```
┌─────────────────────────────┐         GitHub (no token)            ┌────────────────────────────┐
│ jamessw-ntv/blue-prince-log │  ── reads data.json live, on load ─▶ │  Viewer (read-only HTML)   │
│  (this repo, public)        │                                      │  jamessw-ntv/ntv-prod      │
│  • data.json  ← edited here │                                      │  docs/blue-prince/         │
│  • README.md  ← these rules │                                      │  GitHub Pages /blue-prince/│
└─────────────────────────────┘                                      └────────────────────────────┘
```

- **This repo** stores the data. All edits land on the `main` branch.
- **The viewer** lives in `jamessw-ntv/ntv-prod` at `docs/blue-prince/` and is
  served via GitHub Pages at `/blue-prince/`. On page load it reads `data.json`
  from `main` of this repo — **no token, no build step**. Anything committed to
  `main` here shows up in the viewer on the next refresh.
- **Recommended read URL** (no rate limit, returns plain JSON):
  `https://raw.githubusercontent.com/jamessw-ntv/blue-prince-log/main/data.json`.
  The `api.github.com/.../contents/...` endpoint also works but is rate-limited to
  ~60 requests/hour per IP for unauthenticated callers, so prefer the raw URL.

## Logging workflow

The logging is done from a **separate normal Claude chat** (not from inside this
repo's automation). The flow:

1. **Start of a run:** bump `meta.currentRun` (e.g. say *"new run"* → it becomes
   the next integer) and add a matching entry to `runs[]`.
2. **As you explore, tell the assistant what you found**, e.g.
   *"Log a room: Aquarium — green, Standard, 2 doors, has a dig spot"* or
   *"In this run, the Courtyard had 2 gems and a key."*
3. The assistant updates `data.json`: adds/updates the room or item in its catalog,
   and records a **sighting** (which room appeared in which run, and what was in
   it). This is what powers "click a thing to mark it's in this room this run" in
   the viewer.
4. The assistant commits to `main` and pushes.
5. Refresh the viewer to see it.

### How "which run / what's in the room" is modeled

- `rooms[]` and `items[]` are **catalogs** — one entry per distinct room/item, with
  a `firstSeenRun` recording the run you first encountered it.
- `runs[]` is the list of runs (days). `meta.currentRun` points at the active one.
- `sightings[]` is the **per-run, per-room record**. Each sighting is one room's
  appearance in one run, plus the items found inside it that run. The viewer's
  "click to denote this item is in this room this run" action **finds-or-creates**
  the sighting for `(meta.currentRun, roomId)` and toggles the item in its `items`
  list. Sighting ids use the deterministic form `run<N>-<roomId>` so there's never
  a duplicate for the same room in the same run.

### Room variants (upgrades)

Blue Prince rooms can be permanently **upgraded** (via Upgrade Disks). An upgraded
floorplan keeps its base room's directory slot but can change color and effect, so
variants are nested under their base room in `rooms[].variants[]` rather than being
separate rooms. The **Spare Room** is the headline case: it upgrades into one of
three types (Bedroom / Hall / Greenroom), each with its own sub-upgrades. Record a
specific variant appearing in a run by setting `variantId` on that sighting.

### Rules for whoever (or whatever) edits `data.json`

- **Keep it valid JSON.** No comments, no trailing commas. Validate before
  committing (`python3 -c "import json; json.load(open('data.json'))"`).
- **Keep the top-level shape.** The file is always an object with these keys:
  `meta`, `runs`, `rooms`, `items`, `sightings`, `puzzles`, `notes`.
- **One entry per thing; dedupe by `id`.** If a room/item already exists, update it
  in place instead of adding a duplicate. For per-run presence, add a `sighting`
  rather than duplicating the catalog entry.
- **`id` is a lowercase kebab-case slug** derived from the name
  (`"Boiler Room"` → `"boiler-room"`). Unique within its array; don't change it
  once set. (`runs[].id` is an integer.)
- **Keep references valid.** Every `sightings[].roomId` must exist in `rooms`, every
  `sightings[].items[].itemId` must exist in `items`, and `sightings[].run` must
  exist in `runs`.
- **Dates are ISO `YYYY-MM-DD`.** Use the date you logged it; `null` if unknown.
- **Bump `meta.updated`** to today's date on every edit.
- **Stick to the enumerated values** for `color`, `rarity`, item `type`, and puzzle
  `status` (see below). If something genuinely doesn't fit, add it to the schema
  here in the README first, then use it.
- **Leave unknown fields empty** (`""`, `null`, `[]`, or `0`) rather than omitting
  them — consistent shapes keep the viewer simple.
- **Commit messages**: short and descriptive, e.g. `Add Aquarium room`,
  `Run 3: log Courtyard gems`, `Mark Observatory puzzle solved`.

## `data.json` schema (v2)

Top-level object:

```jsonc
{
  "meta":      { ... },   // info about the log + currentRun pointer
  "runs":      [ ... ],   // each day/run you've played
  "rooms":     [ ... ],   // catalog of rooms discovered
  "items":     [ ... ],   // catalog of items / resources / tools
  "sightings": [ ... ],   // per-run record: which room appeared, with what inside
  "puzzles":   [ ... ],   // puzzles / codes / secrets, open or solved (full solutions stored)
  "notes":     [ ... ]    // free-form dated notes
}
```

### `meta`

| Field           | Type   | Notes                                                    |
| --------------- | ------ | -------------------------------------------------------- |
| `game`          | string | Always `"Blue Prince"`.                                  |
| `title`         | string | Display title for the viewer.                            |
| `schemaVersion` | number | Currently `2`. Bump only if the schema shape changes.    |
| `updated`       | string | ISO date of the last edit — **update on every commit**.  |
| `currentRun`    | number | The active run id; **increment when a new run starts**.  |
| `source`        | string | This repo's URL.                                         |
| `viewer`        | string | The deployed viewer URL.                                 |
| `note`          | string | Human note about the file.                               |

### `runs[]`

| Field     | Type           | Notes                                                            |
| --------- | -------------- | --------------------------------------------------------------- |
| `id`      | number         | Run number (1, 2, 3, …). Referenced by `sightings[].run`.        |
| `date`    | string         | ISO date played.                                                |
| `rank`    | number \| null | Furthest rank/row reached (the house has 9; Antechamber = 9).   |
| `outcome` | string         | How the run ended (e.g. `"reached Antechamber"`, `"out of steps"`). |
| `notes`   | string         | Anything notable about the run.                                 |

### `rooms[]`

| Field          | Type           | Allowed / notes                                                                                   |
| -------------- | -------------- | ------------------------------------------------------------------------------------------------ |
| `id`           | string         | Unique kebab-case slug.                                                                           |
| `name`         | string         | Room name as shown in game.                                                                       |
| `color`        | string         | One of `blue`, `orange`, `green`, `purple`, `yellow`, `red`, `black` (see **Room colors** below). |
| `rarity`       | string         | One of `Commonplace`, `Standard`, `Unusual`, `Rare`.                                              |
| `doors`        | number \| null | Number of doorways, if known.                                                                     |
| `cost`         | object         | `{ "gems": n, "coins": n, "keys": n }` — resources to draft/enter (special rooms usually cost Gems). |
| `digSpot`      | boolean        | `true` if the room has a Dig Spot (common in green rooms).                                        |
| `effect`       | string         | What the room does / why it matters.                                                              |
| `variants`     | object[]       | Upgraded versions — see **`rooms[].variants[]`** below. `[]` if none.                             |
| `tags`         | string[]       | Free-form labels (e.g. `"connector"`, `"shop"`, `"ability"`).                                     |
| `notes`        | string         | Personal notes.                                                                                   |
| `discovered`   | boolean        | Whether you've actually seen it in a run.                                                         |
| `firstSeenRun` | number \| null | Run id where you first saw it.                                                                    |
| `firstSeen`    | string \| null | ISO date first encountered.                                                                       |

#### `rooms[].variants[]`

| Field    | Type   | Notes                                                            |
| -------- | ------ | --------------------------------------------------------------- |
| `id`     | string | Unique kebab-case slug for the variant.                         |
| `name`   | string | Variant/upgraded room name.                                     |
| `color`  | string | Variant color (may differ from the base room).                 |
| `effect` | string | What the upgrade does.                                          |
| `source` | string | How it's obtained (e.g. `"Upgrade Disk"`).                      |
| `notes`  | string | Personal notes.                                                 |

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

| Field          | Type           | Allowed / notes                                                      |
| -------------- | -------------- | ------------------------------------------------------------------- |
| `id`           | string         | Unique kebab-case slug.                                             |
| `name`         | string         | Item name.                                                          |
| `type`         | string         | One of `Resource`, `Key`, `Tool`, `Consumable`, `Document`, `Other`. |
| `effect`       | string         | What it does.                                                       |
| `location`     | string         | Where it's found / how it's obtained.                               |
| `value`        | object         | `{ "coins": n }` — shop price if applicable, else `null`.          |
| `tags`         | string[]       | Free-form labels.                                                  |
| `notes`        | string         | Personal notes.                                                    |
| `found`        | boolean        | Whether you've obtained it.                                        |
| `firstSeenRun` | number \| null | Run id where you first saw it.                                     |
| `firstSeen`    | string \| null | ISO date first obtained.                                           |

The three main currencies are **Keys** (unlock doors), **Gems** (draft special
rooms), and **Coins / Gold** (buy from shops). **Ivory Dice** redraw floorplans
during drafting; **Upgrade Disks** permanently upgrade rooms.

### `sightings[]`

One record per room appearance per run.

| Field       | Type           | Allowed / notes                                                          |
| ----------- | -------------- | ----------------------------------------------------------------------- |
| `id`        | string         | Deterministic key `run<N>-<roomId>` (e.g. `run1-courtyard`).            |
| `run`       | number         | Run id (must exist in `runs`).                                          |
| `roomId`    | string         | Room id (must exist in `rooms`).                                        |
| `variantId` | string \| null | Variant id if an upgraded version appeared, else `null`.               |
| `items`     | object[]       | What was in the room: `[{ "itemId", "qty", "notes" }]`. `[]` if none.  |
| `notes`     | string         | Notes about this appearance.                                           |

### `puzzles[]`

Full solutions/spoilers are stored here on purpose.

| Field      | Type     | Allowed / notes                                 |
| ---------- | -------- | ----------------------------------------------- |
| `id`       | string   | Unique kebab-case slug.                         |
| `name`     | string   | Puzzle name / short description.                |
| `location` | string   | Where it appears.                               |
| `status`   | string   | `open` or `solved`.                             |
| `clues`    | string[] | Clues gathered so far.                          |
| `solution` | string   | The full answer — fill it in once solved.       |
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

`data.json` ships with a small set of example rooms (one per color, plus the
upgradeable Spare Room), the core resources, two example sightings, and one example
run/puzzle/note so the viewer has something to render. Entries tagged `"example"`
(and `example-*` ids) are placeholders — delete or overwrite them as real logging
begins.
