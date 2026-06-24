# Templates — reusable building blocks

A **template** is a small, standard cluster of machines you build over and over —
think of it as a **blueprint**: once you know what "an Iron Rod bank" or "a
Reinforced Iron Plate cell" looks like, you stamp it wherever it's needed. The
whole plan is built from a handful of these, which is what makes it feel like
Lego instead of spaghetti.

- A **bank / area** (the §N cells in the app) is one template stamped down: **N
  copies of the same machine** making one item.
- A **district** is a column of these banks for one material family.
- A **build step** says *"place 2× the RIP cell"* — that's one template.

> **Blueprint tip:** once you unlock the **Blueprint Designer** (Tier 4), save the
> most-repeated cells (rod/screw, RIP, rotor, smelter banks) as real in-game
> blueprints. Then building a district is dropping blueprints in a row — the
> single biggest anti-tedium win in the game.

## Convention for every template

```
┌─ inputs (belted/piped in from the left) ──────────────┐
│   [machine] [machine] [machine] ...  (a row of N)     │  →  output merged
└───────────────────────────────────────────────────────┘     to one belt (right)
```

Build every cell **left-to-right, raw on the left, product on the right**, on a
raised foundation pad. Feed inputs with a **smart-splitter manifold** along the
back; merge outputs along the front. The app's **exact-placement** drill-down
(click any area block in 📐 **Blueprints**) draws this precisely — every machine,
splitter, merger, belt and storage buffer.

## Where the numbers live (not duplicated here)

The exact per-machine recipe, I/O rates and footprint for **every** template —
and every sub-component (Supercomputer, Cooling System, Dark Matter Crystal,
Ficsite Trigon, …) — live in **two** always-current places, so they're never
hand-copied (and never drift) into this file:

- the **🧩 Templates** tab of `factory-network.html` — searchable, with a visual of
  each cell and "made in / used by" links; and
- **VERIFICATION.md** — the same recipes cross-checked against the wiki/SCIM, with
  the corrections log.

Open a template in the app to see its spec **and which districts use it**. Build
by repeating templates — never improvise a one-off.
