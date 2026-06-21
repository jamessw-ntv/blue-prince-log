# 📚 Learnings Log

Append-only record of what each session taught us and the refinements it proposed. Newest
first. See `./SELF-IMPROVEMENT.md` for the loop. Mark items **Done** when folded into canon.

---

## 2026-06-21 — Gate 2 autoplay: party + voting (run 2, consensus lead) + folded fixes
A consensus-seeker lead self-played the same opening; **also ≥4 on all axes** (Runnable 4,
Coherent 5, Branching 4, Fair 4, Alive 5, Onboardable 5). Confirmed the vote-weighting cleanly
broke a 3-option fork (Corwin's bond > Lysa's curiosity) and that a companion voting *against
his own flaw* is great texture. **Biggest gap (both runs):** companions + pre-gens lacked
printed stat blocks, forcing the DM to invent modifiers — capping Runnable/Fair at 4.

### [DONE] folded into canon (the loop's fix step)
- **§7:** "meets AC = hit"; mindless/construct foes skip the dying clock; forewarned-vs-hunting surprise default.
- **§10:** companion sheet now requires a **stat block** (mods · AC · HP · attack bonus) + signature definition + persona; **approval moves in sub-steps** (5 = one tier).
- **AUTOPLAY:** votes are now a **number** (conviction 1–3 × approval tier 1–5; ±1 sub-step; 2nd-choice + tie-break).
- **Bramblewick:** full **ability arrays** for the 3 pre-gens; **stat blocks + signature defs** for Corwin & Lysa.
- **STORY-STRUCTURE:** node `type` list noted as open.

*Next: run 3 (post-fix, fresh disposition) to confirm Gate 2's ≥3-consecutive-runs bar — expect Runnable/Fair → 5.*

---

## 2026-06-21 — Gate 2 autoplay: party + voting (run 1, headstrong lead)
A headstrong Lead Player self-played *Smoke Over Bramblewick* Act 1 → the Act 2 entry-shaft
fight, with companion **voting** at forks. **Scored ≥4 on all six axes** (Runnable 5,
Coherent 5, Branching 4, Fair 4, Alive 5, Onboardable 4). Combat ran clean on the new §7
clarifications — **nothing stalled**. The override→cost→repair approval loop was the most alive
part; Corwin & Lysa stayed clearly distinct. The Living-Map `story` schema held (the agent even
added `beatCount` and encoded vote outcomes on edges).

### [open] to fold AFTER the consensus run (keep canon stable mid-validation)
- **§7:** state explicitly that a total **meeting** AC hits; add the *forewarned-but-not-hidden
  vs. a hunting foe = no surprise* default.
- **AUTOPLAY:** give votes a **number** — conviction (1 light / 2 firm / 3 will-fight-for-it) ×
  approval tier (Estranged 1 → Devoted 5); follow/override of a firm+ vote = ±1 sub-step;
  5 sub-steps = one tier; conviction-1 costs nothing; 2nd-choice + tie-break at non-binary forks.
- **§10:** define approval **step size** (sub-tier nudges, not whole-tier jumps).

*Run 2 (consensus-seeker) in flight; then fold these and run a 3rd to confirm Gate 2's
≥3-consecutive-runs bar.*

---

## 2026-06-21 — Gate 2: folded story-structure + Rules-Light combat into canon
Folded into `AI-DUNGEON-MASTER.md`: §7 gained **combat clarifications** (attack bonus,
multiattack, recharge, "save ends", downed/dying with Mature-default lethality, surprise); §11
Session Zero now sets the **Freedom dial + spine + Living Map** and gives companions a tunable
**persona** that **votes** at forks. Unblocks runnable party play. **Done.**
*Next:* autoplay the Bramblewick opening with companion voting → score vs rubric → iterate.

---

## 2026-06-21 — Autoplay iteration 1 (The Ember Key · 3 dispositions)
Three independent Lead-Player agents (Cautious / Reckless / Cunning) self-played the
micro-test. **The engine branches:** three different paths, two distinct endings (PERFECT ×2,
GOOD ×1); checks resolved; fail-forward intact. Avg rubric — Runnable 4.3, Coherent 5,
Branching 2.7, Fair 4.3, Onboardable 4.3.

