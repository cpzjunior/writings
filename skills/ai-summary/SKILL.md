---
name: ai-summary
description: Create concise, topic-by-topic English summaries of articles for AI agent consumption, preserving substantive information while eliminating Markdown structure and redundant content.
---

# AI Summary

Transform the provided article into a condensed representation optimized for consumption by other AI agents.

## Inputs

- `text`: Complete source article.

If the source article is missing, request it. Detect its language automatically.

## Instructions

- Write entirely in English, regardless of the source language.
- Preserve the original topic sequence and argumentative progression.
- Organize content into coherent paragraphs, one per major topic or closely related group of ideas.
- Preserve central arguments, concepts, recommendations, relevant examples, qualifications, and conclusions.
- Eliminate repetitive ideas, redundant expressions, unnecessary context, and secondary details.
- Consolidate related information without losing meaningful distinctions.
- Remove Markdown headings, bullet points, numbering, and other formatting markers.
- Use plain text paragraphs without Markdown formatting.
- Short inline topic labels may be retained when useful for identifying the subject of a paragraph.
- Preserve factual accuracy, terminology, and the author's intended meaning.
- Do not introduce interpretations, assumptions, or information absent from the source.
- Avoid excessive compression that compromises the article's informational value.

## Output

Return only the resulting text, ready to be saved as `README.ai.md`.

Do not include titles, introductions, explanations, lists, Markdown formatting, or conclusions that are not present in the source.
