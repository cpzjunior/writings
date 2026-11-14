---
name: skill-creator
description: Design, create, review, and refine reusable AI skills. Use whenever the user asks to create a skill, improve an existing skill, review its design, or redesign a skill pipeline. Never use for one-off prompts, ordinary instructions, or tasks that do not require reusable AI capabilities.
---

# Skill Creator

Design skills that are precise, portable, maintainable, and efficient in context.

A skill is read by a model with no memory of the conversation that created it. Every instruction must therefore be understandable and actionable on its own.

## Workflow

### 1. Discover

- Identify the skill's purpose, intended users, activation conditions, inputs, and expected outputs.
- If the skill already exists, read it before proposing changes.
- Read sibling skills and identify upstream and downstream dependencies.
- Identify existing skills that could be reused or extended instead of creating new ones.
- Ask the user for missing information unless explicit permission to infer has been provided.
- Ask only for information necessary to define the skill correctly.

### 2. Specify and Design

Define the skill's specification before writing it.

**Responsibility and scope**
- Define its primary responsibility.
- Explicitly state what is out of scope.
- Identify opportunities to reuse, extend, merge, or split existing skills.

**Activation**
- Define when the skill must be used.
- Define when the skill must never be used.
- Write the description to support accurate activation, including phrases users are likely to use.

**Interface**

Define an explicit interface for every skill, following programming method conventions.

- Inputs: named parameters in English, with their types, purposes, and required or optional status.
- Outputs: named return values in English, with their types, purposes, and expected formats.
- Context: information available from the execution environment that does not need to be supplied as an input parameter.
- Dependencies: external tools, resources, and other skills required for execution.
- Side effects: identify persistent or external changes produced by execution.

For each input:
- Use a clear, descriptive name in English.
- Specify its data type.
- Describe its purpose and constraints.
- State whether it is required or optional.
- Define its behavior when optional and omitted.

For each output:
- Use a clear, descriptive name in English.
- Specify its data type.
- Describe its purpose and expected format.

**Missing information and inference**
- Do not assume missing required information.
- Ask the user for missing information unless explicit permission to infer has been provided.
- When inference is authorized, infer only what is necessary and disclose material assumptions.
- Never interpret permission to infer as permission to perform external actions or create side effects.

**Workflow and decision-making**
- Define execution steps and decision points.
- Specify when to infer, ask the user, request approval, or stop.
- Define failure handling for incomplete inputs, unavailable tools, missing dependencies, and conflicting instructions.

**Dependencies and compatibility**
- Define the expected inputs and outputs of dependent skills.
- Resolve interface conflicts explicitly.
- Avoid circular dependencies and unnecessary coupling.

Challenge assumptions and propose alternatives when the requirement is better served by reusing, extending, merging, or splitting existing skills.

### 3. Write

- Use concise, imperative instructions.
- Include a short reason for rules that are non-obvious or easy to misapply.
- Omit instructions that do not meaningfully change the model's behavior.
- Prefer one short example over lengthy explanations when format or behavior is subtle.
- State each rule once.
- Resolve conflicts between rules explicitly.
- Keep SKILL.md concise, generally under 500 lines.
- Move extensive documentation and reference material into supporting files loaded only when needed.
- Avoid absolute paths, hardcoded URLs, and repository-specific assumptions.
- If the skill is intended for a specific repository or environment, state that assumption explicitly.

### 4. Approve

Before modifying any file:

- Present the complete proposed SKILL.md.
- For existing skills, present a diff and a concise summary of proposed changes.
- Explain relevant design decisions and assumptions.
- Identify decisions the user may want to challenge.

Incorporate feedback and resubmit the proposal when necessary.

Never create or modify files without explicit user approval.

### 5. Implement

1. Identify the skills directory by inspecting the project. If it cannot be identified reliably, ask the user.
2. Create or update `<skills-dir>/<skill-name>/SKILL.md`.
3. Use lowercase letters, digits, and hyphens for skill names. The name must match its directory and contain no more than 64 characters.
4. Keep the description within 1024 characters.
5. Add supporting files only when necessary.
6. Never overwrite an existing skill without explicit authorization.

### 6. Validate

Prepare 2 or 3 realistic test scenarios covering:

- Normal execution with valid inputs.
- Missing or ambiguous required inputs.
- A scenario that must not activate the skill.

For each scenario:
- Present the input.
- Describe the expected behavior.
- Identify the expected output or decision.

Present the scenarios to the user for validation.

Do not claim successful validation until the user has reviewed and approved the proposed behavior.

Incorporate feedback and revise the skill when necessary.

### 7. Report

After implementation, report only:

- Skill name and location.
- What was created or modified.
- Validation status.
- Known limitations, if any.

Keep the report concise.

## Principles

- One responsibility per skill, with a clear interface to its dependencies.
- Explicit inputs and outputs, following programming method conventions.
- Ask rather than assume, unless inference is explicitly authorized.
- Explicit approval before any file change.
- Human validation of expected behavior.
- Smallest effective instructions, not merely the shortest.
- Prefer reuse over unnecessary duplication.
