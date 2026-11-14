---
name: translate-text
description: Translate text into a specified target language while preserving its original structure, Markdown formatting, meaning, tone, and content.
---

# Translate Text

Translate the provided text into the specified target language.

## Inputs

- `text`: Source text to translate.
- `target_language`: Target language. Required.

If the target language is missing or ambiguous, ask the user before proceeding. Infer the source language automatically.

## Instructions

- Preserve the original meaning, content, tone, and order.
- Preserve Markdown structure and formatting exactly.
- Do not add, remove, reorder, or modify formatting markers.
- Translate textual content only.
- Preserve code blocks, inline code, URLs, identifiers, and non-translatable technical elements.
- Preserve headings, lists, tables, links, blockquotes, and other Markdown structures.
- Do not summarize, interpret, adapt, or improve the source text.
- Do not omit or introduce information.
- Maintain terminology consistency throughout the translation.

## Output

Return only the translated text.

Do not include introductions, explanations, notes, translation labels, or conclusions.
