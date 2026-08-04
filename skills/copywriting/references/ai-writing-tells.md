# Avoiding AI-Writing Tells in Marketing Copy

Detailed reference for the "Avoid AI-Writing Tells" section of SKILL.md.

Derived from Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WP:AISIGNS), which catalogues the patterns Wikipedia editors use to spot LLM text, with the underlying linguistics research it cites. Translated here into copywriting terms.

## Why marketing copy is the hard case

Two findings from that article matter more for copywriting than for any other genre:

**1. LLMs drift toward advertising language by default.** The article documents that LLM output "will often tend toward advertisement-like writing, or like the prose of a travel guide" *even when explicitly prompted to write neutrally* — to the point that edit summaries claiming to have "removed promotional tone" actually introduced it. Every other genre gets a free warning signal when copy starts sounding salesy. Marketing copy doesn't. The tells arrive camouflaged as the thing you were trying to write.

**2. The core failure is being vaguer and louder at the same time.** LLMs regress toward the statistically average phrasing, so specific facts get smoothed into generic praise. The article's example: the highly specific "inventor of the first train-coupling device" becomes "a revolutionary titan of industry." The subject ends up *simultaneously less specific and more exaggerated*.

That is also the definition of bad marketing copy. So this is not a separate checklist bolted onto the skill — it is the skill's own "Specificity Over Vagueness" principle, arriving from a different direction. Copy that survives the specificity test usually survives the AI-tell test automatically.

**Corollary:** newer models are subtler. The article notes older models (GPT-4 era) produced blatant superlatives, while newer ones "are more subtly positive and tend to avoid obviously superlative statements like 'the best.'" Don't just scan for hype words; scan for the *shape* of hollow praise.

## Strong tells vs. weak tells

Not every item is equally damning. Weight the revision effort accordingly.

| Weight | Tells |
|---|---|
| **Strong** — fix on sight | Negative parallelism; dense AI vocabulary; superficial "-ing" analysis; puffery about significance; vague attribution; elegant variation |
| **Moderate** — fix when it clusters | Copula avoidance; rule-of-three runs; inline-header bold lists; formulaic conclusions; mechanical boldface |
| **Weak** — only meaningful alongside others | Em dashes; curly quotes; title-case headings |

The article is explicit that weak signals prove nothing alone: em dashes are "most useful when taken in combination with other indicators, not by itself," and curly quotes have entirely innocent sources (Chicago style, Word's smart quotes, macOS defaults). Don't mangle good copy chasing these.

---

## 1. Substance tells

### 1.1 Puffery about significance and broader trends

The most consistently identifiable AI content move: announcing that something matters instead of showing what it does.

Watch for: *stands/serves as · is a testament/reminder · a crucial/pivotal/vital/significant/key role · underscores/highlights its importance · reflects broader · symbolizing its ongoing/enduring/lasting · setting the stage for · marking/shaping the · represents a shift · key turning point · evolving landscape · focal point · indelible mark · deeply rooted*

> ❌ In today's evolving hospitality landscape, reliable supply plays a pivotal role in a restaurant's success.
> ✅ Run out of dish soap on a Thursday night and you're washing by hand through the dinner rush.

The fix is always the same: replace the claim of importance with the concrete consequence.

### 1.2 Superficial analysis tacked on with "-ing"

The article's signature structural finding: a present-participle phrase glued to the end of a sentence, adding commentary that carries no information.

Watch for trailing: *highlighting… · underscoring… · emphasizing… · ensuring… · reflecting… · symbolizing… · contributing to… · fostering… · enhancing… · encompassing…*

> ❌ We deliver within 24 hours in Tehran, ensuring a seamless experience and fostering long-term customer relationships.
> ✅ We deliver within 24 hours in Tehran. Order by 9am and it ships the same day.

Test: delete everything after the comma. If nothing was lost, it was ornament. Note this pattern also loves to combine with §1.3 — "…, further cementing its reputation among industry observers."

### 1.3 Vague attribution and inflated consensus

Watch for: *Studies show · Experts agree · Industry reports suggest · Observers have cited · Some critics argue · several publications · many customers find*

Two distinct failures, per the article:
- **Unnamed authority.** Cite a real, named, checkable source or drop the claim entirely.
- **Inflated quantity.** Presenting one or two sources as a widespread view — "publications such as X and Y" when X and Y are the only two that exist. Also flagged: *such as* placed before what is actually an exhaustive list, implying more examples exist.

For marketing copy this is also a legal exposure, not just a style problem — see the skill's "Honest over sensational" principle.

### 1.4 Formulaic conclusions

Two shapes to avoid:
- **The wrap-up:** "In summary," / "In conclusion," / "Ultimately," / "All in all,"
- **The challenges arc:** "Despite its strengths, [product] faces challenges…" resolving into vague optimism about the future.

The article stresses this tell "is about the rigid formula, not simply the mention of challenges." Honestly discussing a product's limits is good copy and builds trust. Reciting a balance-then-reassure template is not.

End on the CTA or on a concrete specific. Never on a summary of what the reader just read.

---

## 2. Sentence-shape tells

### 2.1 Negative parallelism — the single most recognizable cadence

Three subtypes. The first two are widely known; the third is frequently missed.

**a) Not just X, but also Y**
> "It's not just a cabinet — it's a statement." · "Not only fast, but also affordable."

