# Porting a project in from another chat

You build a lot of small things in normal Claude chats. This is how you move one
into the hub with a single copy-paste, so it comes out clean and on-brand.

The flow has two halves:

1. **Export** — paste the prompt below into the *old* chat that holds the project.
   It produces **one self-contained Markdown file** (a "handoff").
2. **Ingest** — paste that handoff into a hub chat (one with write access to this
   repo) and say *"port this in."* A new `/<slug>/` folder appears and a card
   shows up on the menu.

---

## Step 1 — paste this into the source chat

> You're helping me hand this project off to my personal projects hub. Produce
> **one Markdown document** I can copy in full — no preamble, no follow-up
> questions — using exactly these sections and headings:
>
> ```
> # <Project name>
> - slug: <kebab-case-folder-name>
> - one-liner: <one sentence on what it is>
> - status: active | wip | planned
> - icon: <a single emoji>
>
> ## Purpose & design philosophy
> What it's for, who it's for, and the handful of principles behind how it
> looks and behaves.
>
> ## Data model
> If it's data-driven, the schema/shape (fields + types + meaning). If not,
> write "none".
>
> ## Current code
> The COMPLETE current code, each file in its own fenced block, with the
> intended file path as the block's first comment line. Don't summarise or
> elide — paste it all.
>
> ## State & history
> What works today, what's half-done, and any important decisions/context I'd
> lose otherwise.
>
> ## Open tasks / roadmap
> Bullet list of what's next.
>
> ## Assets
> List any images/fonts/data files and where to get them (or paste small text
> assets inline).
> ```
>
> Keep it self-contained: someone with only this document should be able to
> rebuild the project from scratch. Output the document and nothing else.

## Step 2 — paste the handoff into a hub chat

Say: **"Port this into the hub."** The hub chat will:

1. Read the `slug`, create `/<slug>/` from `_template/index.html`.
2. Rebuild the code there, **conforming to the design system** in
   [`DESIGN.md`](./DESIGN.md): link `../assets/hub.css`, use the tokens, add the
   standard `.hubbar` back-link, keep all links relative.
3. Bring data into `<slug>/data.json` and assets into `<slug>/...` as needed.
4. Add a card to the `PROJECTS` array in the root `index.html` (icon, title,
   `href:"<slug>/"`, status, one-liner).
5. Commit, and tell you the URL (`https://jamessw-ntv.github.io/<slug>/`).

That's it — export once, paste once, it's live.

---

### Notes
- A project doesn't *have* to match the source's original look — the point of
  porting is that it adopts the hub's design system. Functionality and data are
  preserved; styling is re-skinned to match.
- Anything to do with NTV-PROD stays out of this repo entirely.
