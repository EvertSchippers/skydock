def read_prompt(name: str) -> str:
    with open(f"me/prompts/{name}.md", "r", encoding="utf-8") as f:
        return f.read()