**b) Not X, but Y** — asserts the first trait is absent entirely
> "This isn't software. It's a workflow." · "No fluff, no filler, just results."

**c) X rather than Y** — the reversed form, easy to miss because it reads analytical
> ❌ We prioritize consistent stock rather than the widest catalogue.
> ✅ We stock 40 lines and keep every one of them in the warehouse.

All three share one root problem: they define the product by what it isn't. Say what it is.

> ❌ It's not just a cabinet — it's a statement.
> ✅ It's a cabinet built to your exact size.

### 2.2 Copula avoidance — say "is"

LLMs systematically replace plain *is/are* with inflated alternatives. One cited study found a >10% drop in "is"/"are" usage in academic writing the year LLMs became widely available, and that asking GPT to "revise the following sentence" reliably removed them.

Watch for: *serves as · stands as · marks · functions as · operates as · represents · refers to*

**And the marketing-verb variant, which is the one that will bite you here:** the article notes LLMs specifically prefer *boasts · features · offers · maintains* over the plain *has*. These read as normal product copy, which is exactly why they slip through.

> ❌ Our warehouse boasts over 2,000 square metres and features climate control.
> ✅ Our warehouse is 2,000 square metres and it's climate controlled.

Also flagged: elaborated biography verbs — "began his career as" / "ventured into politics as a candidate" where "was" would do.

### 2.3 Rule of three

LLMs overuse triads — "adjective, adjective, adjective" or "short phrase, short phrase, and short phrase" — and the article notes they specifically use the structure "to make superficial analyses appear more comprehensive." Three items feel researched whether or not the third item earned its place.

One triad on a page is fine and often good rhythm. Three triads is a signature. Vary list length: write two items when there are two, four when there are four. Delete any third item that exists only for cadence.

> ❌ Fast, simple, and affordable.
> ✅ Delivered next morning. Priced per carton.

### 2.4 Elegant variation — the same thing under five names

Missing from most anti-AI checklists and worth real attention. LLMs carry a repetition penalty that discourages reusing a word, so they keep renaming the same referent. Across one page the product becomes "the platform," "the solution," "this powerful tool," "the system." The customer becomes "users," "clients," "businesses," "partners."

Human copywriters do the opposite: they pick one name for a thing and hammer it, because consistent vocabulary is how a reader learns their way around. (This is the same principle as the interface-writing rule that a "Publish" button must produce a "Published" toast.)

Pick one noun for the product, one for the customer, one for the core action. Repeat them. Repetition reads as confidence.

*Caveat:* the article notes some non-native English speakers avoid repetition because their schooling taught it as good style, so this signals nothing about a human author's tooling. Judge the copy, not the person.

---

## 3. Vocabulary

### 3.1 The corroborated list

Wikipedia only admits a word here when its overuse is backed by an external study, which makes this list far more reliable than the usual "banned AI words" listicle:

> *Additionally* (esp. starting a sentence) · *align with* · *boasts* (meaning "has") · *bolstered* · *crucial* · *delve* · *emphasizing* · *enduring* · *enhance* · *fostering* · *garner* · *highlight* (as a verb) · *interplay* · *intricate/intricacies* · *key* (as an adjective) · *landscape* (abstract) · *meticulous/meticulously* · *pivotal* · *robust* · *showcase* · *tapestry* (abstract) · *testament* · *underscore* (as a verb) · *valuable* · *vibrant*

Plus the promotional cluster: *rich · profound · exemplifies · commitment to · natural beauty · nestled · in the heart of · groundbreaking · renowned · featuring · diverse array*

**Prioritise the current era.** The article tracks which words dominate which model generation, and the list moves — *delve* was the notorious 2023–24 tell and had dropped off sharply by 2025. The words flagged for mid-2025 onward are: ***emphasizing, enhance, highlighting, showcasing***. If you check nothing else, check those four.

### 3.2 Read the list literally

The article's own instruction: *"This section is to be taken as literally as possible: a word being overused by AI does **not** imply that its synonyms are also overused."*

Two consequences:
- Don't extend the ban by analogy. *Showcase* is flagged; *display* and *show* are not. Swapping a flagged word for a plain synonym is the correct fix.
- **Context decides.** *Underscore* is a tell as a figurative verb, not when it means a literal underline. *Key* is a tell as a vague adjective ("a key benefit"), not as a noun.

One or two of these words is coincidence — they are ordinary English. The tell is **density**: several of them, repeatedly, in one piece. The research notes they co-occur; where there's one, look for others.

### 3.3 Keep this separate from ordinary buzzword-cutting