### [content] DONE — model goal items, state Ash's attack line, define "scene"
Folded into `the-crossroads-test.md` this iteration (the loop closing): Ash's shortsword now
prints `+4, 1d6+2`; Node 2A states Ash acts first; "scene" = the whole crypt; the Ember
Key/Charm are added to `items` on a win.
### [design] LOW — signature ability disjoint from the optimal ending
Quick Hands (first DEX check) never fires on the Perfect line (lever → study INT). Fine for a
micro-test; for real heroes, ensure signature abilities get a natural moment on the best path.
### [design] NOTE — branching is a "diamond" by design
2A/2B both funnel into Node 3; only Node 3 yields distinct endings. Expected for a smoke-test;
real campaigns need wider divergence (Gate 2 in `GOAL-STATE.md`).

---

## 2026-06-21 — Initial QA sweep (4 review agents, pre-play)
A deep self-improvement pass run by review agents over the engine + the *Smoke Over
Bramblewick* one-shot, before first play. Backlog below, highest-leverage first.

### [schema] HIGH — `state.json` is a dashboard schema, not a real save
A cold DM loading only `state.json` has no ability modifiers, no AC, no initiative, and no
tone / boundaries / system — so it must invent ~a dozen numbers, and two DMs produce
different fights from the same save. **Fix:** add per-character `abilities_mods` (the six
mods), `ac`, `init`; add top-level `system`, `tone`, `boundaries`. Make `state.json` the
authoritative save; Notion an optional mirror. *(Modelled in `the-crossroads-test.md`.)*
**Status: Open.**

### [rules] HIGH — Rules-Light §7 omits mechanics the adventures rely on
`recharge 5–6`, monster **multiattack** ("two per round"), **"save ends"**, **psychic /
damage types**, and a concrete **downed / stabilise** procedure are used by Bramblewick but
never defined in §7 (they are 5e idioms). **Fix:** add a "Running enemies & rulings in
Rules-Light" block defining recharge, monster multiattack, how conditions end, and the
downed procedure. **Status: Open.**

### [content] HIGH / marquee — Companions have personality but no serialization or sliders
Voice / drive / flaw / approval live only in prose, vanish from `state.json`, and there is
**no player customization**. **Fix:** the Companion Sliders design — five axes (Warmth,
Caution, Bond, Levity, Voice) + an archetype tag + approval-driven behaviour, serialized as
a `persona` object on each companion and surfaced on the dashboard (approval chip +
sliders). **Status: Open.**

### [logic] MED — XP-vs-milestone and MP-vs-cooldown label mismatch
The UI shows `XP __/__` and Lysa carries `mp`, but Rules-Light uses milestone leveling and
slots / cooldowns, not XP / MP. **Fix:** reconcile the labels (hide XP / MP for Rules-Light,
or define them). **Status: Open.**

### [onboarding] MED — The docs address the AI, not a human; the ready adventure isn't in the menu
No human "start here"; Notion / dashboard read as required, not optional; Help lacks a
"how do I take an action" example; Bramblewick is not selectable from New Campaign. **Fix:**
add a human front-door, wire the pre-mades into the menu, mark Notion / dashboard optional,
add a worked first-turn example, and recommend Rules-Light for newcomers. **Status: Open.**

### [content] MED — *Smoke Over Bramblewick* story patches
Reconcile the Burn ending vs keeping the bell / Miller's Hammer; give Bram (who caused the
disaster) a real payoff; specify the Quelling-rite action economy and a fallback if the
party skips Coll / the Hammer (soft-lock risk). **Status: Open.**

### [schema / QoL] LOW–MED — Dashboard upgrades
Approval chip per companion, a dice / checks feed beside the System Log, quest threads +
objectives, and rendering attributes / achievements (or documenting them as in-chat only).
**Status: Open.**

### [test] HIGH — Prove the live loop end-to-end
Observe one full GM → `state.json` → commit → Pages → dashboard-refresh cycle. **Status: Open.**

### [balance] ONGOING — Playtest tuning
Odds, pacing, lethality. Needs real play; cannot be closed autonomously. **Status: Open
(iterative).**
