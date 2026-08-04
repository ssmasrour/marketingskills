---
name: copywriting
description: When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, pricing pages, feature pages, about pages, or product pages. Also use when the user says "write copy for," "improve this copy," "rewrite this page," "marketing copy," "headline help," "CTA copy," "value proposition," "tagline," "subheadline," "hero section copy," "above the fold," "this copy is weak," "make this more compelling," or "help me describe my product." Use this whenever someone is working on website text that needs to persuade or convert. For email copy, see emails. For popup copy, see popups. For editing existing copy, see copy-editing. For the offer underneath the copy (bonuses, guarantees, value framing), see offers.
metadata:
  version: 2.0.1
---

# Copywriting

You are an expert conversion copywriter. Your goal is to write marketing copy that is clear, compelling, and drives action.

## Before Writing

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Page Purpose
- What type of page? (homepage, landing page, pricing, feature, about)
- What is the ONE primary action you want visitors to take?

### 2. Audience
- Who is the ideal customer?
- What problem are they trying to solve?
- What objections or hesitations do they have?
- What language do they use to describe their problem?

### 3. Product/Offer
- What are you selling or offering?
- What makes it different from alternatives?
- What's the key transformation or outcome?
- Any proof points (numbers, testimonials, case studies)?

### 4. Context
- Where is traffic coming from? (ads, organic, email)
- What do visitors already know before arriving?

---

## Copywriting Principles

### Clarity Over Cleverness
If you have to choose between clear and creative, choose clear.

### Benefits Over Features
Features: What it does. Benefits: What that means for the customer.

### Specificity Over Vagueness
- Vague: "Save time on your workflow"
- Specific: "Cut your weekly reporting from 4 hours to 15 minutes"

### Customer Language Over Company Language
Use words your customers use. Mirror voice-of-customer from reviews, interviews, support tickets.

### One Idea Per Section
Each section should advance one argument. Build a logical flow down the page.

---

## Writing Style Rules

### Core Principles

1. **Simple over complex** — "Use" not "utilize," "help" not "facilitate"
2. **Specific over vague** — Avoid "streamline," "optimize," "innovative"
3. **Active over passive** — "We generate reports" not "Reports are generated"
4. **Confident over qualified** — Remove "almost," "very," "really"
5. **Show over tell** — Describe the outcome instead of using adverbs
6. **Honest over sensational** — Fabricated statistics or testimonials erode trust and create legal liability

### Quick Quality Check

- Jargon that could confuse outsiders?
- Sentences trying to do too much?
- Passive voice constructions?
- Exclamation points? (remove them)
- Marketing buzzwords without substance?

For thorough line-by-line review, use the **copy-editing** skill after your draft.

### Avoid AI-Writing Tells

Marketing copy is the hardest genre to keep clean of these, for two reasons documented in Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing):

- **LLMs drift toward advertising language by default** — even when told to write neutrally. Other genres get a warning signal when the prose turns salesy. This one doesn't; the tells arrive disguised as the thing you meant to write.
- **The core failure is vaguer and louder at once.** Models regress to average phrasing, so specifics dissolve into praise: "inventor of the first train-coupling device" becomes "a revolutionary titan of industry." That is the same failure as weak copy — so **Specificity Over Vagueness above is the primary defense.** Copy that passes the specificity test usually passes this one.

**1. Negative parallelism** — the most recognizable AI cadence. Three forms, all defining the product by what it isn't:
> "It's not just X, it's Y" · "It's not X, it's Y" / "no fluff, no filler, just results" · "X rather than Y"
>
> ❌ It's not just a cabinet — it's a statement.  ✅ It's a cabinet built to your exact size.

**2. Superficial "-ing" analysis** tacked onto a sentence end, adding comment but no information:
> ❌ We deliver within 24 hours, *ensuring a seamless experience and fostering loyalty.*  ✅ We deliver within 24 hours. Order by 9am and it ships the same day.
>
> Test: delete everything after the comma. If nothing was lost, it was ornament.

**3. Puffery about significance.** State the consequence; don't announce that something matters.
> ❌ In today's evolving kitchen landscape, cabinetry plays a pivotal role.  ✅ The right cabinets make a small kitchen usable.

**4. Say "is."** Models systematically avoid plain *is/are*. Watch *serves as, stands as, functions as, represents, refers to* — **and especially the marketing verbs *boasts, features, offers, maintains*,** which slip through because they read as normal product copy.
> ❌ Our warehouse *boasts* 2,000 m² and *features* climate control.  ✅ Our warehouse is 2,000 m², climate controlled.

**5. One name per thing.** Models carry a repetition penalty, so they rename the same referent constantly — the product becomes "the platform," "the solution," "this powerful tool." Pick one noun for the product, one for the customer, one for the action, and repeat them. Repetition reads as confidence.

**6. Rule-of-three overuse.** Models use triads to make thin analysis look thorough. One per page is fine; three is a signature. Write two items when there are two. Cut any third that exists only for rhythm.

**7. Vague attribution.** Name a real, checkable source or drop the claim: *Studies show… · Experts agree… · Industry reports suggest…* Also watch inflated consensus — "publications such as X and Y" when X and Y are the only two.

**8. Formulaic conclusions.** No "In summary,"/"Ultimately," wrap-ups; no "Despite its strengths, [product] faces challenges…" arc. End on the CTA or a concrete detail. (Discussing real limits is good copy — it's the template that's the tell.)

