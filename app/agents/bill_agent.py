from app.services.llm_service import ask_gpt
import json

def process_bill(text: str) -> dict:
    prompt = f"""
Extract the following fields from the hospital bill text below and return as a JSON object:
- type: "bill"
- hospital_name
- total_amount (number only)
- date_of_service (in YYYY-MM-DD)

Bill Text:
{text[:1500]}
"""
    response = ask_gpt(prompt)
    try:
        return json.loads(response)
    except:
        return {"type": "bill", "error": "LLM parsing failed"}
