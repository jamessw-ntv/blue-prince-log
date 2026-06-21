# 🎮 Going Live — LitRPG Starter Crawl

*Breadth piece: proves the engine in the **LitRPG** system + the System UI Kit.*
**System:** 🧩 LitRPG (Dungeon-Crawler game-show flavour) · **Levels:** 1 → 2 · **~15–20 min** ·
**Tone:** dark satire · **Content:** **Mature (R)** — cartoonish ultraviolence, corporate menace,
gallows humour · **Original homage** — capture the genre's vibe; **no copyrighted names or text.**

> **GM:** Run on the d20 engine (§7) + the **System UI Kit** (§13) — print `[ SYSTEM ]`,
> `[ LOOT ]`, `[ SKILL ]`, `[ ACHIEVEMENT ]`, `[ QUEST ]` notifications as things happen. The
> **System** is a character: a cheerful-menacing game-show host narrating your every move to a
> galaxy of viewers. Reward **showmanship**. Keep the `state.json` HUD current.

---

## Premise
Humanity's planet was *"scheduled for redevelopment."* The survivors were dropped into **the
Dungeon** — an eighteen-floor death-crawl broadcast across the galaxy for entertainment. An AI
**System** narrates every level-up, loot drop, and death to billions. You are on **Floor 1**. The
more you *entertain*, the better your loot. Survive, descend, and maybe the sponsors will love you
enough to keep you alive.

**System voice (this campaign):** cheerful, chummy, and casually monstrous — a host who adores you
right up until you're cancelled.

## The hero — start Unclassed
You begin as an **Unclassed Crawler** (a normal person holding whatever they had when the world
ended). After your **first real kill**, the System assigns a **Class** — usually with cruel irony.
Offer one (or Session Zero). **Level 1: HP 12, MP 6, Luck 5, prof +2.**
| Crawler | Former life | System grants | Signature |
|---|---|---|---|
| **Dent** | parking inspector | **Enforcer** | clipboard is a +1 bludgeon; "issue a Citation" (foe −2) |
| **Mo** | barista | **Alchemist** | brew a "Special" (a stim or a grenade) each safe-room |
| **Rae** | kindergarten teacher | **Beast-Tamer** | monsters hesitate (WIS check to pacify one/scene) |

**Attributes:** STR DEX CON INT WIS CHA + **Luck** (boosts loot rarity, crit range, random events).
**Pre-gen arrays (AC 10 + DEX, prof +2):** **Dent** STR+2 DEX+0 CON+2 INT+0 WIS+1 CHA+1 (AC 10) ·
**Mo** STR+0 DEX+2 CON+1 INT+2 WIS+1 CHA+1 (AC 12) · **Rae** STR+0 DEX+1 CON+1 INT+1 WIS+3 CHA+2 (AC 11).
**XP / loot / showmanship / Luck numbers:** use the **§9 "LitRPG economy"** tables as-is.

## Companion — BUDDY-7
A **Sponsor-issued floating mascot drone**: a grinning corporate logo with a speaker, relentlessly
upbeat and occasionally menacing. *Original homage to the genre's snarky sidekick.* It can: **scan**
a foe (reveal its stats), **pop a "sponsored" buff** (a boon with an embarrassing catch), and
**heckle** for the audience. Drive: ratings. Flaw: legally cannot stop advertising.

---

## Floor 1 — "Tutorial Hell" (a dead mall, weaponised)
4–5 rooms. Lethal but fail-forward where it's funnier to maim than kill.

1. **The Spawn Atrium.** You wake among other crawlers — most die in the first minute (establish the
   stakes, darkly comic). `[ SYSTEM ]  Welcome, Crawler. You are now **content**. Please smile.` A
   tutorial foe lurches up: a **Mimic Vending Machine**. **First kill → the System assigns your
   Class** with a `[ SYSTEM ] ⬆ CLASS UNLOCKED` notification + your signature skill.
2. **The Food Court of the Damned.** A pack of **3 Mall-Rats**. **Showmanship:** a flashy or funny
   kill earns **bonus XP + audience favour** (and better loot). A **loot box** drops — roll rarity,
   **+Luck** (Common→Mythic). Print `[ LOOT ]`.
3. **The Sponsor Lounge (safe room).** BUDDY-7 presents a **"sponsored" System choice** — pick one
   of **3 boons**, each with a catch (e.g. *+2 STR, but you must shout the sponsor's name before each
   attack*). A **System shop** sells stims/gear for credits. Heal here.
4. **The Maintenance Tunnels (hazard + secret).** Trapped crawlspaces (DEX **DC 13** or 1d6). A
   **hidden room** (Investigation **DC 14**) holds a **secret achievement** — `[ ACHIEVEMENT ] Off
   the Beaten Path` — and a **Rare** item. Rewards curiosity + showmanship.
5. **Floor Boss — "Mr. Tiddles, Manager of the Month."** A corrupted mall-manager fused to his
   kiosk. Beating him → `[ SYSTEM ] FLOOR 1 CLEARED`, **level to 2**, the stairs down (`>`) open.
   `[ SYSTEM ]  Floor 1 cleared! The audience is… *mildly* entertained. Do try harder, Crawler.`

---

## Mechanics (LitRPG · §9 + §7 dice)
- **Checks/combat:** d20 + mod vs DC/AC (§7). **Luck** adds to loot-rarity rolls and widens the crit
  range (nat 19–20 on high Luck).
- **Showmanship:** entertaining actions earn **bonus XP** and **better loot**; the System *rewards
  spectacle and punishes boredom* (a dull turn may draw a taunt or a hazard).
- **Leveling** is a printed plot event: +HP/MP, +1 attribute point, and a **new skill or a System
  "choice"** (pick one of N boons).
- **Loot & rarity:** Common · Uncommon · Rare · Epic · Legendary · Mythic (Luck-weighted).
- **Death is permanent and broadcast** (Mature) — fail forward where you can, but the Dungeon bites.

## Stat blocks
- **Mimic Vending Machine** — HP 8, AC 12, **Init +0**. Snack-shrapnel **+3, 1d6**. Drops 1d6 credits.
- **Mall-Rat** (goblinoid) — HP 6, AC 12, **Init +2**. Shiv **+3, 1d4+1**. Cowardly in the open.
- **Mr. Tiddles, Manager** — HP 30, AC 13, **Init +1**. Stapler-of-Authority **+5, 1d8+2**.
  *Performance Review* (recharge 5–6): all crawlers in view **WIS DC 13** or gain a stacking
  **Demerit** (−1 to all rolls per stack). *Counter:* a big showmanship beat clears 1 stack.

## Rewards & hooks
Level **2**; your **Class** + first signature skill; first **Rare** loot; the stairs to Floor 2.
Your **Showmanship score** sets **sponsor interest** (a thread — high interest = better future loot
boxes, but the System raises the difficulty to keep the ratings up). The host teases Floor 2's theme.

## State / HUD
Uses the §14 schema. Track **Class · Level · XP/Showmanship · HP/MP · Luck · loot (by rarity) · the
System log**. The diegetic notifications double as the dashboard's `log` entries.

## Change Log
| Date | What changed |
| --- | --- |
| 2026-06-21 | Created as the LitRPG breadth starter (Gate 4). Original game-show-crawl homage. |
