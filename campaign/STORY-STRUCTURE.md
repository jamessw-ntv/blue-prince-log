# 🧭 Story Structure — spine, freedom, and the living map

*How much is locked vs. free, and how "any path gets mapped out completely." This is the
canonical answer to that design question. Pairs with the GM Engine (§6) and Campaign
Creation (§11) in `./AI-DUNGEON-MASTER.md`.*

---

## The question
> *Is there a main story that must be completed, or is it free-range? And whatever path I
> take, it should be mapped out completely — fully pre-mapped, or lazily generated with
> checkpoints?*

## The answer: **Spine + Sandbox + Living Map**
Three ideas working together. You get a guaranteed story **and** genuine freedom **and** a
complete record of wherever you go.

1. **The Spine** — a few **locked beats** that always happen and must be completed for the
   campaign to end. *This is the main story that always has to be finished.*
2. **The Sandbox** — everything **between** beats is open. Go anywhere; the GM improvises and
   bends back toward the next beat **without invisible walls**.
3. **The Living Map** — every place visited, choice made, and consequence is appended to a
   **persistent story graph** in the save. The world isn't pre-built — it's **built as you
   explore and never forgotten** ("explored space becomes canon"). *That* is how any path
   gets mapped out completely.

### Why not fully pre-map the world?
Enumerating every branch ahead of time explodes combinatorially, is mostly never seen, and
makes the world rigid and retcon-prone. **Lazy generation + durable recording** gives the
*feeling* of a complete, consistent world without authoring a multiverse. You map the road
you actually walk — permanently.

### Why not pure free-range?
A story with no guaranteed beats has no shape, no payoff, no "completion." The Spine
guarantees a satisfying arc and a definite ending.

---

## The Spine (locked beats)
A campaign defines a **few load-bearing beats** (usually 3–6): an **Inciting Incident**,
1–3 **Midpoint Turns**, a **Climax**, a **Resolution**. Each beat:
- has a **flexible trigger** (multiple routes can satisfy it — not one corridor),
- is **locked**: it *will* happen, but *how / when / where* is open,
- is **tracked**: `pending → foreshadowed → active → resolved`.

The campaign **completes** when every spine beat resolves (climax → resolution reached).

## The Freedom Dial (set per campaign at Session Zero)
How tight the rails are is **a per-campaign setting** — because, as you said, it depends on
the story:

| Setting | Feel | Good for |
|---|---|---|
| **Linear** | Strong rails, beats back-to-back | Tutorials, tight one-shots |
| **Guided** *(default)* | Clear spine + meaningful side-quests; GM nudges back | Most campaigns |
| **Open** | Loose spine; mostly emergent; beats are distant gravity wells | Exploration, intrigue |
| **Sandbox** | Only the ending is fixed; the world reacts, you drive | Player-driven epics |

Stored on the save, changeable in Settings. Also store **beat count**. *"A few main points
really locked in stone"* = **Guided, ~4–5 beats** — the recommended default.

## The Living Map (the "map it out completely" engine)
A persistent **story graph** in the save, **appended every turn, never rewritten** (no
retcons):
- **Nodes** — scenes / locations / decision points / NPCs / discoveries (the `type` list is
  open — `encounter`, `hazard`, etc. are fine). Each has an id,
  title, type, summary, state (`known` / `visited` / `resolved`), and tags (`beat`,
  `branch`, `sidequest`).
- **Edges** — the choices/transitions between nodes, each with the **consequence** that
  followed.
- **Anchors** — a handful of nodes that exist **before** you reach them (the spine beats +
  key locations/factions seeded at Session Zero) → foreshadowing and a sense of a world ahead.
- **Generated nodes** — everything else, created **just-in-time** as you approach, then made
  canon by being written into the graph.
- **Current pointer + open threads** — where you are, and the loose ends in play.

This graph **is** the complete map of the realized story. Reload reads it; the GM stays
consistent with it; later it can render as a visual **story map** on the dashboard.

### Schema (extends the §14 save; lives in `state.json` under `story`)
```json
"story": {
  "freedom": "Guided",
  "spine": [
    { "id": "b1", "beat": "Inciting", "title": "The mill falls silent", "trigger": "Arrive in Bramblewick", "state": "resolved" },
    { "id": "b3", "beat": "Midpoint", "title": "Find Coll in the mine",  "trigger": "Reach the refuge",    "state": "active" },
    { "id": "b5", "beat": "Climax",   "title": "Face the Choir",         "trigger": "Enter the bell chamber","state": "pending" }
  ],
  "map": {
    "current": "n14",
    "nodes": [ { "id": "n14", "title": "The Flooded Mine", "type": "location", "state": "visited", "tags": ["beat:b3"], "summary": "Green haze; spore-thralls; water rising." } ],
    "edges": [ { "from": "n12", "to": "n14", "choice": "Took the trapdoor down", "consequence": "Left the village exposed to the smoke." } ]
  },
  "threads": [ "Bram's true motive", "the cracked bell" ]
}
```

## How the GM steers without walls
When the player wanders, the GM (per §6) bends back with **soft pressure, never barriers**:
foreshadow the next beat, let **consequences accumulate** (time passes, factions move), have
NPCs/companions **pull**, make the world **react** so the spine feels like *gravity, not a
fence*. If the player truly subverts a beat, **adapt the beat** (re-trigger it another way)
rather than block it — a beat is a **promise**, not a corridor.

## Completion & failure
- **Complete:** all spine beats resolved → climax → resolution/epilogue → final checkpoint.
- **Branch endings:** the *route* and *flavour* of the climax/resolution vary by the path and
  key decisions (the realized map), so different players get different versions of the **same
  guaranteed arc**.
- **Soft-fail (default):** failing a beat reshapes the next one (fail-forward) rather than
  ending the game — unless the campaign opts into hard-fail / permadeath.

## Session Zero additions (fold into §11)
Pick the **Freedom dial**; define the **spine beats** with flexible triggers; seed **anchors**
(start location, looming threat, a mystery, a faction); initialize the **story map** with the
opening node. *(Not yet folded into the manual + Notion playbook — flagged for `apply learnings`.)*
