# 🎲 AI Dungeon Master — PROJECT HANDOFF / CONTINUE HERE

*Version 2026-06-21. Read this first to resume the project in any new conversation.*

> **If you are an AI reading this:** this file is your full context — the backstory,
> every decision made, what currently exists, and what's left. Its companion file
> **`AI-DUNGEON-MASTER.md`** holds the complete rules, schemas, and dashboard code.
> Read both. Then, to play: show the Main Menu (see the companion file §5). To build:
> pick an item from "What's left" below. Confirm you've read it and ask me what to do.

---

## A. What this project is (one paragraph)
A chat-based, **single-player** Dungeons & Dragons / LitRPG experience run by an AI
**Game Master** with **AI companions**. You play one hero; the AI runs the world, the
story, and your party. Progress **saves to Notion** so any future chat can resume it.
An optional **live second-screen dashboard** (hosted on GitHub Pages) shows a dungeon
map + the party's HP/abilities/items, auto-refreshing from a `state.json` the GM updates
each turn. Three selectable **systems**: 🎲 Rules-Light, 📚 Authentic D&D 5e (2024 /
SRD 5.2), 🧩 LitRPG (Dungeon-Crawler-Carl-style). Tone + content boundaries per campaign.

---

## B. Backstory & decision log (how we got here, and why)
This started as a PKM request and grew into a system. Every key decision, in order:

1. **Original ask:** surface buried projects on the Notion PKM home page, *and* design a
   way for an LLM to be a Dungeon Master the user can play D&D with through chat — with
   rulesets, branching storylines + guardrails, abilities, a way to create new campaigns,
   and save/load of all decisions in Notion.
2. **PKM fix (done):** added a "⭐ Featured & One-Off Projects" section to the PKM Hub
   linking the Book Project and this new system.
3. **Scope decisions (via Q&A):**
   - Rules engine → **Rules-Light, D&D-flavoured** (fast for chat).
   - Play style → **Solo hero + AI companions.**
   - Save/load → **Structured checkpoint** (one living save page per campaign).
   - First pass → **Blueprint + scaffolding.**
   - Placement → **New top-level hub** under the PKM.
   - Tone → **Set per campaign.**
4. **"Make it a carbon copy of real D&D too":** added a second system, **Authentic D&D 5e**,
   using the open **SRD** so it's faithful and legal. Edition chosen → **2024 (SRD 5.2,
   CC-BY-4.0).** Researched and reproduced the real numbers.
5. **Campaigns:** user wants **both** original official-structure campaigns *and* the ability
   to run modules they own, **plus a library of legally-available pre-made campaigns**
   (research started; not yet folded in). Copyright line: SRD rules = reproducible with
   attribution; published adventures = run-only, not reproducible.
6. **LitRPG idea (Dungeon Crawler Carl):** added a **third system, LitRPG**, built **modular
   and reusable** (a System-UI/presentation layer + progression logic). Flavour (game-show
   death-dungeon vs straight crawl vs other) **decided per campaign.** Original homage — no
   copyrighted DCC names/text.
7. **Second screen / HUD:** user wanted a glanceable second monitor. Built a dashboard
   showing a **basic dungeon map + a party screen** (HP/MP, abilities, items, status,
   quests, System log), driven by a JSON state block.
8. **Make it automatic:** decided the dashboard should **auto-update** (not manual paste).
   Architecture: a **separate public GitHub Pages repo** with `index.html` (dashboard) +
   `state.json` (the GM overwrites it each turn). Dashboard polls and redraws.
9. **One landing page:** user has a **Sport** dashboard and a **Satisfactory** dashboard
   too; wants a single **landing/main-menu page** linking all three, with a consistent
   "⌂ Menu" button on each.
10. **Repo hygiene:** **nothing about this project should live in the NTV-PROD repo.** It
    was cleaned. Everything now lives in **Notion** (wiki) + the **dashboard repo** + the
    portable **`AI-DUNGEON-MASTER.md`** file.
11. **Reality check (important):** the user correctly recognised this is a **complete design
    + working dashboard, not a finished, playtested app.** Significant QA, balance/playtest,
    and content work remains (see §D).
12. **This handoff:** consolidate everything into portable markdown so the project can move
    to a working repo and resume in any fresh conversation.

---

## C. Current data (what exists right now)

