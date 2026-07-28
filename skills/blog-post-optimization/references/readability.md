# Long-form readability engineering

Framework-agnostic CSS values for a premium reading experience. These are delivery-layer
decisions — they don't change the words, they change how effortlessly the words land.
Adjust to the brand's type, but keep the ratios.

## Type scale

**Body**
- `font-size: 18–19px` (long-form; 16px is fine for UI, small for reading)
- `line-height: 1.7–1.85`
- paragraph spacing: `28–32px` (bottom margin, not `<br>`)

**H1** — `clamp(32px, 4vw, 48px)`, weight 650–800, `line-height: 1.05–1.1`,
`letter-spacing: -0.02 to -0.03em`, `margin-bottom: 24px`.

**H2** — 28–40px (28 keeps a serif comp calm; go higher for a stronger hierarchy),
`margin: 64–80px 0 16px`, `line-height: 1.2–1.3`.

**H3** — 20–26px, `margin: 44–56px 0 12px`.

**Lists** — item spacing `8–12px`. **Table text** — `16–17px`. **Blockquote** — `20–22px`.
**Captions** — `14–15px` (never 12px — it drops below comfortable secondary-text size).

## Measure (line length)

- Cap prose at **66–75 characters** (`max-width: 68–72ch`), even if the column is wider.
- Let **images, tables, and callouts use the full column** — cap only `p`, `ul`, `ol`.
- Reading column ~700–740px; if a sidebar shares the row, keep the article ≤720px.

## Rhythm and the heading margin-collapse trap

Headings need **more space above than below** (separate from the prior section, bind to
their own text). A common bug:

```css
.body > * { margin: 0 0 30px; }     /* flow rhythm */
.body h2  { margin: 72px 0 0; }      /* BUG: bottom margin now 0 → heading collides
                                        with its paragraph */
```

Fix — give the heading an explicit small bottom, and zero the following element's top:

```css
.body h2 { margin: 72px 0 16px; }
.body h3 { margin: 48px 0 12px; }
.body h2 + *, .body h3 + * { margin-top: 0; }
```

Also set `scroll-margin-top` on headings so anchor jumps clear a sticky header
(drive it from one variable shared with any JS scrollspy offset):

```css
:root { --sticky-offset: 112px; }
.body h2, .body h3 { scroll-margin-top: calc(var(--sticky-offset) + 8px); }
```

## Tables

```css
.body table { display: block; width: 100%; overflow-x: auto;  /* never clip on mobile */
              border-collapse: collapse; font-size: 16px;
              border: 1px solid #e0e0e0; border-radius: 12px; }
.body th, .body td { padding: 14px 18px; }
.body thead tr { background: <accent-soft>; }
.body tbody tr:nth-child(even) { background: <faint-tint>; }   /* zebra */
.body tbody tr:hover { background: <accent-soft>; }
.body td:not(:first-child) { font-variant-numeric: tabular-nums; }  /* aligned figures */
```

## Sidebar navigation (long guides)

- **Sticky TOC** ("On this page") at `top: var(--sticky-offset)`.
- **Scrollspy**: highlight the current section. Prefer a **scroll-position calculation**
  (find the last heading whose `getBoundingClientRect().top <= offset`) over a raw
  `IntersectionObserver` band — the IO approach can miss headings on fast scroll jumps.
- Active link: color + 3px left border + a subtle
  `linear-gradient(90deg, <accent-soft>, transparent)` wash.
- **Mobile**: the sidebar stacks *after* the article, so a bottom-of-page TOC is useless.
  Render a collapsible `<details>` TOC near the top for `<=1040px`, and hide the sidebar
  copy there.

## Reading affordances (subtle, premium only)

- **Reading-progress bar**: fixed 3px top bar, gradient fill = scroll position through
  the **article body element only** (not the whole page).
- **Back-to-top**: appears after ~700px; 48px target; smooth scroll.
- `scroll-behavior: smooth` gated behind `@media (prefers-reduced-motion: no-preference)`.
- Optional hero hover `scale(1.02)` gated behind `@media (hover: hover)` so it never
  sticks on touch.

## Accessibility (WCAG)

- Touch targets **≥44px** (mobile), buttons **48–52px** tall.
- Visible focus: `:focus-visible { outline: 2px solid <accent>; outline-offset: 2px; }`
  on links, buttons, TOC links, and card links.
- Body contrast ≥ 4.5:1; don't drop secondary text below 13px or into low-contrast greys.
- No horizontal body scroll at any width; wide content scrolls inside its own container.

## Verify

Read the rendered page at desktop **and** ≤400px. Confirm: heading space-above,
no table clipping, no horizontal scroll, TOC reachable on mobile, focus rings visible,
one non-prose element per ~400–600px.
