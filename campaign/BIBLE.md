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
| `adventures/the-crossroads-test.md` | "The Ember Key" — 5-min engine test |
| `adventures/smoke-over-bramblewick.md` | First Rules-Light one-shot |

**In Notion (the PKM wiki + saves):** the **AI Dungeon Master hub** (with the agent bootstrap),
the module pages (GM Engine, the three Systems, Companions, Campaign Creation, Save & Load,
System UI Kit, Legal), and the **Campaigns** database (one page per save).

## Where it lives & the rules of the road
- **Notion** = the wiki + the saves. **This repo** = the dashboard + the portable docs.
- Everything is **self-contained** here and in Notion; **nothing** lives in any work repo.
- **Legal:** Authentic 5e reproduces SRD 5.2 (CC-BY-4.0, attributed); LitRPG is original homage.

## Status (2026-06-21)
Engine + dashboard live; turnkey load wired; **Gate 1 met** (the engine self-plays and
branches). One Rules-Light one-shot ready, one micro-test. **Next:** Gate 2 — dial in the
nuance (the story spine/map above, companion voting) and autoplay a full party scene. See
`./GOAL-STATE.md` for the gates and `./LEARNINGS.md` for the latest.
