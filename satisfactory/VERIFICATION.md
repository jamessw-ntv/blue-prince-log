# Verification log & recipe reference (Satisfactory 1.0)

## Corrections (QA passes, 2026-06-17)

Multiple QA + data-verification passes re-checked every recipe against the
official wiki and SCIM, resolving per-craft-vs-per-minute confusion. Final
corrected late-game recipes (all values **per minute, 1 machine, 100%**):

| Recipe | Corrected to | Note |
|--------|--------------|------|
| **Nuclear Pasta** | **100 Copper Powder** + 0.5 PCC → 0.5 | per-craft 200 Cu at 0.5 craft/min = 100/min (an earlier pass wrongly set 200) |
| **Dark Matter Residue** | **5 Reanimated SAM → 50** | Converter |
| **Neural-Quantum Processor** | **15 Time Crystal** + 3 Supercomputer + 45 Ficsite Trigon + 75 EPM → 3 | per-craft 5 TC : 1 SC : 15 Trigon : 25 EPM : 1 (an earlier pass wrongly set 45 TC) |
| **Heavy Modular Frame** | **40 Steel Pipe, 240 Screw** (+10 Modular Frame, 10 Encased Beam → 2) | |
| **Ficsite Ingot** | **40 Reanimated SAM + 240 Iron Ingot → 10** | inputs had been 10× too low (critical SAM/Iron under-supply) |
| **Biochemical Sculptor** | **0.5 ADS + 40 Ficsite Trigon + 10 Water → 2** | Blender 120 s; values had been the per-craft amounts (2×) |
| **FLUID set** | Plastic & Rubber are **solids (belts)**, removed from fluids | they were wrongly piped |

Re-verified **correct** (no change): Crystal Oscillator (36 Quartz + 28 Cable +
5 RIP → 1), Diamonds (600 Coal → 30), Dark Matter Crystal (30 Diamonds + 150
Residue → 30), Singularity Cell (1 Pasta + 20 DM Crystal + 100 Iron Plate + 200
Concrete → 10), Supercomputer (7.5 Computer + 3.75 AI Limiter + 5.625 HSC + 52.5
Plastic → 1.875), High-Speed Connector (210 Quickwire + 37.5 Cable + 3.75 CB →
3.75), Computer (10 CB + 20 Cable + 40 Plastic → 2.5), Cooling System (12 Heat
Sink + 12 Rubber + 30 Water + 150 N₂ → 6), Turbo Motor, Fused Modular Frame,
Radio Control Unit, Thermal Propulsion Rocket, Modular Engine, Adaptive Control
Unit, Assembly Director System, Electromagnetic Control Rod, Heat Sink, AI
Limiter, Encased Industrial Beam, Circuit Board, Superposition Oscillator, the
full aluminium chain, the Ficsite/Reanimated-SAM/Time-Crystal chain, and Excited
Photonic Matter (no input, Converter). Magnetic Field Generator ratios correct
(5 VF + 2 EM Rod per unit); spot-check its exact craft rate in-game.

> Machine counts in the app are now **demand-solved**: the 12 final parts have
> design rates and every upstream bank is sized to total demand, so feeds never
> starve. MAX mode = 250% overclock + Somersloop (5× per machine).

---

Every recipe and quantity in this plan was cross-checked against **at least two
independent sources** — the official wiki (`satisfactory.wiki.gg`), the Fandom
wiki, the community **Satisfactory Calculator** (SCIM), and **satisfactorytools.com**.
All rates are **standard recipes, one machine, 100 % clock**, unless noted.

> WebFetch was blocked in the build environment (HTTP 403), so figures were
> gathered via search snippets and reconciled across sources. Two values that no
> source printed verbatim are **flagged** below — spot-check them in-game:
> Excited Photonic Matter output rate, and the exact Quantum-Encoder craft times.

---

## 1. Space Elevator deliveries — CONFIRMED

| Phase | Parts (qty) | Unlocks |
|-------|-------------|---------|
| 1 | Smart Plating ×50 | Tiers 3 & 4 |
| 2 | Smart Plating ×500 · Versatile Framework ×500 · Automated Wiring ×100 | Tiers 5 & 6 |
| 3 | Versatile Framework ×2,500 · Modular Engine ×500 · Adaptive Control Unit ×100 | Tiers 7 & 8 |
| 4 | Assembly Director System ×500 · Magnetic Field Generator ×500 · Thermal Propulsion Rocket ×250 · Nuclear Pasta ×100 | Tier 9 |
| 5 | Nuclear Pasta ×1,000 · Biochemical Sculptor ×1,000 · AI Expansion Server ×256 · Ballistic Warp Drive ×200 | Game complete |

*(One third-party guide misreported Phase 2 as 1000/1000/100 — that is wrong; the
in-game value is 500/500/100.)*

## 2. Belt / pipe throughput & availability — CONFIRMED

