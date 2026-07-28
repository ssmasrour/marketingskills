# Rich content blocks

A wall of paragraphs (para → para → para → table → para) underperforms because it gives
the reader no visual handholds and gives Google no structured passage to feature. Fix it
by inserting **intent-driven** non-prose blocks — never blocks for their own sake.

## Why it works (state the mechanism correctly)

Variety is **not** a direct ranking signal. It helps through two real mechanisms:

1. **Engagement** — scannable structure raises scroll depth and dwell, lowers
   pogo-sticking. These are quality signals Google's systems approximate.
2. **SERP features** — specific structures are eligible for featured snippets, People
   Also Ask, and (a shrinking set of) rich results.

## The catalog

Pick by query intent. The right-hand column is the *live* payoff — see
`serp-features.md` for what has been deprecated.

| Block | Reader / SEO purpose | SERP payoff |
|---|---|---|
| **Quick Summary / TL;DR** | Answers the query in 40–55 words at the top | Strong **featured-snippet** target |
| **Cost / spec Breakdown** | Itemized numbers scan better than prose | **Table** featured snippet |
| **Checklist** | Actionable, skimmable, savable | **List** snippet |
| **Pros & Cons** | Balanced decision aid | Editorial pros/cons structured data |
| **Comparison Cards / Decision Matrix** | Side-by-side reduces choice friction | **Table** snippet |
| **Common Mistakes** | High-value, experience-flavoured | Engagement + PAA coverage |
| **Expert Tip callout** | Injects first-hand experience mid-read | E-E-A-T + engagement |
| **Myth vs Reality** | Handles objections | PAA / engagement |
| **Visual Timeline / Steps** | Breaks a long flat stretch | Engagement (see HowTo note) |
| **Key Takeaways recap** | Closes the loop for scanners | Featured snippet + retention |

## The cadence rule

Aim for **one non-prose element every ~400–600px of scroll**. This is a rhythm target,
not a quota — if a stretch is genuinely all prose and the intent doesn't call for a
block, leave it. Fatigue comes from *unbroken* text, not from having "too few boxes."

## Anti-patterns

- **Block-stuffing** — adding a decision matrix to a post nobody is comparing options on.
  It reads as padding and dilutes the page.
- **Duplicating the quick answer in three formats** — pick the one that matches intent.
- **Fake data in a table** to look authoritative. Real numbers only.

## Implementation notes (framework-agnostic)

- Build blocks as **semantic HTML** (`<table>`, `<ul>`, `<ol>`, `<blockquote>`,
  `<figure>`), then style — don't fake a list with `<div>`s. Semantics feed both
  screen readers and snippet extraction.
- A **quick-answer** block should be a single clean paragraph or a tight list
  immediately under the H1/first H2 — snippet extractors favour an early, self-contained
  answer.
- A reusable **tip/callout** class (e.g. `.tip` with a small uppercase label) lets
  authors drop experience blocks in without bespoke markup each time.
- Keep tables responsive (`overflow-x:auto`) so a wide comparison never breaks mobile.
