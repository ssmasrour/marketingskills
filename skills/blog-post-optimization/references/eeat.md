# E-E-A-T: first-hand experience signals

**E-E-A-T = Experience, Expertise, Authoritativeness, Trust.** It comes from Google's
Search Quality Rater Guidelines. Two things people get wrong:

- It is **not a direct ranking signal.** Raters score it; Google's systems *aim to
  approximate* it. You influence it by putting real signals on the page.
- **Trust is the dominant component.** Experience/Expertise/Authoritativeness all feed
  Trust; a page can be expert-sounding and still fail on trust (no author, thin sourcing,
  fabricated claims).

It matters more on **YMYL and money-adjacent topics** (health, finance, and anything
that influences a purchase — e.g. pricing guides).

## The non-negotiable rule

**Every experience/expertise claim must be true.** "In our experience pricing 2,000+
layouts…" is a strong signal *only if the business has done that*. If it hasn't, the
claim is fabrication — an ethics failure and a trust liability. When the real signal
doesn't exist, recommend acquiring it; never invent it.

## Concrete signals to add (in priority order)

1. **A real, named author** with a byline — not "Admin," not anonymous. This is usually
   the single biggest gap on a demo/CMS post (default author = 0 / "admin"). Wire it into:
   - visible byline (name + role),
   - an author bio card with credentials ("Workshop Lead, 12 years on installs"),
   - the `Article` schema `author` (Person with `name`, optionally `jobTitle`).
2. **First-hand specifics over generic claims** — real tolerances, real failure cases,
   real numbers. "Walls bow; if three readings differ by >¼in, plan to the tightest"
   beats "measure carefully."
3. **Real photography**, not stock or placeholders. A placeholder hero is itself a weak
   trust signal on a guide claiming hands-on expertise.
4. **Publish + last-updated dates**, visibly and in schema (`datePublished`,
   `dateModified`). Freshness is a trust cue.
5. **Sourcing** — link claims to primary sources / your own tools where relevant.
6. **Organisation-level trust** — `Organization` and `WebSite` schema, an about page,
   contact info, consistent NAP. Ties the article to a real entity.

## Checklist

- [ ] Post has a real named author (not admin/anonymous)
- [ ] Author has a bio + credentials on the page
- [ ] `Article` schema includes `author` (Person)
- [ ] Experience claims are specific and true
- [ ] Real images, not placeholders/stock for the hero
- [ ] Published + updated dates visible and in schema
- [ ] Key claims are sourced or backed by the product's own data
- [ ] `Organization`/`WebSite` schema present site-wide
