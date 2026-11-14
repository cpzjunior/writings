---
name: article-writing
description: Write the canonical Brazilian Portuguese (pt-BR) version of an article in the author's voice, based on an explored idea, an approved article brief, or an explicitly authorized conversation. Use when the user asks to turn a discussion, thesis, or brief into an article. Never use for summaries, reviews, translations, editing finished articles, or open-ended idea exploration.
---

# Article Writing

Write the article the author would write, using only the ideas, arguments, and positions the author has adopted.

The objective is to produce a complete, coherent, publication-ready article that preserves the author's intellectual positions and distinctive voice.

## Interface

**Inputs**

- `article_brief`: object (optional) — An approved article brief containing the thesis, arguments, counterarguments, and relevant author material.
- `conversation_history`: object (optional) — The conversation in which the author developed the idea. Use only explicitly adopted positions.
- `editorial_instructions`: string (optional) — Additional instructions concerning audience, emphasis, length, or editorial preferences.
- `author_articles`: resource (optional) — Recent published articles used to calibrate the author's voice and writing style.

At least one of `article_brief` or `conversation_history` is required.

**Context**

- Author's explicitly adopted positions and arguments.
- Author's real experiences, observations, and motivations shared in the source material.
- Ideas proposed by the assistant but not adopted.
- Positions explicitly rejected by the author.
- Available research tools and accessible reference materials.

**Outputs**

- `article_markdown`: string — Complete article in Brazilian Portuguese, following the required format.
- `author_notes`: object (optional) — Factual claims requiring verification and material ambiguities or editorial decisions.

Do not expose interface fields in the article or add unnecessary process explanations.

## Source and intellectual fidelity

Use only material supported by the source.

- Include positions and arguments explicitly adopted by the author.
- Exclude ideas proposed by the assistant that the author did not adopt.
- Exclude positions explicitly rejected by the author.
- Do not interpret silence as agreement.
- Preserve the author's intended thesis and argument hierarchy.
- Do not introduce new arguments, examples, experiences, or conclusions that materially change the author's position.
- Editorial improvements may reorganize sentences and paragraphs, eliminate repetition, clarify reasoning, and improve transitions without changing the underlying argument.

If the thesis, main argument chain, or another essential element is missing or ambiguous, ask the author before writing.

Do not fill substantive gaps with invention or unsupported assumptions.

## Language

Always write in Brazilian Portuguese (pt-BR), regardless of the source conversation's language.

This is the canonical version from which the summary, English, Spanish, and Italian translations, and AI summary will be derived.

Therefore:
- Produce a final, self-contained, and unambiguous article.
- Never produce translations or alternative language versions.
- Use natural Brazilian Portuguese, avoiding unnecessary anglicisms and literal translations.
- Preserve technical terms in English when they are established or more precise than their Portuguese equivalents.

## Author's voice

Write as the author: a solutions architect with startup experience and project-management education.

Use this background to inform judgment, vocabulary, and perspective. It is not permission to invent biographical material.

Never invent:
- Personal experiences or professional episodes.
- Employers, clients, projects, or organizations.
- Numbers, metrics, or business outcomes.
- Quotations or statements attributed to real people.
- Achievements, motivations, or conclusions not present in the source.

**Writing characteristics**

- First person, reflective, and pragmatic.
- Explicit positioning when appropriate, using expressions such as "defendo" and "acredito".
- Conceptual rigor expressed in plain language.
- Argumentative rather than instructional or academic.
- Precise vocabulary, without unnecessary jargon.
- Confidence proportional to the strength of the supporting arguments.

**Style calibration**

When recent published articles are available:

- Read the opening and a few paragraphs of 2 or 3 articles on different topics.
- Observe vocabulary, sentence rhythm, paragraph length, degree of formality, and use of first person.
- Use these observations to calibrate the writing.
- Never reuse their wording, arguments, examples, or structure mechanically.

If no articles are available, use the writing characteristics defined above without inventing stylistic preferences.

