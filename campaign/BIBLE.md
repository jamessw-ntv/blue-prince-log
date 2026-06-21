# 📖 The AI Dungeon Master — Bible

*The easy view. What this is, how the engine works, how a game is made, and where every piece
lives. If you read one file, read this — it links to all the rest.*

---

## What it is
A chat-based, single-player **D&D / LitRPG** run by an AI **Game Master** with an AI **party**.
You play one hero; the AI runs the world, the story, and your companions. Saves live in
**Notion**, so any future chat can resume. An optional **live second-screen dashboard** shows
the map + party, auto-refreshing each turn. Pick one of three rule systems and any story you
like — it's **one engine**, many games.

## Play in 30 seconds
1. Open a chat (with Notion connected) → say **"be my Dungeon Master."**
2. It reads the PKM hub, shows the **Main Menu**, and you pick **New** or **Continue**.
3. *(Optional)* open the live dashboard on a second screen: `jamessw-ntv.github.io/campaign/`.

*No file uploads needed — the Notion hub has an **AGENT — START HERE** block that boots it.*

## What you can do — actions & ways to play
**Ways to play:** load it from the PKM in any chat (no upload) or just say *"be my DM"* — one hero
+ 2–3 AI companions, in **Rules-Light**, **Authentic 5e**, or **LitRPG** (royalty-free modules next).
Optional **live dashboard** on a second screen; **save to Notion** and resume in any future chat. Set
**tone + content lines** and a **Freedom dial** (Linear → Guided → Open → Sandbox) per campaign.

**In a scene you can:**
- **Go anywhere, try anything** — open prompts, not menus; the GM reads your intent and the **Living
  Map** records everywhere you go (no path is forgotten).
- **Skill checks** — d20 + modifier vs a difficulty across every skill (Athletics, Stealth, Insight,
  Arcana, Persuasion…); advantage/disadvantage, help, and **fail-forward** (failure complicates, rarely dead-ends).
- **Combat** — initiative, attack, cast spells, use class abilities, move, bonus actions, reactions,
  conditions, **downed/death saves**, short/long **rests**.
- **Social play** — persuade, deceive, intimidate, read people; **turn NPCs and whole factions**.
- **Companions** — distinct personalities that **advise and vote** at forks (you decide; overriding
  shifts **approval**); high approval unlocks loyalty/personal beats; mistreat them and they leave.
- **Story choices** — a locked **spine** of main beats with open space between; **branching paths**
  and **real moral forks** with distinct endings (e.g. *destroy it / take the bargain / turn the pact*).
- **LitRPG extras** — level-ups as printed events, **loot boxes by rarity** (Luck-weighted),
  **showmanship** for bonus loot, sponsored choices, ironic **class grants**, achievements/titles, a System shop.

**Commands:** `main menu` · `save` · `give me my state block` · `dial it back` / `fade to black` ·
`continue` · `apply learnings`.

## The engine, at a glance — one engine, four layers
Only the middle two change per game:

| Layer | What it is | Changes per game? |
|---|---|---|
| **Engine core** | GM behaviour: narrate, resolve dice, voice companions, hold the story, save | ❌ Always the same |
| **Rules** | 🎲 Rules-Light · 📚 Authentic D&D 5e · 🧩 LitRPG | ✅ Swappable |
| **Content** | The story: a generated original, a royalty-free module, or a LitRPG crawl | ✅ Swappable |
| **Presentation** | The System UI + the live dashboard (one JSON state → HUD) | ❌ Always the same |

**Rules × Content are independent axes:** e.g. a published module → *Authentic 5e* rules; a
Dungeon-Crawler-style crawl → *LitRPG* rules; an original → *any* rules. A "module" is just a
chapter; a campaign is one or more chained. Everything serialises into **one save**.

## Design philosophy
A handful of principles drive every part of the build:
- **One engine, many games.** The engine core is constant; only the *rules* and the *story* swap.
  Build the system once, play any genre.
- **The story is data, played live.** A locked **spine** (a few beats that must happen) sits inside an
  open **sandbox**, and everything you actually do is written to an **append-only Living Map** —
  *explored space becomes canon.* The GM improvises freely but never retcons.
- **Rails are gravity, not fences.** Go anywhere; the world *pulls* you back with consequence, never an
  invisible wall. **Fail forward** — failure complicates, rarely dead-ends.
- **Companions are characters, not menus.** They have drives and flaws, **advise and vote** at forks,
  remember how you treat them (**approval**), and can leave.
- **The engine adapts and self-heals.** Difficulty, goals, and curveballs flex on the fly; if anything
  breaks mid-game the GM repairs it *in-world* and the story **picks back up** — it never hard-stops.
- **It gets better every time it's played.** Every session feeds a **self-improvement loop**; the
  engine can even **play itself** (autoplay) to harden between sessions.
- **Boring tech, on purpose.** Plain Markdown + JSON + a static HTML dashboard; Notion for saves. No
  build step, no lock-in — open it and read it.
