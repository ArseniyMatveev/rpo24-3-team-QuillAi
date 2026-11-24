import httpx


MODEL = "qwen2.5:3b"
OLLAMA_URL = "http://localhost:11434/api/chat"

def ask_model(prompt: str) -> str:
    response = httpx.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "stream": False,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=180,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]


def summarize(text: str) -> str:
    text = text[:20_000]
    prompt = (
        "Ты — сервис QuillAI. Сделай краткий конспект текста. "
        "Сохрани ключевые смыслы. Не добавляй факты, которых нет в исходном тексте. "
        "Верни только конспект, без пояснений.\n\n"
        f"Текст:\n{text}"
    )
    return ask_model(prompt)