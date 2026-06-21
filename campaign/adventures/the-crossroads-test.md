# 🔑 The Ember Key — 5-Minute Engine Test

*The smallest possible adventure: a pure **decision tree** to prove the engine runs,
branches correctly, resolves a check, updates the live state, and reaches distinct
endings. Uses only rock-solid Rules-Light mechanics (d20 + modifier vs DC, flat HP) —
no recharge, multiattack, or anything §7 doesn't define. ~5 minutes.*

**System:** 🎲 Rules-Light · **Hero:** one pre-gen · **Goal:** leave the crypt holding the
Ember Key.

---

## The decision tree
```
                    [NODE 1] Crypt Mouth
                     /                 \
              A: Dry Stair          B: Wet Tunnel
               [NODE 2A]              [NODE 2B]
            sneak(DEX) / fight       lever / swim(STR)
                     \                 /
                      \               /
                      [NODE 3] The Ember Key
                   /          |           \
            study(INT)     grab(DEX)      leave
            PERFECT       GOOD / SCRAPED  EMPTY-HANDED
                              (win)        (the fail path)
```

## Hero (pre-gen) — drop straight in
**Ash**, a level-1 tomb-scout. **STR +2, DEX +2, CON +1, INT +1, WIS +0, CHA +0.**
**HP 12/12 · AC 14.** Shortsword: **+4 to hit, 1d6+2**. *Quick Hands:* advantage on the
first DEX check of the run *(treat the whole crypt as one "scene")*.
Carries a shortsword, two torches, a coil of rope.

---

## NODE 1 — Crypt Mouth
Cold air, two ways on. **Left:** a dry stone stair, faint smell of ash. **Right:** a
flooding tunnel, water already at the ankle and rising.
- **Choose A (Dry Stair)** → NODE 2A
- **Choose B (Wet Tunnel)** → NODE 2B

## NODE 2A — The Dry Stair
An **ash-hound** dozes by a brazier, between Ash and the inner door.
- **Sneak past** — DEX (Stealth) **DC 13** *(Quick Hands → advantage if it's the first DEX
  check)*. **Success:** slip through → NODE 3. **Fail:** it wakes → short fight.
- **Fight** — Ash acts first (the hound is dozing — no initiative roll). Ash-hound: **HP 7,
  AC 12**, bite **+3, 1d6**; Ash strikes at **+4, 1d6+2**. Drop it (~2 rounds) → NODE 3.
- *Fail-forward:* losing the sneak just costs a little HP; you always reach NODE 3.

## NODE 2B — The Wet Tunnel
Water rising fast. A rusted **lever** on the wall; the key alcove lies across the deepening
water.
- **Pull the lever** — a grate grinds open, the water drains, the way is dry → NODE 3 *(no
  risk; rewards caution)*.
- **Swim across now** — STR (Athletics) **DC 13**. **Success:** → NODE 3. **Fail:** swept
  back, **lose 1 torch**, then pull the lever instead → NODE 3.

## NODE 3 — The Ember Key
The key rests on a pressure plate; a sealed exit door stands beyond.
- **Study the plate** — INT **DC 12**. **Success:** spot the counterweight, swap in a stone,
  lift the key clean, the door yawns open → **ENDING: PERFECT** (key + unharmed + the
  brazier's **Ember Charm**, *Uncommon*: once/day relight any flame). **Fail:** no harm — you
  may still Grab.
- **Grab and run** — DEX **DC 13**. **Success:** snatch it as the dart-trap fires wide; door
  opens → **ENDING: GOOD**. **Fail:** darts graze you (**−3 HP**), but you keep the key and
  shove through → **ENDING: SCRAPED** *(still a win)*.
- **Leave the key** — walk out empty-handed → **ENDING: EMPTY-HANDED** *(the deliberate
  fail branch, so the test proves a negative path too)*.

**Win condition:** exit holding the Ember Key (Perfect / Good / Scraped all count).
*On a win, add `Ember Key` (Uncommon) to the hero's `items`; PERFECT also adds `Ember Charm`
(Uncommon — once/day relight any flame).*

---

## What a clean run validates ✅
- Menu → **Continue/Load** reconstructs the scene from `state.json`.
- **Node 1** binary branch routes correctly (A vs B).
- **Node 2** a skill check resolves *and fails forward*.
- **Node 3** a multi-option node with check-gated, distinct endings.
- `state.json` updates each move (`@` moves, HP changes, a new `log` line).
- Different choices produce **different endings** — the engine isn't on rails.

## Starter `state.json` (Node 1) — model save (note the referee fields)
```json
{
  "system": "Rules-Light",
  "tone": "Brisk dungeon test (PG)",
  "boundaries": "None; this is a mechanics test.",
  "campaign": { "name": "The Ember Key (engine test)", "location": "The Sealed Crypt", "floor": "Crypt Mouth" },
  "currency": { "name": "Gold", "amount": 0 },
  "map": { "note": "The passage forks: a dry stone stair (left) or a flooding tunnel (right).",
    "legend": { "@": "Ash", ">": "Deeper" },
    "grid": ["#######", "#..@..#", "#######"] },
  "party": [ {
    "name": "Ash", "class": "Tomb-Scout", "level": 1, "role": "leader",
    "abilities_mods": { "STR": 2, "DEX": 2, "CON": 1, "INT": 1, "WIS": 0, "CHA": 0 },
    "ac": 14, "init": 2,
    "hp": 12, "hpMax": 12, "mp": 0, "mpMax": 0,
    "status": [],
    "abilities": [ { "name": "Quick Hands", "desc": "Advantage on the first DEX check each scene." } ],
    "items": [ { "name": "Shortsword", "rarity": "Common", "qty": 1, "desc": "1d6." },
               { "name": "Torch", "rarity": "Common", "qty": 2 },
               { "name": "Rope", "rarity": "Common", "qty": 1 } ]
  } ],
  "quests": { "active": ["Leave the crypt with the Ember Key."], "completed": [] },
  "log": ["Engine test loaded. Two ways on: the dry stair, or the flooding tunnel."]
}
```
*(`abilities_mods`, `ac`, `init`, and top-level `system`/`tone`/`boundaries` are the
"real-save" fields from the learnings backlog — modelled here so the test doubles as the
reference for that schema upgrade. The dashboard safely ignores fields it doesn't render.)*
