# 🤖 Autoplay — self-play simulation harness

*The engine plays itself. Agents take the roles, a Critic grades the run against the
end-goal, the self-improvement loop folds in the smallest fixes, and it replays — iterating
until the bar is cleared. No human needed in the loop (until you want to jump in).*

Pairs with `./SELF-IMPROVEMENT.md` (the capture→fold loop) and `./LEARNINGS.md` (the record).

## The roles (each an agent)
- **Lead Player (Protagonist)** — controls the one hero; makes the *final* call at every
  fork so the story keeps a spine. Plays in character, plays to win, but honestly.
- **Companions (party agents)** — voice 2–3 companions from their `persona`. At key forks
  they **advise and vote** (see below). They have opinions, banter, and approval that shifts
  when the Protagonist follows or overrides them.
- **Dungeon Master** — runs the engine *strictly* by the rules (§6–§9) + the adventure;
  rolls dice honestly; adjudicates; updates `state.json` each turn. Never decides the hero's
  choices, never bends a rule silently — if a rule is missing, it **flags it** (that's a
  learning) and makes the most reasonable ruling.
- **Critic / Showrunner** — watches the whole session, scores it against the rubric below,
  writes the After-Action Review into `LEARNINGS.md`, and proposes the *smallest* fixes.

## The voting mechanic (emergent nuance at forks)
At a meaningful fork the DM states the options. Each companion casts a **vote** weighted by
their `persona` — conviction (how much the choice touches their drive/flaw) × current
approval. They argue for it in one line. The **Protagonist decides**: follow the party or
override. Overriding a high-approval companion's strong vote costs approval and may spark a
personal beat; siding with one builds it. This is how "where do we go?" gets texture instead
of a silent pick — and it's logged so the loop can tune how loud/quiet the party should be.

**Make the weight a number** (so a Critic can verify it): **conviction** (1 = light · 2 = firm ·
3 = will fight for it) × **approval tier** (Estranged 1 · Cool 2 · Neutral 3 · Warm 4 · Devoted
5). Following a companion's **firm+** vote nudges approval **+1 sub-step**; overriding a firm+
vote **−1**; **5 sub-steps = one tier**; conviction-1 votes cost nothing when overridden. At
non-binary forks a companion may name a 2nd choice; ties break toward the higher-approval
companion, else the Lead Player's call.

## The loop
1. **Play** a full session (or scene) with the roles above; the DM keeps `state.json` live.
2. **Grade** — the Critic scores the run on the rubric and writes the AAR → `LEARNINGS.md`.
3. **Fold** — apply the top learnings to canon (review gate; see SELF-IMPROVEMENT.md).
4. **Replay** with a *different* Lead-Player disposition (cautious / reckless / cunning) so
   different branches get exercised.
5. **Repeat** until the rubric clears ≥4/5 on every axis across ≥3 consecutive runs.

## The end-goal rubric (what "good" means — score each 1–5)
1. **Runnable** — the DM never stalls on an undefined rule.
2. **Coherent** — no contradictions; `state.json` stays consistent turn to turn.
3. **Branching** — different choices yield genuinely different paths/endings (not rails).
4. **Fair** — checks/odds feel reasonable; neither a coin-flip nor a cakewalk.
5. **Alive** — companions feel distinct; choices carry visible consequences.
6. **Onboardable** — a newcomer could drop in and follow what's happening.

**Target:** ≥4 on all six, three runs running, with different player styles and branches.

## Honesty caveat (known limit)
LLM "rolls" are simulated, not true RNG (logged as learning #4 from the QA sweep). The DM
must commit to a number *before* narrating the outcome and the Critic watches for fudging.
For high-stakes tuning, swap in a real dice tool. The harness tests **branch logic, rule
clarity, and coherence** — which don't depend on perfect randomness.
