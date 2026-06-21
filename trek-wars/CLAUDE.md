# Trek & Wars — project rules

A **visual publication timeline** of the full history of Star Trek and Star Wars
comics and novels (1967–present). The viewer (`trek-wars/index.html`) renders
`trek-wars/data.json` at <https://jamessw-ntv.github.io/trek-wars/>: four
swimlanes (Trek/Wars × Comics/Novels), one horizontal bar per series spanning
its publication years, tap a row for the detail panel. Works on mobile and
desktop from the same markup.

## Intent routing

1. **Content** (new series, issue counts, a run ended/announced): → edit
   `trek-wars/data.json`, commit to `main`. Bump `meta.updated`.
2. **Viewer change** (layout, colours, sections): → edit
   `trek-wars/index.html`; appears after the ~30–60s Pages rebuild.
3. **Question** → just answer; don't commit.

## Data — `data.json`

`entries[]`, one object per series/run. Adding a series = adding one entry:

```
id        unique kebab-case (detail lookup)
name, sub display name + sub-label
type      'comic' | 'book'      → bar colour (pink / green) + swimlane
franchise 'trek' | 'wars'       → swimlane
canon     true = current canon · false = Legends / pre-Disney / non-canon (dimmed bar)
rel       [startYear, endYear] decimals — bar position + width on the 1967→present axis
publisher plain text  ·  pubColor / eraYear are kept but not used by the timeline
issues    total count (null = ongoing/unknown) · out = released so far
status    'complete' | 'ongoing' | 'upcoming'  → tag + bar style (upcoming = dashed)
avail[]   where to read — { l: label, c: class, u: url }
            class → colour: mu (Marvel Unlimited), gc (GlobalComix),
            amz (Amazon/Comixology), lcs (print/LCS), kindle
desc      short HTML blurb (<strong>/<em> ok), 2–4 sentences
```

## Golden rules

1. Use the hub design system: links `../assets/hub.css`, standard `.hubbar`
   back-link, **relative links only**. Don't redefine hub's `:root` tokens.
2. Self-contained: data over content (`data.json`), no build step, no
   dependencies (system fonts only).
3. Only change counts/status you're certain about; no speculative placeholders.
   This list is allowed to go stale.
4. Keep `data.json` valid JSON, commit to `main`, push. Don't open a PR.
