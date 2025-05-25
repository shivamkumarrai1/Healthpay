from typing import List, Dict

REQUIRED_TYPES = {"bill", "discharge_summary"}

def validate_claim(documents: List[Dict]) -> Dict:
    found_types = set(doc["type"] for doc in documents if "type" in doc)
    missing_documents = list(REQUIRED_TYPES - found_types)
    discrepancies = []

    for doc in documents:
        if doc.get("type") == "discharge_summary":
            try:
                admission = doc["admission_date"]
                discharge = doc["discharge_date"]
                if admission > discharge:
                    discrepancies.append("Admission date is after discharge date.")
            except:
                discrepancies.append("Invalid or missing admission/discharge date.")

        if doc.get("type") == "bill":
            if doc.get("total_amount", 0) <= 0:
                discrepancies.append("Total amount in bill is zero or missing.")

    return {
        "missing_documents": missing_documents,
        "discrepancies": discrepancies
    }