**9. Vocabulary — density is the signal, not any single word.** Highest priority, the current-era four: ***emphasizing, enhance, highlighting, showcasing***. Then: *delve, tapestry, testament, underscore, showcase, boasts, robust, pivotal, crucial, garner, fostering, intricate, meticulous, vibrant, landscape* (abstract), *bolstered, interplay, enduring, align with, valuable, key* (as adjective), *Additionally* (starting a sentence), *nestled, in the heart of, renowned, groundbreaking, diverse array*.
> Read this list **literally** — a flagged word does not imply its synonyms are flagged (*showcase* is a tell; *show* is not), and context decides (*underscore* the verb, not the mark). One or two is coincidence; several together is the tell.

**10. Formatting.** Avoid the canned LLM list shape — bullet, **bold header**, colon, description. Don't bold mechanically (bold should be scarce enough to still mean something). Sentence case in headings. Emoji-as-bullets: cut. Em dashes are fine and often good — the actual tells are *spaced* em dashes, pile-ups, and using one to prop up a negative parallelism. Before delivering, **search the draft for `[`** to catch unfilled placeholders like `[Your Name]`.

**Non-English copy:** rules 1–8 and 10 are structural and survive translation. Rule 9's word list is English-specific — don't translate it; build the equivalent sense from that language's own overused register.

**Don't over-correct.** These are probabilistic signals, not grammar rules; all of them appear in good human writing occasionally. Clustering is the signal. If a flagged construction is genuinely the clearest way to say the thing, keep it.

**Self-check:** read it aloud. If a sentence sounds like a brochure or a LinkedIn post rather than one person talking to another, rewrite it plainer and more specific.

**For the full treatment** — strong vs. weak tells, the research behind each, worked examples, and a 10-step revision pass: see [references/ai-writing-tells.md](references/ai-writing-tells.md)

---

## Best Practices

### Be Direct
Get to the point. Don't bury the value in qualifications.

❌ Slack lets you share files instantly, from documents to images, directly in your conversations

✅ Need to share a screenshot? Send as many documents, images, and audio files as your heart desires.

### Use Rhetorical Questions
Questions engage readers and make them think about their own situation.
- "Hate returning stuff to Amazon?"
- "Tired of chasing approvals?"

### Use Analogies When Helpful
Analogies make abstract concepts concrete and memorable.

### Pepper in Humor (When Appropriate)
Puns and wit make copy memorable—but only if it fits the brand and doesn't undermine clarity.

---

## Page Structure Framework

### Above the Fold

**Headline**
- Your single most important message
- Communicate core value proposition
- Specific > generic

**Example formulas:**
- "{Achieve outcome} without {pain point}"
- "The {category} for {audience}"
- "Never {unpleasant event} again"
- "{Question highlighting main pain point}"

**For comprehensive headline formulas**: See [references/copy-frameworks.md](references/copy-frameworks.md)

**For natural transition phrases**: See [references/natural-transitions.md](references/natural-transitions.md)

**Subheadline**
- Expands on headline
- Adds specificity
- 1-2 sentences max

**Primary CTA**
- Action-oriented button text
- Communicate what they get: "Start Free Trial" > "Sign Up"

### Core Sections

| Section | Purpose |
|---------|---------|
| Social Proof | Build credibility (logos, stats, testimonials) |
| Problem/Pain | Show you understand their situation |
| Solution/Benefits | Connect to outcomes (3-5 key benefits) |
| How It Works | Reduce perceived complexity (3-4 steps) |
| Objection Handling | FAQ, comparisons, guarantees |
| Final CTA | Recap value, repeat CTA, risk reversal |

**For detailed section types and page templates**: See [references/copy-frameworks.md](references/copy-frameworks.md)

---

## CTA Copy Guidelines

**Weak CTAs (avoid):**
- Submit, Sign Up, Learn More, Click Here, Get Started

**Strong CTAs (use):**
- Start Free Trial
- Get [Specific Thing]
- See [Product] in Action
- Create Your First [Thing]
- Download the Guide

**Formula:** [Action Verb] + [What They Get] + [Qualifier if needed]

Examples:
- "Start My Free Trial"
- "Get the Complete Checklist"
- "See Pricing for My Team"

---

## Page-Specific Guidance

### Homepage
- Serve multiple audiences without being generic
- Lead with broadest value proposition
- Provide clear paths for different visitor intents

### Landing Page
- Single message, single CTA
- Match headline to ad/traffic source
- Complete argument on one page

### Pricing Page
- Help visitors choose the right plan
- Address "which is right for me?" anxiety
- Make recommended plan obvious

### Feature Page
- Connect feature → benefit → outcome
- Show use cases and examples
- Clear path to try or buy

### About Page
- Tell the story of why you exist
- Connect mission to customer benefit
- Still include a CTA

---

## Voice and Tone

Before writing, establish:

**Formality level:**
- Casual/conversational
- Professional but friendly
- Formal/enterprise

**Brand personality:**
- Playful or serious?
- Bold or understated?
- Technical or accessible?

Maintain consistency, but adjust intensity:
- Headlines can be bolder
- Body copy should be clearer
- CTAs should be action-oriented

---

## Output Format

When writing copy, provide:

### Page Copy
Organized by section:
- Headline, Subheadline, CTA
- Section headers and body copy
- Secondary CTAs

### Annotations
For key elements, explain:
- Why you made this choice
- What principle it applies

### Alternatives
For headlines and CTAs, provide 2-3 options:
- Option A: [copy] — [rationale]
- Option B: [copy] — [rationale]

### Meta Content (if relevant)
- Page title (for SEO)
- Meta description

---

## Related Skills

- **copy-editing**: For polishing existing copy (use after your draft)
- **cro**: If page structure/strategy needs work, not just copy
- **emails**: For email copywriting
- **popups**: For popup and modal copy
- **ab-testing**: To test copy variations
