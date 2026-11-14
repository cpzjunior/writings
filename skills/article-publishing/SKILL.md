---
name: article-publishing
description: Publish one finalized article version (a single language file) in the project's GitHub repository, identified by article number. Creates the article directory for a new canonical pt-BR article and reuses it for translations. Use when a finalized article or translation is ready to be committed. Do not use to translate other content, summarize, or register index entries.
---

# Article Publishing

Publish exactly one finalized article version per execution. The canonical pt-BR version is published first and creates the article directory. Each translation is published later, separately, into that same directory.

## Input

- `article` (required): finalized Markdown.
- `language` (required): `pt-BR`, `en`, `es`, `it`, or another code. Confirm the text is actually in that language. If not, stop and ask.
- `article_number` (required): the number given by the user.
- Optional additional instructions.

If something essential is missing, ask.

## Workflow

### 1. Inspect

List the top-level article directories, find the one that starts with `<article_number>-`, and read recent commit messages. Identify the default branch. Do not read other articles' content. Do not assume conventions from memory when they can be inspected.

### 2. Determine destination

- No directory exists and `language` is pt-BR: this is a new canonical article. Use `translate-text` to translate the article's H1 title into English. Build the directory as `<article_number>-<slug>`. The slug is the English title in lowercase, words separated by single hyphens, other punctuation removed (apostrophes, commas, colons, question marks, quotes), digits kept. Example: "Games Don't Need a Netflix, They Need an AWS" becomes `games-dont-need-a-netflix-they-need-an-aws`. The directory does not exist beforehand: it is created by committing the file at `<directory>/README.pt-BR.md`. If the number is not the next sequential one, warn the user but do not block.
- A directory exists and the target-language file does not: this is another language version. Reuse the directory. Verify it contains the canonical `README.pt-BR.md`.
- Any other case stops with an explanation: a pt-BR file that already exists (never overwrite), a non-pt-BR version without a canonical, or an existing target file.

### 3. Prepare file

Filename by language: `README.pt-BR.md`, `README.md` (English), `README.es.md`, `README.it.md`, `README.<code>.md` for others. The content is the article exactly as supplied.

### 4. Validate (before writing)

- The destination path is correct and does not already exist. For a new article, re-check the directory list immediately before writing.
- The filename matches the language.
- Present: title (H1), subtitle, summary paragraph, `---` separator.
- Absent: `{{RESUMO}}`, any "Notas para o autor" or "Notes for the author" block, and other placeholders.
- English version only: the slug of its H1 equals the slug of the directory. If it differs, stop and report both titles.
- Translations: structural parity with the canonical version (same number of headings, paragraphs, and links). Read the canonical only for this check.
- No unrelated changes in the commit.

### 5. Publish

- Ask the user to authorize, showing the full destination path (for a new article, this includes the directory name derived from the English title).
- Commit only this file, directly to the default branch, unless the repository requires pull requests. Use a short message in the style of recent history.
- Verify by reading the committed file from the default branch and comparing it with the prepared content. Report success only after this.
- Without write access or authorization, prepare the file and report its exact path and content.

## Constraints

- One version per execution. Never batch languages or articles.
- Do not translate anything other than the title (new article only), and do not summarize, edit content, or touch indexes, other files, or previously published versions.
- Process only the supplied version and essential repository metadata.

## Output

Report the directory, file path, language, commit reference, and verification result. For a new article, also report the English title used, so the English version can reuse it. Clearly distinguish prepared files from published files.
