import httpx


def summarize(text: str) -> str:
    # ЗАГЛУШКА: потом здесь будет запрос к модели для создания конспекта
    return "Краткий конспект: " + text[:80] + "..."


def ask_model(prompt: str) -> str:
    response = httpx.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "qwen2.5:3b",
            "stream": False,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]
