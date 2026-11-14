---
name: text-summary
description: Write the first-person Resumo of a finalized article in Brazilian Portuguese (pt-BR), stating the author's thesis, reasoning, and conclusion in a single paragraph of exactly five sentences. Use after the article is approved. Do not use for AI-oriented summaries, translations, or summaries of other texts.
---

# Text Summary

Condense the finalized article into the author's own presentation of its central idea. The result is part of the canonical article, so it must be final and in Brazilian Portuguese (pt-BR).

## Input

- `article` (required): the finalized pt-BR article. If missing, ask.

Ignore the `{{RESUMO}}` placeholder or any existing Resumo. Summarize only the body.

## Write

A single paragraph of exactly five sentences, in the first person, as if the author were presenting the idea to the reader. A sentence ends with a period; colons and semicolons do not end a sentence. Keep sentences short to moderate (roughly 15 to 25 words each).

- Open with the author's position: the thesis, or the question it answers, stated directly (for example "Defendo que...", "Proponho...", "Acredito que...").
- Use the middle sentences for the essential progression of the argument, and the last for the conclusion or implication.
- Keep the qualifications that delimit the thesis (what it does not claim). Cut examples, background, repetition, and secondary points.
- Mention a personal experience only if the article treats it as the origin of the thesis. Never add experiences, emotions, numbers, or conclusions that are not in the article.
- Do not change the author's position or add interpretation.
- Plain, direct language and natural rhythm. Avoid academic or bureaucratic wording and the patterns listed under "Avoid" in `article-writing`.

Calibration example, for length and density only. Do not reuse its wording or structure:

> Defendo que o principal dilema arquitetural do MCP não está em centralizar ou distribuir servidores, mas em administrar como suas capacidades são descobertas, selecionadas e disponibilizadas aos agentes. Em ambientes corporativos, disponibilizar todas as ferramentas de uma só vez aumenta a complexidade cognitiva e dificulta a seleção contextual. A solução passa por separar o catálogo global de capacidades, a descoberta progressiva e a execução, combinando governança centralizada com autonomia dos domínios e roteamento inteligente. Assim, os agentes acessam apenas o que precisam, quando precisam, sem assumir a complexidade de administrar toda a infraestrutura. O desafio é transformar a diversidade de recursos corporativos em um ecossistema seletivo, seguro e eficiente.

## Check before returning

- The paragraph has exactly five sentences.
- Every claim traces to a passage in the article.
- The thesis, its main limit, and the conclusion are present.

## Output

Return only the paragraph, as plain text. No label, title, lists, bold, or em dashes. The orchestrating workflow adds the `Resumo` label and places it in the article.
