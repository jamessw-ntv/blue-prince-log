# 🔁 Self-Improvement Loop

*The engine gets a little better every time it is played. Nothing learned is lost.*

A disciplined **capture → propose → review → fold** loop. It runs automatically at save
points and can be invoked any time with `review`.

## When it runs
- **On every save / end of session** — the GM does a short reflective pass.
- **On demand** — the player says `review`.
- **Deep pass** — spin up review agents (like the initial QA sweep) for a thorough audit.

## The After-Action Review (AAR) — what the GM records
After a scene or session, reflect and capture, briefly:
1. **What worked** — beats, choices, pacing the player leaned into.
2. **Friction & ambiguity** — where the GM had to *guess*; where a rule was unclear,
   missing, or contradictory; where the map or a branch diverged unexpectedly; where a
   number felt off (too easy / too lethal / too swingy).
3. **Proposed refinements** — concrete, each tagged `[rules]` `[logic]` `[content]`
   `[schema]` `[nuance]` `[balance]` and rated `High / Med / Low`.
4. **Player signal** — what they reacted well or badly to; tone / boundary notes.

Append it as a dated entry to `./LEARNINGS.md` (newest first).

## Folding learnings into canon — the safe "self-updating" step
Refinements are **proposed automatically, applied on review.** When the player says
`apply learnings` (or during a maintenance pass):
- Work the open items in `LEARNINGS.md`, make the edits to canon (the rules in
  `AI-DUNGEON-MASTER.md`, the adventures, the `state.json` schema, the dashboard), and mark
  each **Done** with its commit.
- Prefer the **smallest change that closes the most gaps** (root-cause over patch).
- After any rules/schema change, re-run the quick test (`adventures/the-crossroads-test.md`).

## Why a review gate, not blind auto-rewrite
Auto-editing the rules mid-play would introduce regressions and contradict saves already in
flight. The loop instead **captures continuously** and **applies deliberately** — so every
change is intentional, tested, and reversible (it's all in git). Across many sessions this
converges the engine toward *genuinely good* — the path from a 5-minute test, to a
30-minute campaign, to a large ongoing, self-refining world.
