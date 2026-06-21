# 🔁 Conversion Playbook — ingest any open module into the engine

*Proof of concept: **there's always a story.** The engine takes an existing, royalty-free adventure
(a "found module") and converts it into a playable campaign on our rules — deriving the spine, the
Living Map, stat blocks, and branches. This is the "Run a module" / Pre-Made Library capability.*

## Where to get legal source modules
- **One Page Dungeon Contest** — every entry is **CC-BY-SA 4.0** (free to adapt + share *with
  attribution*; release your adaptation under the same licence) and **deliberately system-neutral**.
  The richest open library. ([submission rules](https://www.dungeoncontest.com/submission-rules) ·
  [site](https://www.dungeoncontest.com/))
- **SRD 5.2 (CC-BY-4.0)** — for any mechanics/monsters you need to flesh the module out.
- **Public-domain stories** — myth, folklore, gothic horror: convert the narrative, stat with SRD.

## The conversion pipeline (6 steps)
1. **Read the module; pick a System** (🎲 Rules-Light / 📚 5e / 🧩 LitRPG) + tone + Freedom dial.
2. **Plot → Spine:** map the module's beginning / turn / climax to **locked beats** (b1…b5) with
   flexible triggers.
3. **Locations → Living Map:** each keyed area becomes a **node** (id/title/type/state/tags/summary);
   the paths between them become **edges**.
4. **Monsters & NPCs → stat blocks** in the chosen system's printed format (SRD for 5e; §7 for
   Rules-Light; §9 economy for LitRPG). Reuse SRD blocks where they fit.
5. **Decisions → branches** + a moral/ending fork; set the win condition(s).
6. **Wrap:** seed the initial `state.json`, write the §12 save body, and add **attribution**.

**Completeness check (don't skip):** every hazard prints a **DC**; every grapple/restrain prints an
**escape save**; every open-ended effect (a "wish"/boon) is **GM-bounded**; every monster prints an
**Init** mod + attack bonus. *(The fine-grain a live run exposes — folded from the worked-example validation.)*

## Legal (required)
Adapting a **CC-BY-SA** module: **credit the author + the source** and **release your adaptation
under CC-BY-SA 4.0** too (share-alike). SRD content keeps its CC-BY-4.0 attribution (§17). **Never
ingest copyrighted text** — a module the player owns but that isn't open is *run from their copy
only*, never reproduced.

## Worked example
See [`./adventures/converted-example.md`](./adventures/converted-example.md) — a representative open
one-page dungeon (the **input**) and its full conversion into a playable campaign (the **output**).
Swap in any real OPDC entry the same way, with its attribution.

## Change Log
| Date | What changed |
| --- | --- |
| 2026-06-21 | Created. The "ingest a module → campaign" pipeline + legal + the OPDC (CC-BY-SA) source library. |