The SKILL.md rules already cut *leverage, utilize, seamless, streamline, optimize, innovative, cutting-edge, game-changing, world-class, best-in-class*. Those are weak marketing writing whether a human or a model wrote them, and they were bad long before 2022.

Both lists should be applied. Don't merge them — they are different problems with the same fix, and conflating them causes over-correction on words that are merely unremarkable rather than diagnostic.

---

## 4. Formatting tells

### 4.1 Inline-header vertical lists

A precise, high-value format tell: a bullet or number, then a **bolded inline header**, then a colon, then descriptive text.

> ❌
> - **Heavy-Duty Dispensers**: Designed for high-traffic restrooms.
> - **Standard Dispensers**: Suitable for offices and small cafés.

This is the default shape of LLM list output. It shows up constantly in feature sections and comparison blocks, where it looks like reasonable product copy. Either write real prose, or use a table if the content is genuinely tabular, or drop the bold-and-colon scaffolding and just write the line.

### 4.2 Mechanical boldface

The article traces the habit to readmes, how-tos, slide decks, listicles — **and sales pitches**, which is the genre being written here. The pattern is bolding every instance of a chosen term, "key takeaways" style, rather than bolding the one phrase that carries the sentence.

Bold should be scarce enough that it still means something. If more than a phrase or two per section is bold, none of it is emphasis.

### 4.3 Title Case headings

LLMs capitalise every significant word in headings. Use sentence case unless the brand's style guide genuinely specifies title case — and if it does, apply it consistently rather than mid-sentence.

### 4.4 Em dashes — a weak signal, handled precisely

Em dashes are legitimate punctuation and good copy uses them. Three specifics from the article make the difference:

- **Spacing is the actual giveaway.** AI output typically writes ` — ` with surrounding spaces, against the typographic convention most human em-dash users follow.
- **Formulaic use.** LLMs deploy them to "punch up" sales-like writing by over-emphasising clauses and parallelisms — frequently, the em dash is what's holding up a negative parallelism (§2.1).
- **Pile-ups.** Several per paragraph, where a human would have used commas, parentheses, or a full stop.

Newer models actively suppress em dashes, so their *absence* proves nothing either. Use them where they're right; don't use them as a rhythm crutch.

### 4.5 Curly quotes, emoji, placeholders

- **Curly quotes:** weak signal with innocent explanations (Chicago style, Word, macOS). Notably, Claude and Gemini typically *don't* produce them. Match the house style; the real error is mixing curly and straight in one document.
- **Emoji as bullets or in headings:** unambiguous tell. Cut unless the brand voice genuinely runs on emoji.
- **Unfilled placeholders:** `[Your Name]`, `[Specific Topic]`, `[link to page]`. The article documents these shipping publicly because someone forgot to fill them in. In marketing copy this reaches production and is seen by customers. Search the draft for `[` before delivering.

---

## 5. Non-English copy

Split the checklist by language before applying it:

- **The vocabulary list (§3) is English-specific.** *Delve*, *tapestry*, *showcase* have no meaningful Farsi, Arabic, or Spanish equivalent. Translating the banned list word-for-word produces nonsense, and models overuse a *different* set of words in each language.
- **The structural tells (§1, §2, §4) survive translation.** Negative parallelism, tacked-on participial analysis, puffery about significance, rule-of-three runs, elegant variation, and formulaic conclusions are all clause-level patterns that appear in any language the model writes. In practice these are the ones that make translated or natively-generated non-English copy read as machine-made.

So for non-English work: apply §1, §2 and §4 in full, and for §3 build the vocabulary sense from that language's own overused-register words rather than importing this list.

---

## 6. Don't over-correct

The article devotes its opening section to caveats, and they apply here:

- **AI detection tools are unreliable.** Don't run copy through one and rewrite on its verdict.
- **These are probabilistic signals, not rules of grammar.** Every item on this list appears in good human writing sometimes. A single instance means nothing; clustering is the signal.
- **The goal is not "sounds un-AI."** It's specific, honest, useful copy. Chasing the checklist too hard produces stilted writing, which fails for a different reason.

If a flagged construction is genuinely the clearest way to say the thing, keep it.

---

## Revision pass

Run after drafting, before handing off:

1. **Read it aloud.** Anything that sounds like a brochure or a LinkedIn post rather than one person talking to another gets rewritten plainer.
2. **Cut every trailing "-ing" clause** that adds commentary rather than information.
3. **Find every "not just X" / "not X, but Y" / "X rather than Y"** and rewrite as a positive statement.
4. **Restore "is."** Hunt *serves as, functions as, boasts, features, offers, maintains, represents*.
5. **Count triads.** More than one per page: break the pattern.
6. **Name-check consistency.** One name for the product, one for the customer, one for the action, throughout.
7. **Scan for the current-era four:** *emphasizing, enhance, highlighting, showcasing*.
8. **Check every claim has a real source** or is cut.
9. **Search for `[`** to catch unfilled placeholders.
10. **Check the ending.** It should land on the CTA or a concrete detail, never a summary.