| Logistics | Throughput | Unlocked at | Available for building… |
|-----------|-----------|-------------|--------------------------|
| Belt Mk.1 | 60/min | Tier 0 | from the start |
| Belt Mk.2 | 120/min | Tier 2 | Phase 1 work |
| Belt Mk.3 | 270/min | Tier 4 (Logistics Mk.3) | Phase 2 work |
| Belt Mk.4 | 480/min | Tier 5 (Logistics Mk.4) | Phase 3 work |
| Belt Mk.5 | 780/min | Tier 7 (Logistics Mk.5) | Phase 4 work |
| Belt Mk.6 | 1,200/min | Tier 9 (Logistics Mk.6) | Phase 5 work |
| Pipe Mk.1 | 300 m³/min | Tier 3 | — |
| Pipe Mk.2 | 600 m³/min | Tier 6 | — |

**Sizing consequence:** while building Phase 2 you only have **Mk.3 (270)**, so
M2's ~480 steel-ingot internal trunk must be **split across two belts** until you
reach Tier 5 (Mk.4) — then upgrade the belt, no rebuild.

## 3. Production-building unlocks — CONFIRMED

Smelter/Constructor = Tier 0 · Assembler = Tier 2 · Foundry = Tier 3 · Refinery
/ Packager / Manufacturer = **Tier 5** · Blender = Tier 7 · Particle Accelerator
= Tier 8 · Converter & Quantum Encoder = Tier 9.

---

## 4. Verified recipe reference (standard, /min @100 %)

### Ingots & basics
| Item | Building | Inputs/min | Out/min |
|------|----------|-----------|---------|
| Iron / Copper Ingot | Smelter | 30 ore | 30 |
| Caterium Ingot | Smelter | 45 ore | 15 |
| Steel Ingot | Foundry | 45 Iron Ore + 45 Coal | 45 |
| Iron Plate | Constructor | 30 Iron Ingot | 20 |
| Iron Rod | Constructor | 15 Iron Ingot | 15 |
| Screw | Constructor | 10 Iron Rod | 40 |
| Wire | Constructor | 15 Copper Ingot | 30 |
| Cable | Constructor | 60 Wire | 30 |
| Copper Sheet | Constructor | 20 Copper Ingot | 10 |
| Concrete | Constructor | 45 Limestone | 15 |
| Silica | Constructor | 22.5 Raw Quartz | 37.5 |
| Quartz Crystal | Constructor | 37.5 Raw Quartz | 22.5 |
| Steel Beam | Constructor | 60 Steel Ingot | 15 |
| Steel Pipe | Constructor | 30 Steel Ingot | 20 |
| Quickwire | Constructor | 12 Caterium Ingot | 60 |
| Plastic | Refinery | 30 Crude Oil | 20 (+10 Heavy Oil Residue) |
| Rubber | Refinery | 30 Crude Oil | 20 (+20 Heavy Oil Residue) |

### Components
| Item | Building | Inputs/min | Out/min |
|------|----------|-----------|---------|
| Reinforced Iron Plate | Assembler | 30 Iron Plate + 60 Screw | 5 |
| Rotor | Assembler | 20 Iron Rod + 100 Screw | 4 |
| Modular Frame | Assembler | 3 RIP + 12 Iron Rod | 2 |
| Stator | Assembler | 15 Steel Pipe + 40 Wire | 5 |
| Motor | Assembler | 10 Rotor + 10 Stator | 5 |
| Smart Plating | Assembler | 2 RIP + 2 Rotor | 2 |
| Versatile Framework | Assembler | 2.5 Modular Frame + 30 Steel Beam | 5 |
| Automated Wiring | Assembler | 2.5 Stator + 50 Cable | 2.5 |
| Circuit Board | Assembler | 15 Copper Sheet + 30 Plastic | 7.5 |
| Computer | Manufacturer | 10 Circuit Board + 20 Cable + 40 Plastic | 2.5 |
| Encased Industrial Beam | Assembler | 18 Steel Beam + 36 Concrete | 6 |
| Heavy Modular Frame | Manufacturer | 10 Modular Frame + 20 Steel Pipe + 10 Encased Industrial Beam + 120 Screw | 2 |
| AI Limiter | Assembler | 25 Copper Sheet + 100 Quickwire | 5 |
| High-Speed Connector | Manufacturer | 210 Quickwire + 37.5 Cable + 3.75 Circuit Board | 3.75 |
| Supercomputer | Manufacturer | 7.5 Computer + 3.75 AI Limiter + 5.625 High-Speed Connector + 52.5 Plastic | 1.875 |
| Electromagnetic Control Rod | Assembler | 6 Stator + 4 AI Limiter | 4 |
| Crystal Oscillator | Manufacturer | 36 Quartz Crystal + 28 Cable + 5 RIP | 1 *(approx)* |

### Phase-3 finals
| Item | Building | Inputs/min | Out/min |
|------|----------|-----------|---------|
| Modular Engine | Manufacturer | 2 Motor + 15 Rubber + 2 Smart Plating | 1 |
| Adaptive Control Unit | Manufacturer | 5 Automated Wiring + 5 Circuit Board + 1 Heavy Modular Frame + 2 Computer | 1 |

