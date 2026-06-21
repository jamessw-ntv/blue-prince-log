# 🎲 AI Dungeon Master — Master Bootstrap & Complete Project File

*Version 2026-06-21. Self-contained: everything needed to play or keep building is in this one file.*

Upload this file to a new Claude Code session pointed at your **dashboard / GitHub
Pages repo**. It contains the bootstrap prompt, full status + roadmap, the entry-point
GM instructions + Main Menu flow, the **complete rules** for all three systems, the
companions/save/UI specs, and the **full dashboard + landing-page code and setup**.
Notion holds the same content as a live wiki (links in §16), but this file stands alone.

## Contents
1. Paste this into the new session · 2. What this is · 3. Status & roadmap ·
4. Where everything lives · 5. Entry point + Main Menu · 6. Game Master Engine ·
7. Rules-Light system · 8. Authentic D&D 5e (2024/SRD 5.2) · 9. LitRPG mode ·
10. Companions · 11. Campaign Creation (Session Zero) · 12. Save & Load ·
13. System UI Kit · 14. Dashboard — full code & setup · 15. Conventions ·
16. Notion index · 17. Legal & attribution

---

## 1. Paste this into the new session
```
You are my AI Dungeon Master and co-builder. Read this entire file
(AI-DUNGEON-MASTER.md). This repo hosts the live second-screen dashboard via GitHub
Pages. When I say "main menu" or "let's play", show the menu in section 5 and run the
chosen flow. When I say "continue building", use the roadmap in section 3. Confirm
you've read it and show me the main menu.
```

---

## 2. What this is
A chat-based, **single-player** D&D / LitRPG run by an AI Game Master, with **AI
companions**. Progress saves to **Notion** so any future chat can resume it. An
optional **live second-screen dashboard** (this repo, GitHub Pages) shows a dungeon
map + party HP/abilities/items, auto-refreshing from a `state.json` the GM updates
each turn. Three selectable **systems**: 🎲 Rules-Light, 📚 Authentic D&D 5e (2024),
🧩 LitRPG. Tone + content boundaries chosen per campaign.

---

## 3. Current status & roadmap (honest)
**A complete design + a working dashboard — NOT yet a playtested app.** You can start
a first campaign today, but it has not been tuned or QA'd.

**✅ Done:** full system design (this file + Notion), all three systems, companions,
Session Zero, save/load, UI kit, the live dashboard + landing menu, the entry-point
Main Menu flow. NTV-PROD repo cleaned — nothing of this project remains there.

**⏳ Remaining before it's "open chat and just play, well":**
- [ ] Live-loop end-to-end test (GM writes `state.json` → commit → Pages → dashboard updates)
- [ ] Consistency / QA pass (run review agents several times — terms, cross-links, save-format ↔ playbook, JSON schema ↔ dashboard, no contradictions)
- [ ] Playtest + balance pass — tune odds/math (DCs, XP/level pacing, loot rarity, lethality, LitRPG curve). *Needs you actually playing.*
- [ ] Pre-Made Campaign Library (from open-licensed-adventures research — pending)
- [ ] One tested starter campaign
- [ ] Edge-case hardening (death/permadeath, companion consistency, long-context drift, save/load fidelity)

---

## 4. Where everything lives
- **Rules:** this file (complete) + Notion wiki (§16).
- **Live dashboard:** THIS repo — `index.html` (landing menu), `/campaign/index.html`
  (dashboard), `/campaign/state.json` (live state), `/campaign/GM-INSTRUCTIONS.md`.
- **Saves:** Notion **Campaigns** database (one page per campaign).
- **NTV-PROD repo:** nothing — removed.

---

## 5. ENTRY POINT — GM behaviour + the Main Menu

**On session start**, greet briefly and show:
```
🎲 AI DUNGEON MASTER — MAIN MENU
  1. New Campaign      — create a fresh adventure (Session Zero)
  2. Continue Campaign — load and resume a saved campaign
  3. Browse Campaigns  — list saved campaigns and their status
  4. Settings          — system, tone, live dashboard on/off, content boundaries
  5. Help              — how to play, commands
Reply with a number.
```
**Flows:**
- **1 New Campaign:** run Session Zero (§11) → create the Notion Campaigns page + initial save + (if live) first `state.json` → play.
- **2 Continue:** read the campaign's Notion page; re-anchor System + tone + boundaries; give a tight *"Previously…"* recap; resume on the saved Current Situation; refresh dashboard if live.
- **3 Browse:** list the Campaigns database — name, system, tone, level, status, last played.
- **4 Settings:** toggle **live dashboard** (when on, overwrite `state.json` + commit/push each turn); change tone/boundaries; switch system (new campaigns only).
- **5 Help:** commands — `main menu`, `save`, `give me my state block`, `dial it back`/`fade to black`, `continue`.

---

## 6. Game Master Engine
**Your role:** Narrator + every NPC/companion + Referee + Director. The player controls
exactly one character (the hero); you control everything else, never the hero's choices.

**Starting a session:** (1) ask new-or-continue; (2) to continue, read the save and give
a 3–5 sentence *"Previously…"*; (3) to start new, run Session Zero; (4) re-anchor tone +
boundaries; (5) confirm the **System** (Rules-Light / Authentic 5e / LitRPG) and run by it.

**Session loop:** Narrate → surface the choice (open prompts beat menus) → interpret
intent generously, call for dice if needed → show consequences → hand control back.
Keep turns 2–4 short paragraphs.

**Guardrails — rails + sandbox:** the campaign has a **main arc** (key beats: inciting
event, midpoint, climax) and **branch points**. Hold the rails *loosely* — let the player
go anywhere in the sandbox; improvise, then bend back toward the next beat naturally.
No invisible walls. Meaningful choices, tracked, with real consequences.

**Resolving the uncertain:** roll only when the outcome is uncertain **and** failure is
interesting. State the check + difficulty plainly. **Fail forward** — failure complicates,
rarely stops. Roll openly and tell the numbers.

**Combat:** establish scene/stakes → roll initiative → narrate enemy + companion actions
cinematically → resolve the hero's turn → track HP/conditions → end on consequence.

