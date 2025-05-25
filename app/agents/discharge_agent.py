from app.services.llm_service import ask_gpt
import json

def process_discharge(text: str) -> dict:
    prompt = f"""
Extract the following fields from the discharge summary text and return as JSON:
- type: "discharge_summary"
- patient_name
- diagnosis
- admission_date (in YYYY-MM-DD)
- discharge_date (in YYYY-MM-DD)

Discharge Summary:
{text[:1500]}
"""
    response = ask_gpt(prompt)
    try:
        return json.loads(response)
    except:
        return {"type": "discharge_summary", "error": "LLM parsing failed"}
