# 📚 Learnings Log

Append-only record of what each session taught us and the refinements it proposed. Newest
first. See `./SELF-IMPROVEMENT.md` for the loop. Mark items **Done** when folded into canon.

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
