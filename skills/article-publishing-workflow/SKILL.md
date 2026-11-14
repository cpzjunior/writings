---
name: article-publishing-workflow
description: Orchestrate the complete editorial lifecycle of articles, from idea exploration and writing to critical review, multilingual publication, and AI indexing.
---

# Article Publishing Workflow

Coordinate the complete lifecycle of an article, from initial idea exploration to publication and indexing in the repository.

Delegate specialized tasks to existing Skills. Do not duplicate their internal instructions.

## Skills

- `idea-exploration`: Explore and develop ideas, arguments, and perspectives.
- `article-writing`: Produce the article.
- `critical-review`: Critically evaluate the article.
- `text-summary`: Generate the concise, first-person article summary.
- `translate-text`: Translate the article.
- `article-publishing`: Publish article files in the repository.
- `translation-index`: Register published translations in language indexes.
- `ai-summary`: Generate the AI-oriented article summary.
- `ai-index`: Register the article in the semantic AI index.

If a required Skill is unavailable, inform the user rather than silently replacing its responsibilities.

## Workflow

### 1. Editorial Development

Run the following iterative cycle:

1. Use `idea-exploration` to explore the topic, develop arguments, and examine alternative perspectives.
2. When sufficient material has been developed, use `article-writing` to produce the article.
3. Use `critical-review` to evaluate its argumentation, consistency, originality, and publishability.
4. Incorporate relevant feedback and return to exploration, writing, or both as necessary.

Repeat this cycle until the user explicitly approves the article for publication.

The publication decision belongs exclusively to the user. Never infer approval from a positive review or from the article appearing complete.

### 2. Summary

After approval:

1. Use `text-summary` on the finalized Brazilian Portuguese article.
2. Insert its output into the article's `Resumo` section.
3. Preserve the remaining article content without modification.

The summary must remain in the author's first-person voice, following the specialized Skill's instructions.

The resulting article, including its summary, becomes the canonical version for publication and translation.

### 3. Brazilian Portuguese Publication

Use `article-publishing` to publish the canonical article in Brazilian Portuguese.

Treat this version as the original source for all subsequent language versions.

### 4. English Publication

1. Use `translate-text` to translate the complete canonical article, including its summary, into English.
2. Use `article-publishing` to publish the English version.
3. Use `translation-index` to register the published English version.

### 5. Spanish Publication

1. Translate the canonical Brazilian Portuguese article into Spanish using `translate-text`.
2. Publish the Spanish version using `article-publishing`.
3. Register it using `translation-index`.

### 6. Italian Publication

1. Translate the canonical Brazilian Portuguese article into Italian using `translate-text`.
2. Publish the Italian version using `article-publishing`.
3. Register it using `translation-index`.

### 7. AI Summary and Index

1. Use `ai-summary` to generate the AI-oriented summary exclusively from the published English article.
2. Use `article-publishing` to publish the resulting `README.ai.md` in the article directory.
3. Use `ai-index` to register the article in the repository's root semantic index.

## Execution Rules

- Follow the defined sequence and dependencies.
- Preserve the approved Brazilian Portuguese article as the canonical source.
- Always translate from the canonical Portuguese version, never from another translation.
- Generate the AI summary exclusively from the English version.
- Do not modify previously published content without explicit authorization.
- Do not repeat successfully completed stages unnecessarily.
- If a stage fails, preserve completed work and report the failure and its consequences.
- Never register an article or translation in an index before its publication.
- Respect repository conventions through the specialized publishing and indexing Skills.
- Distinguish prepared files from successfully published files.

## Human Approval

Require explicit user approval before:

- Ending the editorial cycle and proceeding to publication.
- Resolving substantive disagreements that could change the article's thesis or conclusions.
- Replacing or modifying already published content.

Routine operations within the approved workflow, including summaries, translations, publication, and indexing, do not require separate approval when the user has already authorized them.

If publication authorization or repository write access is unavailable, follow `article-publishing` instructions for preparing the directory and filenames. Do not claim that publication succeeded.

## Progress Tracking

Maintain the workflow state, including:

- Current stage and completed stages.
- Approved canonical article.
- Summary status.
- Translation status for each language.
- Publication paths and status.
- Translation and AI index status.
- Failures and unresolved issues.

When resuming an interrupted workflow, inspect available artifacts and repository state before executing anything. Reuse valid completed work and continue from the earliest incomplete stage.

## Completion

Report the status of each language version, the AI summary, and all corresponding index entries.

Clearly identify successfully published artifacts, prepared but unpublished files, and any outstanding actions.
