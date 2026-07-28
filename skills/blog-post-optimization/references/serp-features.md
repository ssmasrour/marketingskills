# SERP features & structured data (article layer)

> **Volatility warning.** SERP-feature availability changes often. The statuses below are
> last known as of the dates given (author knowledge cutoff ~Jan 2026). **Verify the
> current state with a web search before asserting it to a user or building for it.**

## What's live and worth targeting

- **Featured snippets** — the highest-value, still-live prize. Win them with:
  - a **quick-answer paragraph** (40–55 words, self-contained, high on the page),
  - a clean **`<ol>`/`<ul>`** for "steps/ways/list" queries,
  - a **`<table>`** for comparison/spec queries.
- **People Also Ask (PAA)** — covered by clear Q-style H2s with concise answers beneath.
- **Passage/section surfacing** — a clean H2 outline with anchor `id`s helps Google jump
  users to the relevant section; also powers on-page TOC.

## What's deprecated — don't build for the rich card

- **FAQ rich results** — restricted (Aug 2023) to authoritative government & health
  sites. FAQ schema no longer yields the accordion rich result for normal sites. FAQ
  *content* still helps users and PAA — just don't promise the rich card.
- **HowTo rich results** — removed (2023). Step/"timeline" content still helps users and
  featured snippets; the HowTo card is gone. *(Re-verify — Google has been known to
  revisit these.)*

## Structured data to ship on a post

Hand implementation depth to the `schema` skill; on the article layer, ensure:

- **`Article`** (or `BlogPosting`) — `headline`, `author` (Person), `datePublished`,
  `dateModified`, `publisher` (Organization), `image`, `mainEntityOfPage`.
- **`BreadcrumbList`** — matches the on-page breadcrumb (Home / Blog / Category / Post).
- **`Organization`** and **`WebSite`** — site-wide; anchors the publisher entity and
  supports sitelinks/knowledge signals.
- Pros/cons structured data — only within editorial *product review* content, where
  eligible.

## Core Web Vitals & page experience (the readability overlap)

Readability fixes double as page-experience signals:

- **CLS** — set image dimensions / aspect-ratios; reserve space for embeds. The
  `overflow-x:auto` table fix also prevents layout breakage.
- **Mobile-friendliness** — ≥44px targets, no horizontal scroll, responsive hero ratio.
- **INP/responsiveness** — keep scroll handlers cheap (passive listeners; a single
  rAF-friendly scroll handler for progress + scrollspy rather than several).
- Engagement (dwell, scroll depth) improves as a downstream effect of all the above.

## Internal linking

- Link from the article into the **product/tool** (configurator, estimator, calculator)
  with descriptive anchor text — funnels readers and distributes authority to money pages.
- Link between related guides (prev/next in-category, "keep reading") for topical depth
  and crawl paths. Keep anchors descriptive, not "click here."