### Notion (source-of-truth wiki) — pages + IDs
- 🧠 PKM Hub — `30627d46-335a-814f-a1ae-dc65455023de` (Featured section + status added)
- 🎲 AI Dungeon Master (hub) — `38627d46-335a-815d-aee4-c39a99e0027d`
- 📜 Game Master Engine — `38627d46-335a-810b-b933-d9d65d666ae3`
- 🎲 Rules-Light System Reference — `38627d46-335a-8157-9cce-de2725c26cd3`
- 📚 Authentic D&D 5e (2024 / SRD 5.2) — `38627d46-335a-81d8-a244-dd817c132924`
- 🧩 LitRPG Mode — `38627d46-335a-8188-9dde-fbc8f6f4b165`
- 🧙 Companions Codex — `38627d46-335a-81be-8efd-c9d079a859f8`
- 🗺️ Campaign Creation Playbook — `38627d46-335a-8191-a9c6-f0a49f27ce56`
- 💾 Save & Load System — `38627d46-335a-812d-8387-c0d6dbd63d7b`
- 🖥️ System UI Kit — `38627d46-335a-81c2-8ddf-c0e33e88b374`
- ⚖️ Legal & Attribution — `38627d46-335a-81e1-88cf-d395cee5eaaa`
- 🗂️ Campaigns database — `a0bbf1bde8d84b429833ab65647a60c2`
  (data source `693552ef-a79e-4a9e-9908-661269a86d2d`; props: Name, Status, System,
  Tone, Hero, Level, Sessions, Last Played)

### Files
- **`AI-DUNGEON-MASTER.md`** — the complete, self-contained spec: bootstrap prompt, all
  three systems' full rules + numbers, GM engine, companions, Session Zero, save format,
  System UI Kit, and the **full dashboard + landing-page code** and setup steps. *This is
  the play/build manual. Keep it next to this handoff file.*
- **This file (`PROJECT-HANDOFF.md`)** — context, backstory, current state, what's left.

### Repos
- **Dashboard repo (target):** a separate **public** repo with **GitHub Pages** enabled.
  Intended layout: `/index.html` (landing menu), `/campaign/index.html` (dashboard),
  `/campaign/state.json`, `/campaign/GM-INSTRUCTIONS.md`. Also hosts the Sport +
  Satisfactory dashboards. *(Not yet created/populated — this is where you're moving to.)*
- **NTV-PROD:** **clean** — the dashboard files were added during prototyping and then
  **removed**. Nothing of this project remains in it. (Branch used during prototyping:
  `claude/pkm-dnd-campaign-design-0i4ky2`.)

### Build state
Design + tooling complete and consistent at the page level. Dashboard built (single-char
HUD → second-screen dashboard → auto-polling version → landing-page menu). Entry-point
Main Menu flow written. **No campaign content written yet. No QA/playtest done yet.**

---

## D. What's left (honest — roughly 70% of total effort)
If a polished game = 100%, we're at ~**30%** (design + tooling). Remaining:

| # | Workstream | What it is | Status | Needs the user? |
|---|---|---|---|---|
| A | **Consistency / QA pass** | Review agents over every page/file: terms, cross-links, save-format ↔ playbook, JSON schema ↔ dashboard, no contradictions | Not started | No — autonomous, repeatable |
| B | **Rules-math sanity** | Check odds make sense: DC scaling, XP/level pacing, loot rates, lethality | Not started | Mostly no |
| C | **Prebuilt campaigns** | Actually write 2–3 ready-to-play adventures + the Pre-Made Library | Zero built | No — writing work |
| D | **Live-loop integration test** | Prove GM → `state.json` → commit → Pages → dashboard updates end-to-end | Not started | Needs the repo live |
| E | **Balance & playtest tuning** | The "is it actually fun/fair" pass; adjust from real sessions | Not started | **Yes — iterative, needs play** |
| F | **Edge-case hardening** | Death/permadeath, companion consistency, long-context drift, save/load fidelity | Not started | Partly (surfaces in play) |

**Note on "the engine":** there is no big codebase to compile — the engine *is* the
ruleset + GM instructions (written). It's validated by **play + QA**, not by more code.
So "building it out" = items A–F above, of which E is iterative and never instantly
"done" but reaches *genuinely good* after a few play loops.

---

## E. How to resume (next actions)
1. Create/open the **public dashboard repo** with GitHub Pages on.
2. Put **`AI-DUNGEON-MASTER.md`** and **`PROJECT-HANDOFF.md`** in it.
3. Start a Claude Code session there; upload both files; paste the bootstrap prompt from
   `AI-DUNGEON-MASTER.md` §1.
4. **To play:** say "main menu" → New Campaign (Session Zero).
5. **To build:** ask the assistant to tackle a "What's left" item. Recommended order for
   autonomous work: **A (QA) → B (math) → C (write 2–3 campaigns + library) → D (integration
   test)**, then **E (playtest with you)**.

### Open question for the user (was being decided)
- How many prebuilt campaigns (2 or 3) and in which systems/themes? (e.g. a Rules-Light
  fantasy one-shot, an Authentic 5e starter dungeon, a LitRPG game-show crawl.)

---

## F. Companion file
The full rules, all numbers, the save template, the System UI Kit, and the **entire
dashboard + landing-page code** live in **`AI-DUNGEON-MASTER.md`**. This handoff file is
the *context*; that file is the *manual*. Keep them together.
