def extract_text(filename: str, data: bytes) -> str:
    name = filename.lower()

    if name.endswith(".txt"):
        return data.decode("utf-8", errors="replace")

    # ЗАГЛУШКА для DOCX/PDF: потом здесь будет реальное извлечение
    return (
        f"ЗАГЛУШКА: извлечение текста из {filename} ещё не реализовано. "
        "Для демонстрации используйте TXT-файл."
    )