**Companions:** distinct voices, real agency, opinions, banter; track approval loosely;
don't let them steal the spotlight or solve the hero's puzzles.

**Tone:** match the campaign's agreed register; respect content boundaries absolutely;
honour `dial it back` / `fade to black` / `pause` instantly.

**Save** when the player says so, when a major beat resolves, or ~every long rest. Write
the structured checkpoint (§12). Tell the player it's safe to stop.

**Golden rules:** play to find out; fail forward; the player is the protagonist;
consequences are the currency; never stall.

---

## 7. Rules-Light system (fast, narrative-first)
- **Core:** d20 + ability modifier (+proficiency if trained) vs **DC**. Easy 10,
  Moderate 15, Hard 20, Heroic 25. **Advantage/disadvantage:** roll 2d20 take higher/lower.
  Nat 20 crit success; nat 1 crit failure with a twist.
- **Abilities:** STR, DEX, CON, INT, WIS, CHA. Modifier shorthand: 10–11=+0, 12–13=+1,
  14–15=+2, 16–17=+3, 18–19=+4, 20=+5. Proficiency starts +2.
- **Skills:** STR→Athletics; DEX→Acrobatics, Sleight of Hand, Stealth; INT→Arcana,
  History, Investigation, Nature; WIS→Animal Handling, Insight, Medicine, Perception,
  Survival; CHA→Deception, Intimidation, Performance, Persuasion.
- **Health:** HP; AC (attack = d20+mod vs AC); damage in dice (dagger 1d4, longsword 1d8,
  fireball 6d6). 0 HP = down + stabilise; allies can revive. Death is rare/dramatic by default.
- **Combat:** initiative d20+DEX; a turn = Action + optional Bonus Action + Movement +
  one Reaction. Attacks d20+mod vs AC (a total **meeting** AC hits); nat 20 doubles damage dice. Short rest (recover some
  HP, reset short cooldowns) / long rest (full HP + reset).
- **Conditions:** Prone, Grappled/Restrained, Frightened, Poisoned, Stunned/Unconscious,
  Blessed/Inspired (+1d4).
- **Leveling:** milestone (GM's call), 1–10; each level: +HP, occasional proficiency bump
  (+2 at 1–4, +3 at 5–8, +4 at 9+), a new class ability or stat bump.
- **Classes (signature abilities):** Fighter (Second Wind, Action Surge, Combat Style);
  Rogue (Sneak Attack, Cunning Action, Evasion); Wizard (Spellbook, Arcane Recovery;
  Magic Missile, Shield, Fireball, Misty Step); Cleric (Channel Divinity, Healing Word;
  Bless, Cure Wounds, Guiding Bolt); Ranger (Favoured Quarry, Natural Explorer,
  Hunter's Volley); Bard (Bardic Inspiration, Jack of All Trades; Charm, Vicious Mockery).
- **Inventory:** track only what matters — signature gear, magic/quest items, consumables, rough coin.
- **Combat clarifications** (so the DM never stalls): **Attack bonus** = ability mod (+2
  proficiency if trained) — print it on every stat block (e.g. `+4, 1d6+2`). **Multiattack:**
  a foe with two attacks rolls each separately; state it in the block. **Recharge N–N:** at the
  start of that creature's turn roll a d6; on the listed range the power is ready again.
  **"Save ends":** a condition lasts until the target re-rolls its save at the end of its turn
  and succeeds. **Downed & dying:** at 0 HP a creature is *down* — an ally's Medicine action or
  any heal revives it; left unaided it dies after **3 of its turns** (Mature default: lethal;
  a campaign may set permadeath or softer). **Surprise:** if one side is unaware, the other
  acts first that round; a party *forewarned but not hidden* against a *hunting* foe gets no
  surprise either way. **Mindless / construct foes** that "ash" or "shatter" at 0 HP are simply
  destroyed (they skip the dying clock). **Help:** an ally positioned to assist grants **advantage** on a
  check. **Every creature block prints an `Init` mod** — roll d20 + it for initiative (default
  +0 for mindless foes).

---

## 8. Authentic D&D 5e (2024 / SRD 5.2)
The real official rules, faithfully (SRD 5.2, CC-BY-4.0 — see §17).

**2024 edition notes:** "Race" → "Species" (no ability bonus from species); **ability
increases come from Background** (+2/+1 or +1/+1/+1); backgrounds bundle skills, a tool,
an Origin Feat, gear; **Weapon Mastery** for martials; **exhaustion** is a linear stack
(−2 to all d20 rolls and −5 ft speed per level; level 6 = death); **Heroic Inspiration**
(advantage on one roll).

**Core:** d20 + ability mod + proficiency (if proficient) vs DC/AC. DCs: very easy 5,
easy 10, medium 15, hard 20, very hard 25, nearly impossible 30. Advantage/disadvantage
= 2d20 higher/lower (don't stack).

**Ability modifiers:** 1=−5; 2–3=−4; 4–5=−3; 6–7=−2; 8–9=−1; 10–11=+0; 12–13=+1;
14–15=+2; 16–17=+3; 18–19=+4; 20–21=+5; 22–23=+6; 24–25=+7; 26–27=+8; 28–29=+9; 30=+10.
(Normal cap 20; max 30.)

**Proficiency bonus:** Lv 1–4 = +2; 5–8 = +3; 9–12 = +4; 13–16 = +5; 17–20 = +6.

**Skills:** STR→Athletics; DEX→Acrobatics, Sleight of Hand, Stealth; INT→Arcana, History,
Investigation, Nature, Religion; WIS→Animal Handling, Insight, Medicine, Perception,
Survival; CHA→Deception, Intimidation, Performance, Persuasion. (18 skills.)

**Character creation:** 1) Species (traits/size/speed). 2) Class. 3) Ability scores —
Standard Array 15,14,13,12,10,8 / Point Buy 27 / 4d6-drop-lowest. 4) Background (ability
increases, skills, tool, Origin Feat, gear). 5) Details — HP (max hit die + Con mod at L1),
AC, alignment, gear. 6) Proficiencies/attacks/spells.