- **Legal & original.** Authentic 5e reproduces the **SRD 5.2** (CC-BY-4.0, attributed); LitRPG is an
  **original homage**; open modules ingest under their CC licence.

## Story shape — a spine you must finish, freedom in between, a map of everywhere you go
There's a **locked main story** (a few beats that must complete) with an **open sandbox**
between them; whatever path you take is **recorded into a permanent map** (generated as you go,
never forgotten). How tight the rails are is a **per-campaign dial** (Linear → Guided →
Open → Sandbox). → **`./STORY-STRUCTURE.md`**.

## Your party
2–3 **companions**, each with a distinct voice, drive, flaw, signature ability, and an
**approval** track. At forks they **advise and vote**; you decide (overriding a favourite
costs approval). You can set their **personalities at Session Zero** and tune in play.

## Saving, loading & the live dashboard
- **Save** → a structured checkpoint to the **Campaigns** database in Notion (the human-readable
  truth) + the machine **`state.json`** (the dashboard's truth).
- **Load** → read the save, re-anchor tone + system, recap, resume on the exact scene.
- **Dashboard** → the GM overwrites `state.json` each turn and pushes; the HUD refreshes ~1 min.

## It gets better every time — the two loops
- **Self-improvement loop** — every save runs an After-Action Review → appends to
  `./LEARNINGS.md`; say `apply learnings` to fold fixes into canon. → **`./SELF-IMPROVEMENT.md`**
- **Autoplay** — the engine **plays itself** (a Player agent + voting companions + a DM + a
  Critic) to test and iterate without you. → **`./AUTOPLAY.md`**
- Both iterate toward a measurable **end goal**. → **`./GOAL-STATE.md`**

## The map of files (all the bits and pieces)
**In this repo, under `/campaign/`:**

| File | What it is |
|---|---|
| `index.html` | The live dashboard (map + party HUD) |
| `state.json` | The live machine save the dashboard reads |
| `BIBLE.md` | **This file** — the easy overview / front door |
| `AI-DUNGEON-MASTER.md` | The full manual: all rules, schemas, dashboard code, setup |
| `GM-INSTRUCTIONS.md` | GM live-mode + the loops, in brief |
| `GOAL-STATE.md` | The Definition of Done (13 criteria, 4 gates) |
| `STORY-STRUCTURE.md` | Spine / freedom dial / living map design |
| `AUTOPLAY.md` | The self-play harness (roles + voting + loop) |
| `SELF-IMPROVEMENT.md` | The learn-and-fold loop |
| `LEARNINGS.md` | The running record of what each session taught us |
| `PROJECT-HANDOFF.md` | Origin, backstory, decisions |
| `CONVERSION-PLAYBOOK.md` | Ingest any open module → a playable campaign |
| `adventures/the-crossroads-test.md` | "The Ember Key" — 5-min engine test |
| `adventures/smoke-over-bramblewick.md` | First Rules-Light one-shot |
| `adventures/emberfall.md` | **Flagship** — 30-min Rules-Light heroic campaign |
| `adventures/going-live.md` | LitRPG starter (game-show crawl) |
| `adventures/sunless-shrine.md` | Authentic 5e starter (SRD) |
| `adventures/converted-example.md` | Module-conversion worked example |

**In Notion (the PKM wiki + saves):** the **AI Dungeon Master hub** (with the agent bootstrap),
the module pages (GM Engine, the three Systems, Companions, Campaign Creation, Save & Load,
System UI Kit, Legal), and the **Campaigns** database (one page per save).

## Where it lives & the rules of the road
- **Notion** = the wiki + the saves. **This repo** = the dashboard + the portable docs.
- Everything is **self-contained** here and in Notion; **nothing** lives in any work repo.
- **Legal:** Authentic 5e reproduces SRD 5.2 (CC-BY-4.0, attributed); LitRPG is original homage.

## Status (2026-06-21) — ~90% to the goal
**Built, validated, and hardened.** All four gates are effectively cleared: the engine self-plays and
branches (Gate 1), party play + companion voting are dialed in (Gate 2), the **flagship *Emberfall***
passes the bar across all 6 classes / 3 routes / 4 endings (Gate 3), and breadth is done — a starter
in **every system** plus a **module-conversion pipeline** (Gate 4). Across **21 autoplay/stress runs**
— including a 5-agent comprehensive batch (full-stack **4.8**, adaptive **4.6**, adversarial **4.2**,
save/load **4.0**, a balance audit) — the engine held **without invisible walls or dead-ends**, and the
**Adaptive Director** (dynamic difficulty, curveballs, **self-healing**) is now canon. **Remaining:**
your one **blessing play** (the "is it fun" call no agent can make) + optional dashboard-render polish
(show approval + the story-map on the HUD). See `./GOAL-STATE.md` for the gates and `./LEARNINGS.md`
for the full audit trail.