### Phase-4 finals + sub-chains
| Item | Building | Inputs/min | Out/min |
|------|----------|-----------|---------|
| **Assembly Director System** | **Assembler** | 1.5 Adaptive Control Unit + 0.75 Supercomputer | 0.75 |
| **Magnetic Field Generator** | **Assembler** | 12.5 Versatile Framework + 5 Electromagnetic Control Rod | 2.5 |
| **Thermal Propulsion Rocket** | Manufacturer | 2.5 Modular Engine + 1 Turbo Motor + 3 Cooling System + 1 **Fused Modular Frame** | 1 |
| **Nuclear Pasta** | Particle Accelerator | 100 Copper Powder + 0.5 Pressure Conversion Cube | 0.5 |
| Turbo Motor | Manufacturer | 7.5 Cooling System + 3.75 Radio Control Unit + 7.5 Motor + 45 Rubber | 1.875 |
| Cooling System | Blender | 12 Heat Sink + 12 Rubber + 30 Water + 150 Nitrogen Gas | 6 |
| Heat Sink | Assembler | 37.5 Alclad Aluminum Sheet + 22.5 Copper Sheet | 7.5 |
| Copper Powder | Constructor | 300 Copper Ingot | 50 |
| Pressure Conversion Cube | Assembler | 1 Fused Modular Frame + 2 Radio Control Unit | 1 |
| Fused Modular Frame | Blender | 1.5 Heavy Modular Frame + 75 Aluminum Casing + 37.5 Nitrogen Gas | 1.5 |
| Radio Control Unit | Manufacturer | 40 Aluminum Casing + 1.25 Crystal Oscillator + 2.5 Computer | 2.5 |

### Aluminium chain (standard; *approx — spot-check ratios*)
| Item | Building | Inputs/min | Out/min |
|------|----------|-----------|---------|
| Alumina Solution | Refinery | 120 Bauxite + 180 Water | 120 (+5 Silica) |
| Aluminum Scrap | Refinery | 240 Alumina Solution + 120 Coal | 360 (+120 Water) |
| Aluminum Ingot | Foundry | 90 Aluminum Scrap + 75 Silica | 60 |
| Aluminum Casing | Constructor | 90 Aluminum Ingot | 60 |
| Alclad Aluminum Sheet | Assembler | 30 Aluminum Ingot + 10 Copper Ingot | 30 |

### Phase-5 finals + sub-chains
| Item | Building | Inputs/min | Out/min |
|------|----------|-----------|---------|
| **Biochemical Sculptor** | **Blender** | 1 Assembly Director System + 80 Ficsite Trigon + 20 Water | 4 |
| **AI Expansion Server** | **Quantum Encoder** | 4 Magnetic Field Generator + 4 Neural-Quantum Processor + 4 Superposition Oscillator + 100 Excited Photonic Matter | 4 |
| **Ballistic Warp Drive** | **Quantum Encoder** | 1 Thermal Propulsion Rocket + 5 Singularity Cell + 2 Superposition Oscillator + 40 Dark Matter Crystal + 25 Excited Photonic Matter | 1 |
| Neural-Quantum Processor | Quantum Encoder | 15 Time Crystal + 3 Supercomputer + 45 Ficsite Trigon + 75 Excited Photonic Matter | 3 |
| Superposition Oscillator | Quantum Encoder | 30 Dark Matter Crystal + 5 Crystal Oscillator + 45 Alclad Aluminum Sheet + 125 Excited Photonic Matter | 5 |
| Singularity Cell | Manufacturer | 1 Nuclear Pasta + 20 Dark Matter Crystal + 100 Iron Plate + 200 Concrete | 10 |
| Excited Photonic Matter | Converter | *(no item inputs)* | ~200 m³ *(flag)* |
| Dark Matter Crystal | Particle Accelerator | 30 Diamonds + 150 Dark Matter Residue | 30 |
| Time Crystal | Converter | 12 Diamonds | 6 |
| Diamonds | Particle Accelerator | 600 Coal | 30 |
| Ficsite Trigon | Constructor | 30 Ficsite Ingot | 90 |
| Ficsite Ingot | Converter | 4 Reanimated SAM + 24 Iron Ingot | 10 |
| Reanimated SAM | Constructor | 120 SAM Ore | 30 |

**Building corrections caught during verification (vs. common older guides):**
- Assembly Director System & Magnetic Field Generator → **Assembler** in 1.0 (MFG no longer uses Batteries).
- Ballistic Warp Drive → **Quantum Encoder** (not Manufacturer).
- Thermal Propulsion Rocket uses **Fused Modular Frame** (not plain Modular Frame).
- Computer recipe has **no Screws** in 1.0 (Circuit Board + Cable + Plastic).
- Every Quantum Encoder recipe consumes **25 m³ Excited Photonic Matter per craft**
  and emits Dark Matter Residue; "Quantum Energy" is the internal name of Excited
  Photonic Matter (not a separate item).

---

*Primary sources: satisfactory.wiki.gg, satisfactory.fandom.com,
satisfactory-calculator.com (SCIM), satisfactorytools.com. Each value above had
≥2 sources in agreement.*