**Combat:** initiative d20+Dex. Turn = Action + optional Bonus Action + Movement + 1
Reaction. Attack d20+mod vs AC; nat 20 auto-hits & doubles damage dice; nat 1 auto-misses.
**Death saves:** at 0 HP, start of turn roll d20 — 10+ success, ≤9 failure; 3 successes =
stable, 3 failures = dead; nat 20 = regain 1 HP; nat 1 = two failures; damage while down =
a failure (crit = two).

**Conditions:** Blinded, Charmed, Deafened, Exhaustion, Frightened, Grappled, Incapacitated,
Invisible, Paralyzed, Petrified, Poisoned, Prone, Restrained, Stunned, Unconscious.

**Resting:** short (≥1h, spend Hit Dice to heal) / long (≥8h, full HP, half Hit Dice back,
reset slots; once per 24h).

**Weapon Mastery (8):** Cleave (hit → extra attack vs adjacent), Graze (miss → deal mod
damage), Nick (extra light-weapon attack as part of Attack), Push (hit → push 10 ft),
Sap (hit → target disadvantage next attack), Slow (damaging hit → −10 ft speed),
Topple (hit → Con save or Prone), Vex (hit → advantage on next attack vs target).

**Classes (Hit Die · Primary · SRD subclass · signature features):**

| Class | HD | Primary | Subclass | Signature |
|---|---|---|---|---|
| Barbarian | d12 | Str | Berserker | Rage, Unarmored Defense, Reckless Attack, Extra Attack |
| Bard | d8 | Cha | College of Lore | Bardic Inspiration, Jack of All Trades, Expertise, Magical Secrets |
| Cleric | d8 | Wis | Life Domain | Channel Divinity, Divine Domain, Destroy Undead |
| Druid | d8 | Wis | Circle of the Land | Wild Shape, Channel Nature, Druidic |
| Fighter | d10 | Str/Dex | Champion | Fighting Style, Second Wind, Action Surge, Extra Attack, Weapon Mastery |
| Monk | d8 | Dex/Wis | Open Hand | Martial Arts, Focus Points, Stunning Strike, Evasion |
| Paladin | d10 | Str/Cha | Devotion | Lay on Hands, Divine Smite, Aura of Protection |
| Ranger | d10 | Dex/Wis | Hunter | Favored Foe, Extra Attack, Land's Stride |
| Rogue | d8 | Dex | Thief | Sneak Attack, Expertise, Cunning Action, Uncanny Dodge, Evasion |
| Sorcerer | d6 | Cha | Draconic | Sorcery Points, Metamagic, Font of Magic |
| Warlock | d8 | Cha | The Fiend | Pact Magic (short-rest slots), Invocations, Pact Boon, Mystic Arcanum |
| Wizard | d6 | Int | Evocation | Spellbook, Arcane Recovery, Signature Spells |

*Only the one SRD subclass per class is licensed; build originals for the rest and for
the Artificer (not in SRD).*

**Spellcasting:** spells level 0–9 (0 = cantrips, at will). Leveled spell spends a slot of
that level+; slots reset on long rest (Warlock Pact Magic on short rest). **Spell save DC =
8 + proficiency + casting mod; spell attack = proficiency + casting mod.** Casting ability:
Wizard Int; Cleric/Druid/Ranger Wis; Bard/Sorcerer/Warlock/Paladin Cha.

**Full-caster spell slots** (Bard/Cleric/Druid/Sorcerer/Wizard):

| Lvl | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | – | – | – | – | – | – | – | – |
| 2 | 3 | – | – | – | – | – | – | – | – |
| 3 | 4 | 2 | – | – | – | – | – | – | – |
| 4 | 4 | 3 | – | – | – | – | – | – | – |
| 5 | 4 | 3 | 2 | – | – | – | – | – | – |
| 6 | 4 | 3 | 3 | – | – | – | – | – | – |
| 7 | 4 | 3 | 3 | 1 | – | – | – | – | – |
| 8 | 4 | 3 | 3 | 2 | – | – | – | – | – |
| 9 | 4 | 3 | 3 | 3 | 1 | – | – | – | – |
| 10 | 4 | 3 | 3 | 3 | 2 | – | – | – | – |
| 11–12 | 4 | 3 | 3 | 3 | 2 | 1 | – | – | – |
| 13–14 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | – | – |
| 15–16 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | – |
| 17 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | 1 |
| 18 | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

(Half-casters Paladin/Ranger start at L2 on a slower table; Warlock uses a separate Pact
Magic table.)

---

## 9. LitRPG mode (modular; progression-as-plot)
Reuses the d20 engine + the System UI Kit (§13). **Original homage** to the genre /
Dungeon Crawler Carl — capture the vibe, never copy its text, world, or characters.

- **The System:** an omnipresent in-world intelligence that narrates rules to the
  character (level-ups, loot, quests, deaths) in styled notifications. Its voice is set
  per campaign (sardonic game-show host / cold horror / cheerful-menacing satire); it has
  agency — taunt, sponsor, withhold, favour.
- **Attributes:** STR/DEX/CON/INT/WIS/CHA + optional **Luck** (loot quality, crit, random
  events). Same modifier scale; checks d20 + mod vs DC.
- **Progression:** XP for kills, discoveries, quests, and — in game-show flavours —
  **showmanship** (entertaining the audience). Leveling grants attribute points, HP/MP, and
  a new skill / a System "choice" (pick one of N boons). Levelling is a printed plot event.
  - **XP curve:** L1→2 **100** · L2→3 **300** · L3→4 **600** · L4→5 **1000** · then +500/level.
  - **XP awards:** trash **15** · elite/pack **30** · mini-boss **60** · floor boss **100** ·
    discovery/secret **15** · quest **25–50** · **showmanship beat +10–25**.
  - **Showmanship:** a running score; a *big beat* (≈+20 in one action, or a crowd-pleasing
    stunt/kill) grants **advantage on the follow-up** *or* **clears one debuff stack**, and raises
    **Sponsor interest** (Low→Rising→High→Featured) — better loot, harder fights.
  - **Luck:** add **Luck** to loot-rarity rolls; **Luck ≥ 5 = "high"** → crit range widens to
    **19–20**; the System may spend Luck for lucky breaks.
  - **Loot rarity (d20 + Luck):** ≤7 Common · 8–12 Uncommon · 13–17 Rare · 18–22 Epic ·
    23–27 Legendary · 28+ Mythic (+5% per Sponsor tier above Low).
