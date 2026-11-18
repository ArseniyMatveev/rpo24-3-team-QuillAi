_summaries = []


def save(filename: str, summary: str) -> dict:
    record = {
        "id": len(_summaries) + 1,
        "filename": filename,
        "summary": summary,
    }
    _summaries.append(record)
    return record
