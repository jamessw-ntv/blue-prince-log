# Templates — reusable building blocks

A **template** is a small, standard cluster of machines you'll build over and
over. Think of it as a **blueprint**: once you know what "an Iron Rod bank" or "a
Reinforced Iron Plate cell" looks like, you stamp it down wherever a module needs
one. **Modules are just compositions of templates.**

This is the layer that makes the whole plan feel like Lego instead of spaghetti:

- A **step** in `build-guide.md` says *"place 2× the RIP cell (T-RIP)."*
- A **module** is a list of templates and how many of each.
- A **template** (here) is the exact machine spec for that one cell.

> **Blueprint tip:** once you unlock the **Blueprint Designer** (Tier 4), actually
> save the most-repeated templates (T-ROD-SCREW, T-RIP, T-ROTOR, smelter banks)
> as real in-game blueprints. Then building a module is dropping blueprints in a
> row. That's the single biggest anti-tedium win in the game.

Each template lists: the **building**, the **recipe**, the **per-machine I/O**,
a rough **footprint** (in foundations; 1 foundation = 8 m), and a build tip. All
rates are at **100 % clock** — underclock the whole cell if you want less output
now (no rebuild later).

---

## Convention for every template

```
┌─ inputs (belted/piped in from the left) ──────────────┐
│   [machine] [machine] [machine] ...  (a row of N)     │  →  output merged
└───────────────────────────────────────────────────────┘     to one belt (right)
```

Build every cell **left-to-right, raw on the left, product on the right**, on a
raised foundation pad. Feed inputs with a **smart-splitter manifold** along the
back; merge outputs along the front.

---

## Tier 0–2 templates (ingots & basic parts)

| ID | Template | Building | Recipe | In / machine | Out / machine | Footprint |
|----|----------|----------|--------|--------------|---------------|-----------|
| **T-IRON** | Iron Ingot bank | Smelter | Iron Ingot | 30 Iron Ore | 30 Iron Ingot | 1×2 / smelter |
| **T-COPPER** | Copper Ingot bank | Smelter | Copper Ingot | 30 Copper Ore | 30 Copper Ingot | 1×2 / smelter |
| **T-CATERIUM** | Caterium Ingot bank | Smelter | Caterium Ingot | 45 Caterium Ore | 15 Caterium Ingot | 1×2 / smelter |
| **T-PLATE** | Iron Plate cell | Constructor | Iron Plate | 30 Iron Ingot | 20 Iron Plate | 1×2 / machine |
| **T-ROD** | Iron Rod cell | Constructor | Iron Rod | 15 Iron Ingot | 15 Iron Rod | 1×2 / machine |
| **T-SCREW** | Screw cell | Constructor | Screw | 10 Iron Rod | 40 Screw | 1×2 / machine |
| **T-WIRE** | Wire cell | Constructor | Wire | 15 Copper Ingot | 30 Wire | 1×2 / machine |
| **T-CABLE** | Cable cell | Constructor | Cable | 60 Wire | 30 Cable | 1×2 / machine |
| **T-CONCRETE** | Concrete cell | Constructor | Concrete | 45 Limestone | 15 Concrete | 1×2 / machine |
| **T-COPSHEET** | Copper Sheet cell | Constructor | Copper Sheet | 20 Copper Ingot | 10 Copper Sheet | 1×2 / machine |

## Tier 3–4 templates (steel & frames)

| ID | Template | Building | Recipe | In / machine | Out / machine | Footprint |
|----|----------|----------|--------|--------------|---------------|-----------|
| **T-STEEL** | Steel Ingot bank | Foundry | Steel Ingot | 45 Iron Ore + 45 Coal | 45 Steel Ingot | 2×2 / foundry |
| **T-BEAM** | Steel Beam cell | Constructor | Steel Beam | 60 Steel Ingot | 15 Steel Beam | 1×2 / machine |
| **T-PIPE** | Steel Pipe cell | Constructor | Steel Pipe | 30 Steel Ingot | 20 Steel Pipe | 1×2 / machine |
| **T-RIP** | Reinforced Iron Plate cell | Assembler | Reinforced Iron Plate | 30 Iron Plate + 60 Screw | 5 RIP | 2×3 / machine |
| **T-ROTOR** | Rotor cell | Assembler | Rotor | 20 Iron Rod + 100 Screw | 4 Rotor | 2×3 / machine |
| **T-FRAME** | Modular Frame cell | Assembler | Modular Frame | 3 RIP + 12 Iron Rod | 2 Modular Frame | 2×3 / machine |
| **T-EIBEAM** | Encased Industrial Beam | Assembler | Encased Industrial Beam | 18 Steel Beam + 36 Concrete | 6 Encased Beam | 2×3 / machine |

> **The screw problem:** T-ROTOR and T-RIP eat screws, and T-SCREW needs rods, so
> the **T-ROD → T-SCREW → (T-RIP / T-ROTOR)** chain dominates early modules. This
> is the #1 place the alt recipe **Cast Screw** (iron ingot → screw, skips rods)
> pays off — it deletes whole rows of T-ROD/T-SCREW. Build the standard version
> first; swap the cell when you unlock the alt.

## Tier 4–5 templates (machines & wiring)