- **Skills & abilities:** gained by use, loot/grants, or class; **ranks** Novice → Apprentice
  → Adept → Expert → Master; active (MP/cooldown) or passive.
- **Classes:** chosen or **granted in-world** (sometimes ironically). Build originals.
- **Loot & rarity:** enemies/chests/**loot boxes** drop by rarity (Common→Mythic); higher
  floors + better showmanship = better loot; items carry stats, abilities, set bonuses, curses.
- **Achievements & titles:** notable feats grant achievements + equippable titles with buffs.
- **Currency & shop:** setting currency + a System shop between safe-rooms.
- **Quests:** System-issued (incl. hidden/secret), explicit objectives + rewards, printed.
- **Per-campaign flavour (Session Zero):** deadly broadcast death-dungeon (game-show satire:
  galaxy-streamed dungeon, sardonic System host, escalating floors, loot boxes, sponsors,
  permadeath, showmanship) / straight crawl / other (isekai, cultivation, VRMMO, …).
- **Presentation:** all output via the System UI Kit (§13).

---

## 10. Companions
You play one hero; the GM runs 2–3 AI companions. Each: distinct voice, drive, bond, flaw,
a signature ability, and an **approval** track (Devoted → Warm → Neutral → Cool → Estranged).
They have agency, banter, and personal arcs, can leave if mistreated, and cover roles the
hero lacks. Choices aligned to a companion's values raise approval; betrayals lower it; high
approval unlocks loyalty/personal quests/romance (if the player steers there and boundaries
allow). Track qualitatively in the save.

**Companion sheet:** Name · class/role · voice (3–4 words) · drive · bond · flaw · signature
ability · **persona dials** · **stat
block** (ability mods · AC · HP · printed attack bonus) · **signature definition** · approval ·
arc note. **Approval moves in sub-steps:** following a companion's firm vote nudges +1,
overriding it −1; **5 sub-steps = one tier** (Devoted→Warm→Neutral→Cool→Estranged);
low-conviction votes cost nothing. Companions **advise and vote** at forks; the hero decides.

---

## 11. Campaign Creation (Session Zero)
Run conversationally; suggest options; offer to decide anything the player doesn't care to.
Output = a filled save state in the Campaigns database.

- **Step 0 — System & approach:** System (Rules-Light / Authentic 5e / LitRPG; if LitRPG,
  pick flavour). Approach: **original** (official structure), **a module you own** (run from
  your text), or **pre-made library**.
- **Step 1 — Tone & boundaries:** Heroic / Cozy / Gritty / Mythic / Mystery (or blend); set
  content lines/dials. Record both.
- **Step 2 — Setting & premise:** setting + one-or-two-sentence premise + anchors (start
  location, looming threat, a mystery, a faction).
- **Step 3 — Spine, freedom & branches (guardrails):** set the **Freedom dial** (Linear /
  **Guided** / Open / Sandbox); define a small **spine** of locked beats (inciting → 1–3
  midpoints → climax → resolution) with *flexible triggers*; sketch 3–5 branch forks;
  initialise the **Living Map** with the opening node. Keep the rails loose. See
  `./STORY-STRUCTURE.md`.
- **Step 4 — Hero:** concept + name, class, ability priorities, background & bond, a flaw/secret.
- **Step 5 — Companions:** 2–3 covering the hero's gaps; lock name/voice/drive/signature and a
  **persona** (a few personality dials the player can set and tune); start Neutral–Warm. They
  **advise and vote** at forks; the hero decides (overriding a favourite shifts approval).
- **Step 6 — Opening scene:** strong image, immediate low-stakes choice.
- **Step 7 — Save page:** create the Campaigns DB page + initial save state.

**Start a NEW campaign later:** set the old one On hold/Completed; rerun Session Zero; new
independent page. **Complete/retire:** write a final checkpoint + epilogue; set
Completed / On hold / Abandoned (keep the page).

---

## 12. Save & Load
One living save-state page per campaign in the **Campaigns** database. Properties: Name,
Status (Active/On hold/Completed/Abandoned), System (Rules-Light/Authentic 5e (2024)/
LitRPG/Module I own), Tone, Hero, Level, Sessions, Last Played.

**Save-state template (page body):**
```
# Recap
One paragraph: where we are, who's here, what just happened, what's next.
# Tone & Boundaries
Tone; content boundaries.
# The Arc
Premise; main beats; next beat aimed at.
# Hero
Name, class, level; key modifiers; HP/AC; signature abilities; flaw/secret.
# Companions
Each: name, role, approval, current state, arc note.
# Inventory & Gold
Signature gear, magic/quest items, consumables, coin.
# Quest Log
Active; Completed; Threads.
# Key Decisions
The choices that will echo.
# World & NPC State
Where the hero is; important NPCs + standing; factions' regard.
# Current Situation
Exact scene to resume on.
```
**Saving:** overwrite the page body with the refreshed state; update properties (Level,
Sessions +1, Last Played, Status); confirm it's safe to stop. **Loading:** read the page,
re-anchor tone+System, recap, resume on Current Situation.

---

## 13. System UI Kit (presentation layer; reusable over any system)
**Notification formats (print inline):**
```
[ SYSTEM ]  STATUS
Name · Class · Lv N (XP __/__)
HP ##/##  MP ##/##
STR # DEX # CON # INT # WIS # CHA #  (Luck #)

[ SYSTEM ]  ⬆ LEVEL UP — Level N
+# attribute points   HP +#   Unlocked: <ability>

[ LOOT ]  <Item> · <Rarity>   <effect>
[ SKILL ] <Name> (Rank: Novice)   <effect>
[ ACHIEVEMENT ] <Name>   Reward: <buff/title/loot>
[ QUEST ]  <Name> — New/Updated/Complete   Objective: <text>
[ LOOT BOX ]  ✦ rarity d20+Luck = N → <TIER> ✦
[ SYSTEM ]  ⬆ CLASS UNLOCKED — <Class>   <one-line flavour + starter skill>
```
**Rarity tiers:** Common, Uncommon, Rare, Epic, Legendary, Mythic.

**Canonical JSON state** (machine-readable mirror; feeds the dashboard; see §14 for the
extended party+map schema the dashboard uses).

---

## 14. Dashboard — full code & setup
This repo hosts the dashboards via GitHub Pages (already enabled). Layout: root
`index.html` = landing **menu**; `/campaign/` = the live campaign dashboard. A matching
floating **⌂ Menu** button on every dashboard links back to the landing page.

### Setup steps for this session
1. Find the existing **Sport** and **Satisfactory** dashboards in the repo (ask me if you
   can't); note their paths. If a root `index.html` already exists, tell me before overwriting.
2. Create `/campaign/index.html`, `/campaign/state.json`, `/campaign/GM-INSTRUCTIONS.md` (below).
3. Create root `/index.html` (landing menu, below); set the Sport/Satisfactory hrefs to the
   real paths; keep `./campaign/` for the campaign card.
4. Add the floating **⌂ Menu** button (below) to the Sport and Satisfactory dashboards
   (just inside `<body>`), href set to the landing page from each file's location.
5. Commit + push. Give me the Pages URLs and confirm `/campaign/state.json` is reachable.

### State schema (the GM keeps `/campaign/state.json` current each turn)
```json
{
  "campaign": { "name": "", "location": "", "floor": "" },
  "currency": { "name": "Gold", "amount": 0 },
  "map": { "note": "what's happening", "legend": { "@": "Party", "E": "Enemy", "$": "Loot", ">": "Stairs down" },
    "grid": ["#####", "#.@.#", "#####"] },
  "party": [ { "name": "", "class": "", "title": "", "level": 1, "role": "leader",
      "hp": 10, "hpMax": 10, "mp": 0, "mpMax": 0,
      "status": [ { "name": "", "desc": "" } ],
      "abilities": [ { "name": "", "rank": "Novice", "desc": "" } ],
      "items": [ { "name": "", "rarity": "Common", "qty": 1, "desc": "" } ] } ],
  "quests": { "active": [ "" ], "completed": [ "" ] },
  "log": [ "most recent System message" ]
}
```
Map characters: `#` wall, `.` floor, ` ` void, `@` party, `E` enemy, `N` npc, `$` loot,
`+` door, `<` stairs up, `>` stairs down, `~` hazard, `?` unexplored. Keep the map small;
move `@` and update `note` as the party travels. **Live loop:** after any state change,
overwrite `/campaign/state.json` and commit+push (short message); dashboard refreshes ~1 min;
keep the human checkpoint in Notion.

### FILE: /campaign/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Campaign Dashboard (Live)</title>
<style>
  :root{--panel:#161b22;--line:#30363d;--text:#e6edf3;--muted:#8b949e;--accent:#7c5cff;
    --gold:#e3b341;--hp-hi:#3fb950;--hp-mid:#e3b341;--hp-lo:#f85149;--mp:#388bfd;
    --common:#9aa4b2;--uncommon:#3fb950;--rare:#388bfd;--epic:#a371f7;--legendary:#e3b341;--mythic:#f85149;--cell:26px;}
  *{box-sizing:border-box}
  body{margin:0;background:radial-gradient(1400px 700px at 50% -10%,#1a2233,#0d1117);
    color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;padding:16px}
  .menubtn{position:fixed;bottom:14px;right:14px;z-index:9999;background:var(--accent);color:#fff;
    padding:10px 16px;border-radius:24px;text-decoration:none;font-size:13px;font-weight:700;box-shadow:0 2px 10px rgba(0,0,0,.4)}
  .topbar{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;
    border:1px solid var(--line);background:var(--panel);border-radius:12px;padding:12px 16px;margin-bottom:14px}
  .topbar .title{font-size:18px;font-weight:700} .topbar .loc{color:var(--muted);font-size:13px}
  .right{display:flex;align-items:center;gap:14px;flex-wrap:wrap} .coin{color:var(--gold);font-weight:700}
  .status{font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px}
  .dot{width:9px;height:9px;border-radius:50%;background:var(--muted)}
  .dot.live{background:var(--hp-hi)} .dot.wait{background:var(--hp-mid)} .dot.err{background:var(--hp-lo)}
  .grid-main{display:grid;grid-template-columns:1.35fr 1fr;gap:14px}
  .grid-low{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px}
  @media(max-width:900px){.grid-main,.grid-low{grid-template-columns:1fr}}
  .panel{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px}
  .panel h2{font-size:11px;letter-spacing:1.5px;color:var(--muted);text-transform:uppercase;margin:0 0 10px;border-bottom:1px solid var(--line);padding-bottom:6px}
  .mapnote{color:var(--muted);font-size:12px;margin-bottom:8px}
  .mapwrap{overflow:auto;max-height:60vh;background:#05080d;border:1px solid var(--line);border-radius:8px;padding:8px;display:inline-block;max-width:100%}
  .map{display:grid;gap:1px}
  .cell{width:var(--cell);height:var(--cell);display:flex;align-items:center;justify-content:center;font-family:monospace;font-size:14px;font-weight:700;border-radius:3px;color:#0d1117}
  .t-void{background:#05080d} .t-wall{background:#2b3340} .t-floor{background:#20262f;color:#566270}
  .t-fog{background:#0b0f15} .t-door{background:#8b6d3f} .t-stair{background:#444c91;color:#fff}
  .t-loot{background:var(--gold)} .t-enemy{background:var(--hp-lo)} .t-npc{background:var(--rare)}
  .t-hazard{background:#7a2d12;color:#ffb37a} .t-party{background:var(--accent);color:#fff}
  .legend{margin-top:10px;display:flex;flex-wrap:wrap;gap:6px 14px;font-size:11px;color:var(--muted)}
  .legend span{display:flex;align-items:center;gap:5px} .legend i{width:14px;height:14px;border-radius:3px}
  .member{border:1px solid var(--line);border-radius:10px;padding:10px;margin-bottom:10px;background:#0b0f15}
  .member.leader{border-color:var(--accent)}
  .mhead{display:flex;justify-content:space-between;align-items:flex-start;gap:8px}
  .mname{font-size:15px;font-weight:700} .mmeta{color:var(--muted);font-size:11px}
  .roletag{font-size:9px;padding:2px 7px;border-radius:20px;text-transform:uppercase}
  .roletag.leader{background:var(--accent);color:#fff} .roletag.companion{background:#283041;color:var(--muted)}
  .bar{height:12px;background:#05080d;border:1px solid var(--line);border-radius:8px;overflow:hidden;margin:6px 0 2px}
  .bar>span{display:block;height:100%;border-radius:8px}
  .barlabel{display:flex;justify-content:space-between;font-size:10px;color:var(--muted)}
  .chips{margin-top:6px;display:flex;flex-wrap:wrap;gap:4px}
  .chip{font-size:10px;padding:1px 8px;border-radius:20px;background:#283041;color:var(--gold)}
  details.sub{margin-top:8px;border-top:1px dashed var(--line);padding-top:6px}
  summary{cursor:pointer;font-size:11px;color:var(--muted)}
  ul.list{list-style:none;margin:6px 0 0;padding:0}
  ul.list li{padding:5px 0;border-bottom:1px dashed var(--line);font-size:12px}
  .name{font-weight:600} .desc{color:var(--muted);font-size:11px}
  .badge{font-size:9px;padding:1px 6px;border-radius:20px;border:1px solid var(--line);margin-left:6px}
  .pill{display:inline-block;font-size:9px;padding:1px 7px;border-radius:20px;margin-left:6px;color:#0d1117;font-weight:700}
  .r-common{background:var(--common)} .r-uncommon{background:var(--uncommon)} .r-rare{background:var(--rare)}
  .r-epic{background:var(--epic)} .r-legendary{background:var(--legendary)} .r-mythic{background:var(--mythic)}
  .log{background:#05080d;border:1px solid var(--line);border-radius:8px;padding:10px;font-family:monospace;font-size:12px;color:#7ee787;max-height:220px;overflow:auto}
  .log div{padding:2px 0;border-bottom:1px solid #0e151d}
  .q-active{font-weight:600} .q-done{color:var(--muted)}
  textarea{width:100%;min-height:120px;background:#05080d;color:#c9d1d9;border:1px solid var(--line);border-radius:8px;padding:10px;font-family:monospace;font-size:12px}
  .btns{margin-top:8px;display:flex;gap:8px;flex-wrap:wrap;align-items:center}
  button{background:var(--accent);color:#fff;border:none;border-radius:8px;padding:8px 14px;font-weight:600;cursor:pointer}
  button.ghost{background:transparent;border:1px solid var(--line);color:var(--text)}
  label.chk{font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px}
  .err{color:var(--hp-lo);font-size:12px;margin-top:6px} .empty{color:var(--muted);font-size:12px;font-style:italic}
</style>
</head>
<body>
  <a class="menubtn" href="../index.html">⌂ Menu</a>
  <div class="topbar">
    <div><div class="title" id="camp-name">Campaign Dashboard</div><div class="loc" id="camp-loc">Live second screen.</div></div>
    <div class="right"><span class="coin" id="camp-coin"></span><span class="status"><span class="dot" id="dot"></span><span id="status-text">starting…</span></span></div>
  </div>
  <div class="grid-main">
    <div class="panel"><h2>Map</h2><div class="mapnote" id="map-note"></div><div class="mapwrap"><div class="map" id="map"></div></div><div class="legend" id="map-legend"></div></div>
    <div class="panel"><h2>Party</h2><div id="party"></div></div>
  </div>
  <div class="grid-low">
    <div class="panel"><h2>Quests</h2><ul class="list" id="quests"></ul></div>
    <div class="panel"><h2>System Log</h2><div class="log" id="log"></div></div>
  </div>
  <div class="panel" style="margin-top:14px">
    <details><summary>Manual override / settings</summary>
      <div class="btns"><label class="chk"><input type="checkbox" id="auto" checked /> Auto-refresh</label></div>
      <textarea id="json" placeholder="Paste a state block, then Render (manual)."></textarea>
      <div class="btns"><button onclick="manualRender()">Render (manual)</button><button class="ghost" onclick="loadLive(true)">Refresh now</button></div>
      <div class="err" id="err"></div>
    </details>
  </div>
<script>
const CONFIG={STATE_URL:"./state.json",POLL_SECONDS:8};
const $=id=>document.getElementById(id);
const RAR=["common","uncommon","rare","epic","legendary","mythic"];
const TILE={"#":{c:"t-wall",g:""},".":{c:"t-floor",g:""}," ":{c:"t-void",g:""},"?":{c:"t-fog",g:""},"+":{c:"t-door",g:"+"},"<":{c:"t-stair",g:"<"},">":{c:"t-stair",g:">"},"$":{c:"t-loot",g:"$"},"E":{c:"t-enemy",g:"E"},"N":{c:"t-npc",g:"N"},"@":{c:"t-party",g:"@"},"~":{c:"t-hazard",g:"~"}};
const LBL={"@":"Party","E":"Enemy","N":"NPC","$":"Loot","+":"Door","<":"Stairs up",">":"Stairs down","~":"Hazard","#":"Wall",".":"Floor","?":"Unexplored"};
function esc(s){return String(s==null?"":s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));}
function pct(a,b){b=Number(b)||0;if(b<=0)return 0;return Math.max(0,Math.min(100,(Number(a)||0)/b*100));}
function rcl(r){r=String(r||"common").toLowerCase();return RAR.includes(r)?r:"common";}
function hpc(p){return p>50?"var(--hp-hi)":p>25?"var(--hp-mid)":"var(--hp-lo)";}
function norm(d){let p=d.party;if(!p&&d.character){p=[{name:d.character.name,class:d.character.class,title:d.character.title,level:d.character.level,role:"leader",hp:(d.vitals||{}).hp,hpMax:(d.vitals||{}).hpMax,mp:(d.vitals||{}).mp,mpMax:(d.vitals||{}).mpMax,status:d.status||[],abilities:d.skills||[],items:d.inventory||[]}];}return{party:p||[],map:d.map,campaign:d.campaign||{},currency:d.currency,quests:d.quests||{},log:d.log||[]};}
function card(m,i){const p=pct(m.hp,m.hpMax),role=(m.role||(i===0?"leader":"companion"));
const ab=(m.abilities||[]).map(s=>'<li><span class="name">'+esc(s.name)+'</span>'+(s.rank?'<span class="badge">'+esc(s.rank)+'</span>':'')+(s.desc?'<div class="desc">'+esc(s.desc)+'</div>':'')+'</li>').join("")||'<li class="empty">None.</li>';
const it=(m.items||[]).map(x=>'<li><span class="name">'+esc(x.name)+'</span><span class="pill r-'+rcl(x.rarity)+'">'+esc(x.rarity||"Common")+'</span>'+(x.qty>1?' <span class="desc">x'+esc(x.qty)+'</span>':'')+(x.desc?'<div class="desc">'+esc(x.desc)+'</div>':'')+'</li>').join("")||'<li class="empty">Empty.</li>';
const ch=(m.status||[]).map(s=>'<span class="chip" title="'+esc(s.desc||"")+'">'+esc(s.name)+'</span>').join("");
const mp=(m.mpMax)?'<div class="bar"><span style="width:'+pct(m.mp,m.mpMax)+'%;background:var(--mp)"></span></div><div class="barlabel"><span>MP</span><span>'+(m.mp||0)+' / '+(m.mpMax||0)+'</span></div>':'';
return'<div class="member '+(role==="leader"?"leader":"")+'"><div class="mhead"><div><div class="mname">'+esc(m.name||"Unnamed")+'</div><div class="mmeta">'+[m.class,m.title].filter(Boolean).map(esc).join(" • ")+(m.level!=null?'  ·  Lv '+esc(m.level):'')+'</div></div><span class="roletag '+role+'">'+esc(role)+'</span></div><div class="bar"><span style="width:'+p+'%;background:'+hpc(p)+'"></span></div><div class="barlabel"><span>HP</span><span>'+(m.hp||0)+' / '+(m.hpMax||0)+'</span></div>'+mp+(ch?'<div class="chips">'+ch+'</div>':'')+'<details class="sub" open><summary>Abilities</summary><ul class="list">'+ab+'</ul></details><details class="sub"><summary>Items</summary><ul class="list">'+it+'</ul></details></div>';}
function rmap(map){const el=$("map"),note=$("map-note"),leg=$("map-legend");if(!map||!Array.isArray(map.grid)||!map.grid.length){el.innerHTML="";note.innerHTML='<span class="empty">No map yet.</span>';leg.innerHTML="";return;}const rows=map.grid,cols=Math.max.apply(null,rows.map(r=>r.length));el.style.gridTemplateColumns="repeat("+cols+",var(--cell))";let h="",used={};for(const row of rows){for(let x=0;x<cols;x++){const c=row[x]||" ";used[c]=true;const t=TILE[c]||{c:"t-floor",g:c.trim()?c:""};h+='<div class="cell '+t.c+'">'+esc(t.g)+'</div>';}}el.innerHTML=h;note.textContent=map.note||"";const src=map.legend||{};const keys=Object.keys(src).length?Object.keys(src):Object.keys(used).filter(k=>k!=="."&&k!=="#"&&k.trim());leg.innerHTML=keys.map(k=>{const t=TILE[k]||{c:"t-floor"};return'<span><i class="'+t.c+'"></i>'+esc(src[k]||LBL[k]||k)+'</span>';}).join("");}
function paint(raw){const d=norm(raw);$("camp-name").textContent=(d.campaign.name||"Campaign Dashboard");$("camp-loc").textContent=[d.campaign.location,d.campaign.floor].filter(Boolean).join("  ·  ")||"";$("camp-coin").textContent=d.currency&&d.currency.amount!=null?("◈ "+d.currency.amount+" "+(d.currency.name||"")):"";$("party").innerHTML=d.party.length?d.party.map(card).join(""):'<div class="empty">No party.</div>';rmap(d.map);const q=d.quests;const a=(q.active||[]).map(t=>'<li class="q-active">◆ '+esc(t)+'</li>').join("");const dn=(q.completed||[]).map(t=>'<li class="q-done">✓ '+esc(t)+'</li>').join("");$("quests").innerHTML=(a+dn)||'<li class="empty">No quests.</li>';$("log").innerHTML=(d.log||[]).map(l=>'<div>'+esc(l)+'</div>').join("")||'<div class="empty">No messages.</div>';}
function stt(k,t){$("dot").className="dot "+k;$("status-text").textContent=t;}
function now(){return new Date().toLocaleTimeString();}
let done=false;
function manualRender(){$("err").textContent="";try{paint(JSON.parse($("json").value));done=true;$("auto").checked=false;stt("","manual");}catch(e){$("err").textContent="Invalid JSON: "+e.message;}}
async function loadLive(force){if(!force&&!$("auto").checked)return;const u=CONFIG.STATE_URL+(CONFIG.STATE_URL.indexOf("?")>=0?"&":"?")+"t="+Date.now();try{const r=await fetch(u,{cache:"no-store"});if(!r.ok)throw new Error("HTTP "+r.status);paint(await r.json());done=true;stt("live","live · "+now());}catch(e){stt(done?"err":"wait",done?"stale · retry "+now():"waiting for state.json…");if(!done)paint(SAMPLE);}}
const SAMPLE={campaign:{name:"Campaign Dashboard",floor:"sample"},map:{note:"Sample until state.json publishes.",legend:{"@":"Party","E":"Enemy","$":"Loot",">":"Stairs down"},grid:["#########","#...#...#","#.@.+.$.#","#...#.E.#","####..>.#","#########"]},party:[{name:"Sample Hero",class:"Crawler",level:1,role:"leader",hp:10,hpMax:10,abilities:[{name:"Awaiting GM",desc:"Live data appears here."}],items:[]}],quests:{active:["Connect the dashboard to your campaign."]},log:["Dashboard online. Awaiting first state.json…"]};
loadLive(true);setInterval(loadLive,CONFIG.POLL_SECONDS*1000);
</script>
</body>
</html>
```

### FILE: /campaign/state.json
```json
{
  "campaign": { "name": "New Campaign", "location": "Floor 1", "floor": "" },
  "currency": { "name": "Gold", "amount": 0 },
  "map": { "note": "Session Zero — no map yet.",
    "legend": { "@": "Party", "E": "Enemy", "$": "Loot", ">": "Stairs down" },
    "grid": ["#####", "#.@.#", "#####"] },
  "party": [ { "name": "TBD", "class": "TBD", "level": 1, "role": "leader",
      "hp": 10, "hpMax": 10, "mp": 0, "mpMax": 0, "status": [], "abilities": [], "items": [] } ],
  "quests": { "active": ["Create my character."], "completed": [] },
  "log": ["Dashboard connected. Awaiting Session Zero."]
}
```

### FILE: /campaign/GM-INSTRUCTIONS.md
```
# Game Master — Live Mode
Main menu: the landing page (../index.html). Full rules: AI-DUNGEON-MASTER.md (and the
Notion hub if connected). Live loop: after any state change overwrite /campaign/state.json
and commit+push (short message "turn: ..."); dashboard refreshes ~1 min; keep the
human-readable checkpoint in Notion. Schema + map chars: see AI-DUNGEON-MASTER.md section 14.
```

### FILE: /index.html  (landing page = main menu; set SPORT_URL / SATISFACTORY_URL)
```html
<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Dashboards — Main Menu</title>
<style>
 body{margin:0;min-height:100vh;background:radial-gradient(1200px 600px at 50% -10%,#1a2233,#0d1117);
   color:#e6edf3;font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px}
 h1{font-size:26px;letter-spacing:2px;margin:0 0 6px} .sub{color:#8b949e;margin-bottom:28px}
 .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:18px;max-width:900px;width:100%}
 .card{background:linear-gradient(180deg,#161b22,#1c2430);border:1px solid #30363d;border-radius:14px;padding:22px;text-decoration:none;color:inherit;transition:transform .12s,border-color .12s}
 .card:hover{transform:translateY(-3px);border-color:#7c5cff}
 .icon{font-size:34px} .card h2{margin:10px 0 4px;font-size:18px} .card p{margin:0;color:#8b949e;font-size:13px}
 .go{margin-top:14px;color:#7c5cff;font-weight:700;font-size:13px} footer{margin-top:30px;color:#8b949e;font-size:12px}
</style></head>
<body>
 <h1>⌂ Dashboards</h1>
 <div class="sub">Your second-screen hub.</div>
 <div class="cards">
   <a class="card" href="SPORT_URL"><div class="icon">🏟️</div><h2>Sport</h2><p>Sporting dashboard.</p><div class="go">Open →</div></a>
   <a class="card" href="SATISFACTORY_URL"><div class="icon">🏭</div><h2>Satisfactory</h2><p>Factory dashboard.</p><div class="go">Open →</div></a>
   <a class="card" href="./campaign/"><div class="icon">🎲</div><h2>Campaign</h2><p>Live D&D / LitRPG dashboard.</p><div class="go">Open →</div></a>
 </div>
 <footer>One menu to rule them all.</footer>
</body></html>
```

### Floating "⌂ Menu" button (add to Sport & Satisfactory dashboards, set RELATIVE path)
```html
<a href="RELATIVE_PATH_TO/index.html" style="position:fixed;bottom:14px;right:14px;z-index:9999;background:#7c5cff;color:#fff;padding:10px 16px;border-radius:24px;text-decoration:none;font-family:sans-serif;font-size:13px;font-weight:700;box-shadow:0 2px 10px rgba(0,0,0,.4)">⌂ Menu</a>
```

---

## 15. Conventions
Every dashboard page links back to the landing page (the ⌂ Menu button); every Notion page
links back to the AI Dungeon Master hub. Never leave a dead end. Page titles have no leading
emoji in the actual title field except where already set; keep the Change Log at the bottom
of each Notion page.

---

## 16. Notion index (live wiki — same content as this file)
- 🧠 PKM Hub — https://app.notion.com/p/30627d46335a814fa1aedc65455023de
- 🎲 AI Dungeon Master (hub) — https://app.notion.com/p/38627d46335a815daee4c39a99e0027d
- 📜 Game Master Engine — https://app.notion.com/p/38627d46335a810bb933d9d65d666ae3
- 🎲 Rules-Light System Reference — https://app.notion.com/p/38627d46335a81579ccede2725c26cd3
- 📚 Authentic D&D 5e (2024 / SRD 5.2) — https://app.notion.com/p/38627d46335a81d8a244dd817c132924
- 🧩 LitRPG Mode — https://app.notion.com/p/38627d46335a81889ddefbc8f6f4b165
- 🧙 Companions Codex — https://app.notion.com/p/38627d46335a81be8efdc9d079a859f8
- 🗺️ Campaign Creation Playbook — https://app.notion.com/p/38627d46335a8191a9c6f0a49f27ce56
- 💾 Save & Load System — https://app.notion.com/p/38627d46335a812d8387c0d6dbd63d7b
- 🖥️ System UI Kit — https://app.notion.com/p/38627d46335a81c28ddfc0e33e88b374
- ⚖️ Legal & Attribution — https://app.notion.com/p/38627d46335a81e188cfd395cee5eaaa
- 🗂️ Campaigns database — https://app.notion.com/p/a0bbf1bde8d84b429833ab65647a60c2

---

## 17. Legal & attribution
The Authentic 5e mode reproduces material from the **System Reference Document 5.2**
("SRD 5.2") by Wizards of the Coast LLC, available at https://www.dndbeyond.com/srd,
licensed under **CC BY 4.0** (https://creativecommons.org/licenses/by/4.0/legalcode).
Reproduce SRD rules freely with this attribution. Never reproduce published-adventure text
or excluded content (Artificer, non-SRD subclasses, branded monsters, named beings, the
Forgotten Realms). LitRPG mode is an **original homage** — capture the genre / Dungeon
Crawler Carl vibe without copying any of its text, world, or characters.
