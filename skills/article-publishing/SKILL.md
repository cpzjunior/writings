---
name: article-publishing
description: Publish one finalized article version at a time in the project's GitHub repository, following its directory, filename, and content conventions.
---

# Article Publishing

Publish one finalized article version per execution in the project's GitHub repository.

## Inputs

- `article`: Finalized article in Markdown.
- `language`: Article language. Required.
- `repository`: Repository context, if not already available.
- `additional_instructions`: Optional publication requirements.

The article must have an approved title and subtitle. If essential content or language information is missing, ask the user.

## Workflow

### 1. Inspect Repository

- Identify the repository root and inspect its README and existing article directories.
- Determine whether this is a new article or another language version of an existing article.
- For a new article, determine the next sequential identifier and inspect the exact directory naming convention.
- For an existing article, locate and reuse its directory.
- Inspect existing language conventions and filename patterns.

Never assume conventions from memory when the repository can be inspected.

### 2. Determine Destination

For a new article, create a directory using:
- The next available sequential identifier.
- The English title.
- Lowercase characters.
- No punctuation, including hyphens, commas, or colons.
- The exact numbering and separator convention used by the repository.

For an existing article, reuse its directory and identifier. Never create another directory for a translation.

### 3. Prepare File

Use the following naming convention:

- English: `README.md`
- Brazilian Portuguese: `README.pt-BR.md`
- Spanish: `README.es.md`
- Italian: `README.it.md`
- Other languages: `README.[language-code].md`, following the project's conventions.

The English title determines the article directory regardless of the publication language.

Preserve the article's title, subtitle, language, Markdown structure, and content.

Process only the supplied language version. Do not request, retrieve, generate, or retain other translations as part of this execution.

Do not generate summaries or modify existing language versions.

### 4. Validate

Verify:
- Correct article directory and identifier.
- Correct filename and language code.
- Presence of title and subtitle.
- Markdown integrity.
- Absence of unintended overwrites or unrelated changes.

### 5. Publish

- If repository write access is available and the user has authorized publication, create the file in the repository.
- Preserve existing content and avoid overwriting files.
- If a commit or pull request is required by the available integration, follow the repository's established workflow.
- Never claim publication without verifying that the change was successfully applied.

If write access or authorization is unavailable, prepare the file and report its exact destination for manual creation.

## Constraints

- Publish exactly one article version per execution.
- Never batch multiple languages or articles.
- Reuse the existing directory for translations.
- Do not generate translations, summaries, or index entries.
- Do not modify unrelated articles or previously published versions.
- Treat the repository's existing conventions as the source of truth.
- Minimize retained context: process only the current article version and essential repository metadata.

## Style Reference

Use the following published article as a reference for the repository's editorial conventions and article presentation:

https://github.com/cpzjunior/writings/blob/main/52-decision-architecture-handbook/README.pt-BR.md

Use it as a reference, not as a template. Follow the actual repository conventions when they differ.

## Output

After successful publication, report the article directory, published filename, language, and commit or pull request reference when available.

If publication was not possible, provide the exact destination path and the prepared content or its preparation status.

Clearly distinguish prepared files from successfully published files.
