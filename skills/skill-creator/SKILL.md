---
name: skill-creator
description: Design, create, and refine reusable AI skills through an interactive, inference-driven process. Use when a user requests a new skill or a substantial redesign of an existing one.
---

# Skill Creator

## Objective

Design and implement effective, portable AI skills with minimal context consumption.

## Workflow

### 1. Discovery

Understand the capability or problem the user wants to address.

- Identify purpose, intended users, execution context, and expected outcomes.
- Accept incomplete ideas and infer missing details.
- Ask focused questions only when ambiguity materially affects the design.

### 2. Specification

Define the Skill's:

- Purpose and scope.
- Activation conditions.
- Inputs and expected outputs.
- Execution workflow and decision points.
- Expected behaviors (Do's) and prohibited behaviors (Don'ts).
- Constraints, dependencies, and autonomy level.
- Quality criteria.

Infer reasonable defaults. Discuss relevant alternatives and challenge assumptions when necessary.

### 3. Design

Translate the specification into operational instructions.

- Define a clear, executable workflow.
- Handle incomplete inputs, ambiguity, and exceptions.
- Establish when to infer, ask, or seek approval.
- Avoid overlapping responsibilities and unnecessary features.

### 4. Context Optimization

Minimize token consumption without compromising execution.

- Use concise, imperative instructions.
- Eliminate repetition and unnecessary explanations.
- Include only operationally relevant information.
- Avoid redundant examples, metadata, and documentation.
- Create supporting files only when essential.
- Prefer progressive disclosure for supplementary content.

Optimize for the smallest effective implementation, not merely the shortest file.

### 5. Approval

Before implementation, present the complete proposed `SKILL.md` for approval.

Include the name, description, scope, workflow, and relevant design decisions.

Incorporate requested changes and resubmit the proposal when necessary.

Never create or modify files without explicit approval.

### 6. Implementation

After approval:

1. Locate the project root relative to the Skill Creator's own location.
2. Create the Skill under `skills/<skill-name>/SKILL.md`.
3. Follow the Agent Skills specification.
4. Generate supporting files only when essential.
5. Preserve existing content. Never overwrite an existing Skill without explicit authorization.
6. Avoid absolute paths, repository-specific assumptions, and machine-specific dependencies.

If the project root or destination cannot be identified reliably, ask the user.

### 7. Validation

Verify:

- Metadata and naming conventions.
- Activation description and scope.
- Input and output definitions.
- Workflow completeness and consistency.
- Behavioral rules and constraints.
- Absence of contradictions and redundancy.
- Context efficiency.
- Correct file location.

Correct any implementation issues before completion.

### 8. Completion

Report the created Skill, location, capabilities, and validation result. Mention unresolved limitations when applicable.

## Principles

- Interactive and inference-driven design.
- Minimal user intervention.
- Explicit approval before implementation.
- Clear responsibilities and predictable execution.
- Portability across projects.
- Context efficiency as a design constraint.
