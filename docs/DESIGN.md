# Design system

Every page on this site should feel like part of one product. That consistency
comes from a few simple, enforced rules — not a framework.

## The one rule that matters

**Link `assets/hub.css` and use its tokens. Never hard-code colours or redefine
the `:root` variables.** Project-specific CSS is welcome on top, but it should
reference the tokens below.

## Tokens (defined in `assets/hub.css`)

| Token | Value | Use |
|---|---|---|
| `--bg` | `#0f1422` | page background |
| `--panel` | `#171d2e` | cards, inputs, pills |
| `--panel2` | `#1f2740` | nested / header surfaces |
| `--line` | `#2b3550` | borders, dividers |
| `--text` | `#e8ecf6` | primary text |
| `--muted` | `#9aa6c4` | secondary text |
| `--accent` | `#6ea8fe` | links, active state |
| `--blue/--orange/--green/--purple/--yellow/--red/--black` | — | category swatches |
| `--maxw` | `1100px` | content width |
| `--radius` | `12px` | card/border radius |

Dark theme, system font stack, generous radii, pill-shaped controls.

## Conventions

- **Layout:** wrap page content in `<div class="wrap">` (centres at `--maxw`).
- **Back-link:** every project page starts with the standard `.hubbar`:
  ```html
  <div class="hubbar">
    <a class="backlink" href="../">← Hub</a>
    <span class="crumb"><b>Project name</b></span>
  </div>
  ```
- **Relative links only.** Use `../` for the hub and `../assets/hub.css` for the
  stylesheet — never a leading `/`. This is what lets the site work both before
  and after the repo is renamed to `jamessw-ntv.github.io`.
- **Components available from `hub.css`:** `.grid` + `.card`, `.badges`/`.b`,
  `.status` (`.active`/`.wip`/`.planned`), `.toggle`, `footer.site`.
- **No build step, no dependencies.** Plain HTML/CSS/JS that runs from a static
  file. Data-driven projects keep a `data.json` beside their `index.html` and
  render it client-side (see `blue-prince/` for the reference implementation).

## Starting a new project

Copy `_template/index.html` into a new folder named after the project's slug
(kebab-case), then build inside it. Add a card to the `PROJECTS` array in the
root `index.html` so it shows up on the menu.
