---
name: skill-creator
description: Design, create, and refine reusable AI skills through an interactive process. Use when the user asks to create a new skill, edit or improve an existing one, or redesign a pipeline of skills. Do not use for one-off prompts that will not be reused.
---

# Skill Creator

Design skills that are precise, portable, and cheap in context. A skill is read by a model with no memory of this conversation, so every instruction must be understandable on its own.

## Workflow

### 1. Discover

- Identify the purpose, who or what triggers the skill, what it receives, and what it must produce.
- If the skill already exists, read it first. Read its sibling skills too, noting what upstream skills produce and downstream skills consume.
- Infer details that are cheap to get wrong. Ask only when a wrong guess would materially change scope, autonomy, output format, or irreversible actions.

### 2. Specify and Design

Define in one pass:

- Scope, including what is explicitly out of scope.
- Activation: when to use the skill and when not to.
- Inputs, with the behavior when they are missing, and outputs, with their exact format.
- Workflow, with decision points: when to infer, ask, or stop for approval.
- Failure handling: incomplete input, unavailable tools or dependencies, conflicting rules.
- Dependencies on other skills or external resources.

Challenge assumptions. Propose alternatives when the need is better served differently, such as merging with an existing skill or splitting one.

### 3. Write

- Use concise, imperative instructions. Add a short reason to any rule that is non-obvious or easy to misapply.
- Omit what the model already does by default. Keep only what changes its behavior.
- Prefer one short example over a paragraph when format or tone is subtle.
- State each rule once. If several skills share a rule or reference, keep it in one place and point to it.
- Resolve conflicts between rules explicitly instead of leaving them to guesswork.
- Keep SKILL.md under about 500 lines. Move bulky material to supporting files loaded only when needed.
- Avoid absolute paths, hardcoded URLs, and repository-specific assumptions. If the skill exists for one repository, state that assumption once.
- Write the description for activation: what the skill does, when to use it (including phrases a user would actually say), and when not to.

### 4. Approve

Present the complete proposed SKILL.md before touching any file. For edits to an existing skill, present a diff and a short summary of what changes and why. List design decisions the user may want to contest.

Incorporate feedback and resubmit. Never create or modify files without explicit approval.

### 5. Implement

1. Find the skills directory by inspecting the project. If it cannot be identified reliably, ask.
2. Create or update `<skills-dir>/<skill-name>/SKILL.md`. The name uses lowercase letters, digits, and hyphens, matches its directory, and has at most 64 characters. The description has at most 1024 characters.
3. Add supporting files only when essential.
4. Never overwrite an existing skill without explicit authorization.

### 6. Validate

Check the file against the specification, then test it:

- Write 2 or 3 realistic prompts, including one with missing or ambiguous input and one that should not trigger the skill.
- Run them, or simulate them as a fresh reader, and compare the results with the intended outputs and rules.
- Check for contradictions, redundancy, unmet dependencies, and consistency with sibling skills.

Fix issues and revalidate.

### 7. Report

Report the skill's name and location, what was validated and how, and any known limitations.

## Principles

- Infer what is cheap to get wrong. Ask about what is expensive.
- One responsibility per skill, with a clear interface to its neighbors.
- Explicit approval before any file change.
- Smallest effective instructions, not merely the shortest.
