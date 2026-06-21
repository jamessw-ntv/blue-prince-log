# 🎯 Goal State — Definition of Done

*The north star. The autoplay loop (`AUTOPLAY.md`) and the self-improvement loop
(`SELF-IMPROVEMENT.md`) iterate toward **this** until every box is ticked. "Done" is not a
feeling — it's the criteria below, measured.*

---

## The end state, in one breath
Open any fresh Claude chat, point it at the PKM Dungeon Master hub (**no uploads**), say
*"be my DM."* It shows the menu; you **start or resume** a campaign in **any of the three
systems** (Rules-Light / Authentic 5e / LitRPG) with **any content source** (generated /
royalty-free module / LitRPG crawl), and play a session that is **coherent, fair, and
alive**, with a **customizable AI party**, while a **live second-screen dashboard** tracks
it. Every session makes the engine **measurably better** (the self-improvement loop), and the
engine can **play itself** (autoplay) to validate and keep improving without you. Everything
lives in **Notion + this repo**; nothing is lost between sessions.

---

## Acceptance criteria (all must pass — each is checkable)

| # | Criterion | Pass condition | How verified |
|---|---|---|---|
| 1 | **Turnkey cold-load** | Fresh session + Notion only → menu in 1 reply, no uploads, no missing-context questions | Cold-session test passes 3× |
| 2 | **Save/load fidelity** | Resume in a NEW session and hero stats, party persona+approval, tone/boundaries, quests, and current scene reconstruct **exactly** (no invented numbers) | Round-trip diff clean; `state.json` is the complete, authoritative save |
| 3 | **Rules completeness** | DM never stalls on an undefined rule across a full session, in each system | Autoplay **Runnable ≥ 4.5**; zero "invented a core rule" flags in the AAR |
| 4 | **Coherence** | No contradictions; state consistent turn to turn | **Coherent = 5** across runs |
| 5 | **Meaningful branching** | Different choices → genuinely different paths and ≥3 reachable endings; the map diverges | **Branching ≥ 4**; autoplay dispositions reach different states |
| 6 | **Fairness / balance** | Odds reasonable — not a coin-flip, not a cakewalk; lethality has stakes but isn't punishing | **Fair ≥ 4** across ≥3 runs; DC/HP/XP pacing within target bands |
| 7 | **Alive party** | 2–3 companions are distinct, voice consistently, **advise + vote** at forks, approval shifts and gates content; player can set **personality sliders** at Session Zero and tune in play | **Alive ≥ 4**; `persona` serialized; a blind reader tells them apart from the save alone |
| 8 | **Onboarding** | A new human is playing in ~2 min: human "start here" exists, ready adventures are menu-selectable, Rules-Light recommended for newcomers, Notion/dashboard explicitly optional | **Onboardable ≥ 4.5**; newcomer reaches play in ≤2 decisions |
| 9 | **Live dashboard loop** | GM writes `state.json` → commit → Pages → dashboard renders, end-to-end, ≤ ~1 min | One real cycle confirmed visually |
| 10 | **Self-improvement loop** | Every save appends an AAR to `LEARNINGS.md`; `apply learnings` folds fixes into canon; scores trend up run-over-run | `LEARNINGS` grows; rubric trend is upward |
| 11 | **Autoplay convergence** | Engine self-plays a full session (Player + party-vote + DM + Critic) and the loop reaches **≥4/5 on all axes across ≥3 consecutive runs** with different dispositions | An autoplay batch clears the bar |
| 12 | **Content depth** | ≥1 proven Rules-Light campaign (~30 min+), a starter in each other system, the pre-made library scaffold — all in one save schema | Each autoplays to a satisfying ending at ≥4 |
| 13 | **Self-contained & legal** | All in Notion + this repo; nothing in any work repo; SRD attribution present; LitRPG original homage only | Present & checked |

---

## The staged gates (advance when each passes)

- **Gate 1 — Engine proven (micro).** The Ember Key autoplays across ≥3 dispositions to
  distinct endings; Runnable & Coherent ≥4. → **MET this iteration** (3 paths, 2 endings;
  the 3 micro-fixes folded in).
- **Gate 2 — Nuance dialed.** Map divergence, action handling, **companion voting**, and the
  Rules-Light gaps (recharge / multiattack / save-ends / downed / attack-mod / "scene")
  resolved; a **party scene** (Bramblewick opening) autoplays at ≥4 *with voting*.
- **Gate 3 — A 30-minute campaign to confidence.** One full Rules-Light campaign autoplays
  **and** human-plays to a satisfying ending at ≥4 on all axes; save/load proven across
  sessions.
- **Gate 4 — The ongoing, self-refining world.** A large campaign that runs indefinitely,
  saves/loads faithfully, self-improves each session; all three systems covered; turnkey
  cold-load passes.

## Done-done
**All 13 criteria pass, all 4 gates clear, and an autoplay batch *and* one human session both
score ≥4/5 on every rubric axis.** Then: open a chat, say *"be my DM,"* and it just works —
well.
