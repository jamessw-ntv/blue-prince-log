# blue-prince-log

Data store for my **Blue Prince** room & item log.

This repository holds both the data and the viewer:

- [`data.json`](./data.json) — the single source of truth for the rooms, items,
  puzzles, runs, and notes I discover while playing
  [Blue Prince](https://blueprince.wiki.gg/).
- [`index.html`](./index.html) — a self-contained, read-only viewer that renders
  `data.json`. No build step, no dependencies.

The repo is **public on purpose** so the viewer can fetch the data without
authentication. **Live viewer: https://jamessw-ntv.github.io/blue-prince-log/**

> **Public repo / spoilers:** everything in `data.json` is world-readable, and by
> choice this log **stores full puzzle solutions and spoilers**. Don't put anything
> private in here.

## How it fits together

```
┌──────────────────────────────────────────────┐
│ jamessw-ntv/blue-prince-log (this repo, public)│
│                                                │
│   index.html  ──fetch("data.json")──▶ data.json│   served together via GitHub Pages
│   (read-only viewer)   same origin             │   at https://jamessw-ntv.github.io/blue-prince-log/
└──────────────────────────────────────────────┘
```

The viewer and data now live in **the same repo**, so the viewer fetches
`data.json` with a plain same-origin relative request — **no GitHub API, no token,
no rate limit, no CORS.** Anything committed to `main` shows up on the next refresh.

If you ever need to read the data from elsewhere, the raw URL works without a
token: `https://raw.githubusercontent.com/jamessw-ntv/blue-prince-log/main/data.json`
(the `api.github.com/.../contents/...` endpoint also works but is rate-limited to
~60 requests/hour per IP). `index.html` falls back to this raw URL automatically if
the same-origin fetch fails (e.g. opened from `file://`).

## Deploying the viewer (GitHub Pages)

One-time setup:

1. Repo **Settings → Pages**.
2. **Source:** *Deploy from a branch*; **Branch:** `main`, **Folder:** `/ (root)`;
   **Save**.
3. After a minute the viewer is live at
   **https://jamessw-ntv.github.io/blue-prince-log/**.

### Redirecting the old `ntv-prod` location

The viewer used to live in `jamessw-ntv/ntv-prod` (served under
`https://jamessw-ntv.github.io/NTV-PROD/`). To forward the old URL to the new one,
drop a small redirect page where the old viewer was (e.g.
`ntv-prod/docs/blue-prince/index.html`):

```html
<!doctype html>
<meta charset="utf-8">
<title>Moved</title>
<meta http-equiv="refresh" content="0; url=https://jamessw-ntv.github.io/blue-prince-log/">
<link rel="canonical" href="https://jamessw-ntv.github.io/blue-prince-log/">
<p>This log moved to <a href="https://jamessw-ntv.github.io/blue-prince-log/">jamessw-ntv.github.io/blue-prince-log</a>.</p>
```

(If you'd rather keep the canonical address on `ntv-prod`, do the reverse: leave the
viewer here and point a redirect *from* the new URL back to the old one. Either way
only one place should host the real `index.html`.)

## Viewer controls

The header has three controls:

- **🏭 Satisfactory** — link back to the factory-network page
  (`https://jamessw-ntv.github.io/NTV-PROD/factory-network.html`).
- **Run `−` / `+`** — a quick run-number tracker. Because the viewer is a static,
  tokenless page it **can't write back to `data.json`**, so this is saved **per
  browser** (`localStorage`) and is purely for keeping your place while playing. It
  highlights the matching run in the Runs/Sightings tabs and shows a hint with a
  *reset* link when it differs from the file. To make a new run permanent, tell the
  logging chat “new run” (it bumps `meta.currentRun` and adds to `runs[]`).
- **💡 Tips** — toggles the `tips[]` panel (training tips / examples, with images).

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
  `meta`, `runs`, `rooms`, `items`, `sightings`, `puzzles`, `notes`, `tips`.
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
  "notes":     [ ... ],   // free-form dated notes
  "tips":      [ ... ]    // training tips / examples shown under the viewer's Tips toggle (can include images)
}
```

### `meta`

| Field           | Type   | Notes                                                    |
| --------------- | ------ | -------------------------------------------------------- |
| `game`          | string | Always `"Blue Prince"`.                                  |
| `title`         | string | Display title for the viewer.                            |
| `schemaVersion` | number | Currently `3`. Bump only if the schema shape changes.    |
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

### `tips[]`

Training tips / examples shown when you turn on the viewer's **💡 Tips** toggle.
Each tip can include an image.

| Field   | Type     | Allowed / notes                                                              |
| ------- | -------- | --------------------------------------------------------------------------- |
| `id`    | string   | Unique kebab-case slug.                                                      |
| `title` | string   | Heading for the tip.                                                         |
| `body`  | string   | The tip text. Newlines (`\n`) render as line breaks.                        |
| `image` | string   | *(optional)* Image URL or repo-relative path (e.g. `images/floorplan.png`). |
| `tags`  | string[] | Free-form labels.                                                           |

**Images:** commit them into this repo (e.g. an `images/` folder) and reference
them with a relative path, or point `image` at any public URL. Relative paths work
because the viewer is served from the same GitHub Pages site.

## Seed data

`data.json` ships with a small set of example rooms (one per color, plus the
upgradeable Spare Room), the core resources, two example sightings, and one example
run/puzzle/note so the viewer has something to render. Entries tagged `"example"`
(and `example-*` ids) are placeholders — delete or overwrite them as real logging
begins.
