---
name: article-writing
description: Write a publication-ready article in the author's voice from an explored idea or approved brief. Use when the user asks to turn a discussion, thesis, or brief into an article. Do not use for summaries, reviews, translations, or open-ended idea exploration.
---

# Article Writing

Write the article the author would write, from the material the author has developed. Default language: Brazilian Portuguese, unless the user specifies another.

## Input

- Source: an article brief, or the conversation. Use only positions the author adopted. Ideas the assistant proposed and the author did not adopt, and positions the author rejected, are out of scope.
- Optional: additional editorial instructions.

If the thesis, the main argument chain, or another essential element is missing, ask before writing. Do not fill gaps with invention.

## Voice

Write as the author: a solutions architect with startup experience and project-management education. This is background for judgment and vocabulary, not a source of episodes. Never invent experiences, employers, clients, numbers, quotes, or outcomes.

- First person, reflective and pragmatic, with explicit positioning ("I argue", "I believe") where the author holds a position.
- Conceptual rigor in plain language. Argue; do not lecture. No academic apparatus.
- To calibrate voice and rhythm, read the opening and a few paragraphs of 2 or 3 recent published articles on different topics, when available. Never reuse their wording, arguments, or structure.

## Opening

Start from the author's own vantage point: a real episode, an observation, a question, or a motivation taken from the source, then move toward the thesis. Use an episode only if the author told it. If the source has none, open from the observation or question that led to the thesis. Avoid generic hooks, scene-setting clichés, and questions asked only to grab attention.

## Argument and prose

- One thesis, developed in layers. Each section adds a development; transitions carry the reasoning.
- Substantial paragraphs of continuous prose. Start a new paragraph only when the idea changes. No lists.
- Keep the counterarguments the author engaged with at full strength.
- Make no claim beyond the source. State unverified factual claims as the author's belief, or flag them in the notes.
- Cut repetition, filler, and jargon. Length follows the material (published articles run roughly 2,000 to 5,000 words). Never pad.
- End when the argument is complete: no recap of what was just said, no moralizing closing line.

## Avoid

- "Not X, but Y" as a recurring device; use it sparingly.
- Triplets and rhetorical questions answered immediately.
- Signposting ("In this article I will...") and stock openers or closers ("Em um mundo cada vez mais...", "No fim das contas", "Em suma").
- Empty intensifiers and stock words (crucial, fundamental, verdadeiramente, jornada, ecossistema used loosely).
- Bold, em dashes, and emoji. Do not replace em dashes with excess colons or semicolons.

## Format

Produce exactly:

    # Title

    _Subtitle_

    {{RESUMO}}

    ---

    Body

- Title: original, expresses the central idea, sentence case.
- Subtitle: complements the title (scope, perspective, or central argument); never restates it.
- `{{RESUMO}}` is a placeholder replaced later by the summary step. Never write or alter the summary.
- The opening has no heading. Use H2 headings only when they advance the argument; avoid generic ones ("Introduction", "Conclusion") or ones that restate the paragraph. Zero headings is acceptable.
- Link only to articles the author mentioned. Never invent URLs.

## Output

Return the article. Only if needed, add after it a block headed `Notes for the author (not part of the article)` listing claims to verify and places where the source was ambiguous and you made a choice. Omit the block otherwise.