| ID | Template | Building | Recipe | In / machine | Out / machine | Footprint |
|----|----------|----------|--------|--------------|---------------|-----------|
| **T-STATOR** | Stator cell | Assembler | Stator | 15 Steel Pipe + 40 Wire | 5 Stator | 2×3 / machine |
| **T-MOTOR** | Motor cell | Assembler | Motor | 10 Rotor + 10 Stator | 5 Motor | 2×3 / machine |
| **T-SMARTPLATE** | Smart Plating cell | Assembler | Smart Plating | 2 RIP + 2 Rotor | 2 Smart Plating | 2×3 / machine |
| **T-VERSFRAME** | Versatile Framework cell | Assembler | Versatile Framework | 1 Modular Frame + 12 Steel Beam | 2 Versatile Framework | 2×3 / machine |
| **T-AUTOWIRE** | Automated Wiring cell | Assembler | Automated Wiring | 2.5 Stator + 50 Cable | 2.5 Automated Wiring | 2×3 / machine |
| **T-PLASTIC** | Plastic line | Refinery | Plastic | 30 Crude Oil | 20 Plastic (+10 Heavy Oil Residue) | 2×4 / refinery |
| **T-RUBBER** | Rubber line | Refinery | Rubber | 30 Crude Oil | 20 Rubber (+20 Heavy Oil Residue) | 2×4 / refinery |
| **T-CIRCUIT** | Circuit Board cell | Assembler | Circuit Board | 15 Copper Sheet + 30 Plastic | 7.5 Circuit Board | 2×3 / machine |
| **T-COMPUTER** | Computer cell | Manufacturer | Computer | 10 Circuit Board + 20 Cable + 40 Plastic | 2.5 Computer | 3×4 / machine |
| **T-HMFRAME** | Heavy Modular Frame cell | Manufacturer | Heavy Modular Frame | 10 Modular Frame + 20 Steel Pipe + 10 Encased Beam + 120 Screw | 2 Heavy Modular Frame | 3×4 / machine |

## Tier 6–9 templates (end-game)

*These are firmed up against the verification pass and the production planner —
each is a Manufacturer / Blender / Particle Accelerator / Quantum Encoder cell:*

| ID | Template | Building | Makes |
|----|----------|----------|-------|
| **T-MODENGINE** | Modular Engine cell | Manufacturer | Modular Engine (2 Motor + 15 Rubber + 2 Smart Plating) |
| **T-ACU** | Adaptive Control Unit cell | Manufacturer | ACU (5 Automated Wiring + 5 Circuit Board + 1 Heavy Modular Frame + 2 Computer) |
| **T-ALUMINGOT** | Aluminium ingot line | Refinery + Foundry/Blender | Alumina → Aluminum Scrap → Aluminum Ingot |
| **T-ADS** | Assembly Director System cell | **Assembler** | ADS (2 ACU + 1 Supercomputer) |
| **T-MFG** | Magnetic Field Generator cell | **Assembler** | MFG (5 Versatile Framework + 2 EM Control Rod) |
| **T-TPR** | Thermal Propulsion Rocket cell | Manufacturer | TPR (5 Modular Engine + 2 Turbo Motor + 6 Cooling System + 2 **Fused Modular Frame**) |
| **T-PASTA** | Nuclear Pasta cell | Particle Accelerator | Nuclear Pasta (200 Copper Powder + 1 Pressure Conversion Cube) |
| **T-SCULPTOR** | Biochemical Sculptor cell | **Blender** | Biochemical Sculptor (1 ADS + 80 Ficsite Trigon + 20 Water → 4) |
| **T-AISERVER** | AI Expansion Server cell | **Quantum Encoder** | AI Expansion Server (MFG + Neural-Quantum Processor + Superposition Oscillator + EPM) |
| **T-WARP** | Ballistic Warp Drive cell | **Quantum Encoder** | Ballistic Warp Drive (TPR + Singularity Cell + Superposition Oscillator + 40 Dark Matter Crystal) |

> Full per-machine rates for every template above (and all sub-components like
> Supercomputer, Cooling System, Dark Matter Crystal, Ficsite Trigon, …) are in
> **VERIFICATION.md**, and live in the **Templates** tab of `factory-network.html`.

---

## How modules map to templates

Every module in `build-guide.md` is "N× of these templates." For example:

**Module M1 — Smart Plating (10/min)** =
`8× T-IRON` + `3× T-PLATE` + `10× T-ROD` + `10× T-SCREW` + `2× T-RIP` +
`3× T-ROTOR` + `5× T-SMARTPLATE`.

**Module M2 — Versatile Framework (20/min)** =
`8× T-IRON` + `11× T-STEEL` + `5× T-PLATE` + `7× T-ROD` + `5× T-SCREW` +
`8× T-BEAM` + `3× T-RIP` + `5× T-FRAME` + `4× T-VERSFRAME`.

**Module M3 — Automated Wiring (5/min)** =
`4× T-COPPER` + `1× T-STEEL` + `8× T-WIRE` + `4× T-CABLE` + `1× T-PIPE` +
`1× T-STATOR` + `2× T-AUTOWIRE`.

The interactive **`factory-network.html`** shows this live: open a module and it
lists its templates; open a template and it shows the spec **and which modules
use it**. Build by repeating templates — never improvise a one-off.

*(Items marked "verify" are pinned to the verification pass results and the
production planner; the table is updated as those land.)*