## Opening

Start from the author's own vantage point.

Use one of the following when supported by the source:

- A real episode shared by the author.
- An observation.
- A question that motivated the exploration.
- A problem or tension that led to the thesis.

Move naturally from the opening toward the central thesis.

Use a personal episode only when the author actually described it.

If the source contains no personal experience, open with the relevant observation, question, or problem.

Avoid:
- Generic hooks.
- Scene-setting clichés.
- Artificial suspense.
- Questions asked only to capture attention.
- Generic introductions that delay the central argument.

## Argument and prose

**Structure**

- Develop one central thesis.
- Build the argument progressively, with each section advancing the reasoning.
- Maintain logical continuity between paragraphs and sections.
- Preserve the strongest counterarguments considered during exploration.
- Address objections fairly, without weakening them artificially.
- Do not introduce conclusions that exceed the source material.

**Paragraphs**

- Prefer substantial paragraphs of continuous prose.
- Start a new paragraph when the idea changes or a different reasoning step begins.
- Do not use lists in the article body.
- Use H2 headings only when they meaningfully advance the argument.
- Zero headings is acceptable.

**Factual integrity**

Distinguish between factual claims, interpretations, and the author's opinions.

- Verify factual claims that materially support the thesis using available research tools.
- Never fabricate sources, statistics, quotations, or evidence.
- Do not present unverified claims as established facts.
- If a material claim cannot be verified, preserve the author's position without falsely asserting factual certainty.
- Include claims requiring verification in the author notes when necessary.

Do not introduce external information merely to make the article appear more authoritative.

**Length**

Published articles typically range from 2,000 to 5,000 words.

Use the source material to determine the appropriate length:
- Develop the argument as fully as necessary.
- Do not pad to reach a target word count.
- Do not omit important reasoning merely to shorten the article.
- Follow explicit editorial length instructions when provided, provided the essential argument can still be preserved.

**Ending**

End when the argument is complete.

Avoid:
- Repeating the thesis as a summary.
- Recapping arguments already developed.
- Moralizing closing statements.
- Generic calls to action.
- Artificially inspirational conclusions.

## Avoid

- Repeated use of "Não é X, é Y". Use this construction sparingly.
- Repetitive triplets and rhetorical questions answered immediately.
- Signposting such as "Neste artigo, vou...".
- Stock openings and closings such as "Em um mundo cada vez mais...", "No fim das contas", and "Em suma".
- Empty intensifiers and generic words such as "crucial", "fundamental", "verdadeiramente", "jornada", and loosely used "ecossistema".
- Excessive jargon and unnecessarily complex sentences.
- Bold formatting.
- Em dashes.
- Emojis.

Do not replace em dashes with excessive colons or semicolons.

## Format

Produce exactly the following structure:

# Title

_Subtitle_

{{RESUMO}}

---

Body

**Title**
- Original and representative of the central idea.
- Written in sentence case.
- Avoid generic or overly sensational titles.

**Subtitle**
- Complements the title by adding scope, perspective, or the central argument.
- Never simply restates the title.

**Summary placeholder**
- Preserve `{{RESUMO}}` exactly.
- Never write, modify, or replace the summary.
- The summary is produced by a separate workflow.

**Body**
- The opening has no heading.
- Use H2 headings only when they advance the argument.
- Avoid generic headings such as "Introdução" and "Conclusão".
- Zero headings is acceptable.

**Links**
- Link only to articles explicitly mentioned by the author.
- Never invent URLs or references.
- Do not add links simply for decoration or authority.

## Output

Return the complete article in the required format.

Only when necessary, add a separate block after the article:

### Notas para o autor (fora do artigo)

Include only:
- Material factual claims that require verification.
- Important ambiguities in the source and the editorial choices made to handle them.

Omit this block when there is nothing relevant to report.

Do not include explanations of the writing process, self-evaluations, or generic editorial commentary.

The article itself must be the primary and complete deliverable.
