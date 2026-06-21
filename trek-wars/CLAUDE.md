# Trek & Wars — project rules

An interactive **star map + timeline** of the full publishing history of Star
Trek and Star Wars comics and novels (1967–present). The viewer
(`trek-wars/index.html`) renders `trek-wars/data.json` at
<https://jamessw-ntv.github.io/trek-wars/>.

## Intent routing

1. **Content** (new series, issue counts, a run ended/announced): → edit
   `trek-wars/data.json`, commit to `main`. Bump `meta.updated`.
2. **Viewer change** (new view, colours, layout): → edit
   `trek-wars/index.html`; appears after the ~30–60s Pages rebuild.
3. **Question** → just answer; don't commit.

## Data — `data.json`

`entries[]`, one object per series/run. Adding a series = adding one entry:

```
id        unique kebab-case (used for dedup + Y jitter)
name, sub display name + node sub-label
type      'comic' | 'book'
franchise 'trek' | 'wars'
canon     true = current canon · false = Legends / pre-Disney / non-canon
rel       [startYear, endYear] decimals — X in release mode, bar width on timeline
eraYear   in-universe year — X in era mode
            Trek = stardate year (2266 TOS, 2378 post-VOY, 2402 post-PIC)
            Wars = years vs ANH — negative = BBY, positive = ABY
publisher plain text · pubColor reserved for a future publisher-colour mode
issues    total count (null = ongoing/unknown) · out = released so far
status    'complete' | 'ongoing' | 'upcoming'
avail[]   where to read — { l: label, c: class, u: url }
            class → colour: mu (Marvel Unlimited), gc (GlobalComix),
            amz (Amazon/Comixology), lcs (print/LCS), kindle
desc      short HTML blurb (<strong>/<em> ok), 2–4 sentences
```

## Visual encoding (don't break it)

- Node **size** = scale (issue/book count). **Colour** = pink comics / green books.
- **Legends/non-canon** = purple ring; **canon** = type-coloured ring.
- **Opacity** = status (upcoming faded, ongoing full, complete dimmed).
- **X** = release date (default) or in-universe era; **Y** = franchise band
  (Trek top / Wars bottom) with comics above centre, books below.

## Golden rules

1. Use the hub design system: links `../assets/hub.css`, standard `.hubbar`
   back-link, **relative links only**. Don't redefine hub's `:root` tokens.
2. Self-contained: data over content (`data.json`), no build step, no
   dependencies (system fonts only — no Google Fonts).
3. Only change counts/status you're certain about; no speculative placeholders.
   This list is allowed to go stale.
4. Keep `data.json` valid JSON, commit to `main`, push. Don't open a PR.
