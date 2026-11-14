---
name: translate-text
description: Translate the canonical pt-BR article into a target language, preserving its meaning, tone, and Markdown structure. Use when producing a language version of an approved article, or when translating an article title. Do not use to summarize, edit, or improve the text.
---

# Translate Text

## Input

- `text` (required): the canonical pt-BR article, or its title. Never translate from another translation.
- `target_language` (required). If missing or ambiguous, ask.

## Rules

- Preserve meaning, tone, and order. Do not summarize, interpret, improve, or add notes.
- Preserve the Markdown structure exactly: headings, paragraphs, links, URLs, code, and the separator. Keep links to other articles unchanged.
- Translate the title, the subtitle, the summary label, the summary, and the body. The summary keeps its five sentences.
- Translate idioms and cultural references by meaning. Keep proper names as they are. Do not add explanations.
- Use one rendering per coined term across the whole text. Keep technical terms in the form the target language's professionals actually use.
- The author's style rules carry over: no bold (except the existing summary label), no em dashes (use a period, comma, or colon), no lists that the source does not have.

## Output

Return only the translated Markdown, with no introduction, notes, or labels.
