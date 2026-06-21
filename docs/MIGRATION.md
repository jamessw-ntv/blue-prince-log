# Migration runbook — turn this into your personal hub

This is the **one document** that gets you from where you are now to the finished
state: a personal projects hub served at the root of your GitHub Pages, with the
Blue Prince log living inside it, everything on one design system, and the repo
renamed. Follow it top to bottom. Two of the steps only you can do; the rest is
already built and committed.

---

## End state you're aiming for

| | URL |
|---|---|
| The hub menu | `https://jamessw-ntv.github.io/` |
| Blue Prince log | `https://jamessw-ntv.github.io/blue-prince/` |
| Future projects | `https://jamessw-ntv.github.io/<slug>/` |

One public repo named **`jamessw-ntv.github.io`**, each project in its own folder,
all sharing `assets/hub.css`. Completely separate from `NTV-PROD`.

---

## What's already done (committed to `main`)

```
index.html          the menu — a PROJECTS array rendered as cards
assets/hub.css      the shared design system (tokens + components)
_template/          starter skeleton for a new project
docs/
  DESIGN.md         design philosophy + system rules
  PORTING.md        how to bring a project in from another chat (one paste)
  MIGRATION.md      this document
blue-prince/        the Blue Prince log, fully self-contained
  index.html        viewer, with a "← Hub" back-link, NTV link removed
  data.json         the log data (source/viewer URLs repointed)
  images/           example.svg + any photos you log
  README.md         schema reference
  CLAUDE.md         spoiler-free logging rules
  LOGGING.md        how to log from a normal Claude.ai chat
CLAUDE.md           hub-wide instructions for the maintaining chat
README.md           repo overview
.github/workflows/pages.yml   deploys the whole repo root to Pages
```

Everything uses **relative links only**, so it works identically before and
after the rename — there is no broken in-between state.

---

## Step 1 — rename the repository (only you can do this)

1. Go to **https://github.com/jamessw-ntv/blue-prince-log** → **Settings**.
2. Under **General**, change the repository name to exactly:

   ```
   jamessw-ntv.github.io
   ```
3. Click **Rename**.

Because that's the special "user site" name, GitHub Pages automatically publishes
it at the **root** (`https://jamessw-ntv.github.io/`). GitHub also auto-redirects
the old `github.com/.../blue-prince-log` URLs to the new name.

> One caveat to know: the old **Pages** URL
> `https://jamessw-ntv.github.io/blue-prince-log/` will 404 after the rename
> (GitHub redirects everything *except* project-site Pages URLs). That's expected
> — the content now lives at the root and at `/blue-prince/`. Nothing important
> linked to the old path.

## Step 2 — let the deploy run

The rename triggers a Pages build (or push anything / use **Actions → Deploy
viewer to GitHub Pages → Run workflow**). Give it ~1 minute.

## Step 3 — verify

- `https://jamessw-ntv.github.io/` → the menu, with a **Blue Prince** card.
- Click it → `https://jamessw-ntv.github.io/blue-prince/`, the log loads, and the
  **← Hub** link returns you to the menu.

That's the whole migration. Everything below is reference for living with it.

---

## Living with the hub

### Adding a new project (the one-paste way)

Full detail is in [`PORTING.md`](./PORTING.md). In short:

1. In the *old* Claude chat that has the project, paste the **export prompt** from
   `PORTING.md`. It emits a single Markdown handoff file.
2. Paste that file into a chat with write access to this repo and say
   **"port this into the hub."**
3. A new `/<slug>/` folder appears, restyled to the design system, and a card is
   added to the menu. Done.

### Adding a project by hand

1. `cp -r _template my-project` (use a kebab-case slug).
2. Build inside it, following [`DESIGN.md`](./DESIGN.md): link `../assets/hub.css`,
   use the tokens, keep the `.hubbar` back-link, relative links only.
3. Add a card to the `PROJECTS` array in the root `index.html`:
   ```js
   { ico:"🎯", title:"My project", href:"my-project/", status:"active",
     desc:"One line about it." },
   ```

### Logging Blue Prince from a normal chat

See [`blue-prince/LOGGING.md`](../blue-prince/LOGGING.md). After the rename, point
the GitHub connector at **`jamessw-ntv/jamessw-ntv.github.io`** and edit
`blue-prince/data.json`. (Your existing authorization should carry over the rename
automatically, since the repo's identity doesn't change.)

### Design philosophy (the short version)

Plain static HTML/CSS/JS, no build step, no dependencies. Each project is one
self-contained folder. Data lives in `data.json`, separate from presentation.
Relative links always. Dark, calm, content-first. Full version in
[`DESIGN.md`](./DESIGN.md).

---

## Rules of the house

- **`NTV-PROD` is off-limits** — never linked, merged, or referenced here.
- Commit project content and menu changes straight to `main`; don't open PRs
  unless asked. A push to `main` redeploys the site.
- Keep files valid; the site has no build to catch errors for you.
