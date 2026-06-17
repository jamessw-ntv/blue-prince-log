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
│   index.html  ──fetch raw data.json (cache-bust)─▶ data.json│  viewer on GitHub Pages
│   (read-only viewer)                              │  at https://jamessw-ntv.github.io/blue-prince-log/
└──────────────────────────────────────────────┘
```

The viewer fetches `data.json` from the **raw GitHub URL with a cache-buster**
(`https://raw.githubusercontent.com/jamessw-ntv/blue-prince-log/main/data.json?_=…`)
— **no token, no rate limit.** This means a data change shows up in the viewer within
**a few seconds of the push**, without waiting for the Pages rebuild. It falls back
to the same-origin copy if the raw fetch fails (e.g. opened from `file://`).

Only changes to `index.html` itself need the Pages deploy (below); plain data edits
do not.

## Deploying the viewer (GitHub Pages)

One-time setup (already done):

1. Repo **Settings → Pages → Source: GitHub Actions**.
2. The [`.github/workflows/pages.yml`](.github/workflows/pages.yml) workflow then
   builds and publishes the site on every push to `main`.
3. The viewer is live at **https://jamessw-ntv.github.io/blue-prince-log/**.

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

## Viewer

Deliberately simple — a reference notepad, not a run tracker. Four tabs:
**Rooms**, **Items**, **Puzzles**, **Notes**, plus a text filter.

- **Rooms** and **Items** are tables showing just **name + effect + notes + image**
  (with a small color dot on rooms and a `▸N` badge for variants). Long text wraps;
  click a thumbnail to open the full image. Stat-block detail (rarity, cost, doors)
  is kept in `data.json` but not shown — it doesn't matter for a notepad.
- **Puzzles** are cards with a collapsible spoiler solution.
- **Notes** are cards tagged **permanent** (green) or **run-specific** (amber), and
  can show a photo/map.
- Header controls: **🏭 Satisfactory** (link to the factory-network page) and
  **💡 Tips** (toggles the `tips[]` panel of examples).

There is intentionally **no run counter or per-run marking** — run-to-run contents
are random and not worth tracking (see below). Anything you want to keep is a
**permanent** note/puzzle/room entry; anything run-specific is just a `run`-scoped
note you can clear.

## What's worth tracking (and what isn't)

The house is re-drafted every day and **most room contents are randomised per draw**
(each room has its own item pool, weighted by Luck), and some puzzles (e.g. the
Billiard Room) change daily. So logging exactly what was in a room on a given run
has little lasting value — it won't recur.

**Worth recording permanently** (it's stable):

- Room facts: `color`, `effect`, `doors`, `cost`, `digSpot`, variants.
- **Guaranteed** contents — put them in the room's `effect`/`notes` (e.g. the Nook
  always has a key; the Pantry has four coins).
- Puzzle solutions that don't change.

**Not worth recording permanently** (it's random/ephemeral):

- The specific items that happened to spawn in a room on one run.

> The catalog **starts empty on purpose** — to stay spoiler-free, rooms/items/puzzles
> are added only as *you* discover them (in your own words), not pre-filled from a
> wiki. Don't paste in room effects you haven't seen yet.

## Logging workflow

This is a **digital notepad first** — drop in whatever you find (text or a photo)
and let the assistant file it. The single most important job for the logging
assistant:

> **Classify every entry as permanent or run-specific, and say which.**
> - **Permanent** (keep in `data.json`): story/lore, codes & combinations, puzzle
>   answers that don't change, maps, **photos of in-game notes/letters**, and fixed
>   room facts. Use `notes` with `scope: "permanent"` (and a `puzzles[]` entry for
>   puzzle answers, a `rooms[]`/`items[]` entry for catalog facts).
> - **Run-specific** (ephemeral): this run's resources, drafted layout, or what
>   randomly spawned in a room. These usually **don't need committing at all** — use
>   the viewer's run-marks scratchpad. If you do log one, use `scope: "run"` with the
>   run number, and drop `scope:"run"` notes when the user says *"new run"*.
> When in doubt, ask "will this still be true next run?" — yes ⇒ permanent.

**Photos:** the user can send a picture (e.g. an in-game letter or a map). Commit it
into `images/` and reference it from the entry's `image` field. Photos of fixed
content are permanent.

The logging is done from a **separate normal Claude chat** (not from inside this
repo's automation). The flow:

1. **Tell the assistant what you found**, in plain language — a room and what it
   does, an item, a code, a puzzle clue/answer, or "here's a photo of this note".
2. The assistant **decides permanence** (see the rule above), then updates
   `data.json`: a `rooms[]`/`items[]` entry for catalog facts, a `puzzles[]` entry
   for puzzle answers, or a `notes[]` entry (with `scope`) for everything else.
3. The assistant commits to `main` and pushes.
4. Refresh the viewer to see it.

> **Legacy fields:** `runs[]`, `sightings[]`, `meta.currentRun`, and `firstSeenRun`
> still exist in the schema below from an earlier run-tracking design, but the viewer
> no longer shows them. You can ignore them — per-run data isn't worth tracking
> (see above). They're documented for completeness and can be revived if wanted.

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

## `data.json` schema (v3)

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
| `image`        | string         | *(optional)* Thumbnail shown in the table — repo-relative path or URL.                            |
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
| `image`        | string         | *(optional)* Thumbnail shown in the table — repo-relative path or URL. |
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

Free-form notepad — text, plus an optional photo. **Each note is classified as
permanent or run-specific** (see the logging rule below).

| Field   | Type           | Allowed / notes                                                              |
| ------- | -------------- | --------------------------------------------------------------------------- |
| `id`    | string         | Unique slug (e.g. dated).                                                    |
| `date`  | string         | ISO date.                                                                   |
| `scope` | string         | `permanent` (kept across runs) or `run` (run-specific, ephemeral).          |
| `run`   | number \| null | Which run it belongs to, when `scope` is `run`; else `null`.                |
| `text`  | string         | The note. Newlines (`\n`) render as line breaks.                           |
| `image` | string         | *(optional)* Photo/map — repo-relative path or URL.                         |
| `tags`  | string[]       | Free-form labels (e.g. `lore`, `code`, `map`, `photo`).                     |

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

`data.json` ships **empty** — `rooms`, `items`, `puzzles`, and `notes` are all `[]`
to keep the log spoiler-free. The only seeded content is `tips[]` (help for using
the tool, shown under the **💡 Tips** toggle) and `images/example.svg` (the
placeholder the image tip references). Everything else fills in as you play.
