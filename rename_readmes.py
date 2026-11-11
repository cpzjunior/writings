from pathlib import Path

ROOT = Path(__file__).resolve().parent

RENAMES = {
    "ai.md": "README.ai.md",
    "en.md": "README.md",
    "es.md": "README.es.md",
    "it.md": "README.it.md",
    "pt-BR.md": "README.pt-BR.md",
}

for source in ROOT.rglob("*"):
    if not source.is_file() or ".git" in source.parts:
        continue

    new_name = RENAMES.get(source.name)

    if new_name:
        target = source.with_name(new_name)

        source.replace(target)
        print(f"[RENAMED] {source} -> {target}")

print("Processamento concluído.")