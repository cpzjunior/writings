---
name: ai-index
description: Register published articles in the repository's root README.ai.md semantic index, following its existing structure and conventions.
---

# AI Index

Register a published article in the repository's root AI index.

## Inputs

- `article_url`: URL of the published article's README.md. Required.

If missing, request the URL.

## Workflow

### 1. Inspect

- Retrieve the published article's README.md.
- Retrieve its directory-level README.ai.md.
- Retrieve the repository root README.ai.md.
- Treat the root index as the canonical template.
- Identify the article slug, title, directory, and existing index entries.

### 2. Build Entry

Extract and prepare:

- Article identifier: next available sequential identifier, following existing conventions.
- Slug: canonical article directory name.
- Topics: concise semantic keywords representing the article's main concepts.
- Thesis: concise statement of the central argument.
- Path: relative path to the article's README.ai.md.

Use the article and its AI summary as sources. Do not invent topics or claims.

### 3. Update Index

- Add the entry following the existing format and ordering.
- Preserve all existing entries.
- Check for duplicates before insertion.
- Do not modify unrelated content.
- Maintain consistent identifiers and relative paths.

### 4. Validate

Verify the new entry against the published article and its README.ai.md.

Check identifier uniqueness, path correctness, topic relevance, thesis accuracy, and formatting consistency.

## Constraints

- Only register published articles.
- Do not generate or modify article summaries.
- Do not reorganize or rewrite existing index entries.
- Do not assume a fixed repository name or absolute path.
- If repository access or write permissions are unavailable, provide the exact entry and insertion location.

## Output

Report the registered article, identifier, topics, thesis, and updated index path. If implementation was not possible, provide the proposed entry without claiming completion.
