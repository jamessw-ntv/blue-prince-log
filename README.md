# jamessw-ntv.github.io — personal projects hub

A little home for the small things I build: logs, trackers, timelines, and other
experiments. One menu, one consistent look, each project self-contained in its
own folder. Lives at **<https://jamessw-ntv.github.io/>**.

> Nothing here is connected to the `NTV-PROD` repo — this is a separate, personal
> space on purpose.

## Layout

```
index.html        the menu (edit the PROJECTS array to add a card)
assets/hub.css    the shared design system — every page links this
_template/         starter skeleton for a new project
docs/
  DESIGN.md        the design system + conventions
  PORTING.md       how to bring a project in from another chat (one paste)
blue-prince/       Blue Prince room & item log (its own README/CLAUDE.md inside)
CLAUDE.md         instructions for the maintaining chat
```

Each project is one folder (`<slug>/`) with its own `index.html`, optional
`data.json` and `images/`, and may carry its own `CLAUDE.md`/`README.md`.

## Adding a project

The easy path is in **[`docs/PORTING.md`](./docs/PORTING.md)**: paste an export
prompt into the chat that already has the project, then paste the result here and
say "port this in." Or by hand: copy `_template/` to `<slug>/`, build it against
[`docs/DESIGN.md`](./docs/DESIGN.md), and add a card to `index.html`.

## How it's served

The repo is named `jamessw-ntv.github.io`, so GitHub Pages publishes it at the
root automatically. A push to `main` deploys via
[`.github/workflows/pages.yml`](.github/workflows/pages.yml). Links are all
relative, so projects work at any path.
