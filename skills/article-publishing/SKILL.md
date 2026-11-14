---
name: article-publishing
description: Publish articles and their language versions in the project's GitHub repository, following its directory, filename, and content conventions.
---

# Article Publishing

Publish finalized articles in the project's GitHub repository, following its existing structure and conventions.

## Inputs

- `article`: Finalized article in Markdown.
- `translations`: Optional translated versions, each associated with its language.
- `repository`: Repository context, if not already available.
- `additional_instructions`: Optional publication requirements.

The article must have an approved title and subtitle. If essential content or language information is missing, ask the user.

## Workflow

### 1. Inspect Repository

- Identify the repository root and inspect its README and existing article directories.
- Determine the next sequential article identifier.
- Identify the exact directory naming convention, including number placement and separators.
- Inspect existing language conventions and filename patterns.
- Never assume conventions from previous projects or memory when the repository can be inspected.

### 2. Prepare Article Directory

Create a directory using:
- The next available sequential identifier.
- The article's English title.
- Lowercase characters.
- No punctuation, including hyphens, commas, or colons.
- The exact numbering and separator convention already used by the repository.

Do not translate the title to generate the directory name. Use the English title consistently across all language versions.

### 3. Prepare Files

Use the following naming convention:

- English: `README.md`
- Brazilian Portuguese: `README.pt-BR.md`
- Spanish: `README.es.md`
- Italian: `README.it.md`
- Other languages: `README.[language-code].md`, following the project's existing conventions.

The English version is the default `README.md`. The original language must use its explicit language suffix when it is not English.

Preserve each article's title, subtitle, language, Markdown structure, and content.

Do not generate translations or summaries. Use only supplied and finalized content.

### 4. Validate

Before publication, verify:

- Directory name and sequential identifier.
- Correct filenames and language codes.
- Presence of title and subtitle in every version.
- Markdown integrity.
- Consistency between language versions.
- Absence of unintended overwrites or unrelated changes.

### 5. Publish

- If repository write access is available and the user has authorized publication, create the directory and files in the repository.
- Preserve existing content and avoid overwriting files.
- If a commit or pull request is required by the available integration, follow the repository's established workflow.
- Never claim publication without verifying that the changes were successfully applied.

If write access or authorization is unavailable, do not attempt publication. Prepare the proposed structure and report the exact directory and filenames for manual creation.

## Constraints

- Publish only finalized content.
- Do not modify unrelated articles or repository files.
- Do not generate translations, AI summaries, or semantic index entries.
- Do not assume fixed repository paths, numbering, language lists, or separators.
- Treat the repository's existing conventions as the source of truth.

## Output

After successful publication, report the article directory, published files, and commit or pull request reference when available.

If publication was not possible, provide the exact directory path and filename for each article version, along with its corresponding content or preparation status. Clearly distinguish prepared files from files actually published.
