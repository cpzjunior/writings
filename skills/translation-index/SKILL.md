---
name: translation-index
description: Register published article translations in their corresponding language indexes, using localized titles and links to translated articles.
---

# Translation Index

Register a published article translation in the corresponding language index.

## Inputs

- `article_url`: URL of the translated article. Required.

If missing, request the URL.

## Workflow

### 1. Inspect

- Retrieve the translated article.
- Identify its language and localized title.
- Identify the corresponding language index (e.g. README.es.md).
- Inspect the index's existing structure and conventions.
- Identify the original article and its canonical repository directory.

### 2. Build Entry

Create an entry containing only:
- The article title in the target language.
- A relative link to the translated article's README.md.

Use the translated article as the source of truth for its title and language.

### 3. Update Index

- Add the entry to the appropriate language index.
- Follow existing formatting and ordering conventions.
- Preserve all existing entries.
- Check for duplicates before insertion.
- Do not modify unrelated content.

### 4. Validate

Verify the localized title, target language, link destination, and formatting consistency.

## Constraints

- Register only published translations.
- Do not generate or modify translations.
- Do not add summaries, topics, descriptions, or metadata.
- Do not assume a fixed repository name or language list.
- Never infer the target language index when it cannot be identified reliably.
- If repository access or write permissions are unavailable, provide the exact entry and insertion location.

## Output

Report the language, registered title, target URL, and updated index path. If implementation was not possible, provide the proposed entry without claiming completion.
