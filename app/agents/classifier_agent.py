from app.services.llm_service import ask_gpt

def classify_document(text: str, filename: str) -> str:
    prompt = f"""
You are a document classification agent.

Your job is to classify the following PDF content into exactly one of the following categories:
- bill
- discharge_summary
- id_card

❗ Only respond with one of the three words above — no explanation, no formatting.

Filename: {filename}

Content:
{text[:1500]}
"""

    response = ask_gpt(prompt).strip().lower()

    # ✅ Add this log to see raw classification output in terminal
    print(f"📄 Classifier response from LLM: {response}")

    # ✅ Sanitize output
    allowed = {"bill", "discharge_summary", "id_card"}
    if response in allowed:
        return response
    return "unknown"

