from fastapi import APIRouter, UploadFile, File
from typing import List

from app.services.pdf_service import extract_text_from_pdf
from app.agents.classifier_agent import classify_document
from app.agents.bill_agent import process_bill
from app.agents.discharge_agent import process_discharge
from app.agents.validation_agent import validate_claim

router = APIRouter()

@router.post("/process-claim")
async def process_claim(files: List[UploadFile] = File(...)):
    extracted_docs = []

    for file in files:
        content = await file.read()
        text = extract_text_from_pdf(content)
        # ✅ Print the first few lines of extracted text
        print(f"\n📄 Extracted text from {file.filename}:\n{text[:800]}\n{'-'*50}")

        doc_type = classify_document(text, file.filename)

        if doc_type == "bill":
            result = process_bill(text)
        elif doc_type == "discharge_summary":
            result = process_discharge(text)
        else:
            continue

        extracted_docs.append(result)

    validation_result = validate_claim(extracted_docs)

    return {
        "documents": extracted_docs,
        "validation": validation_result,
        "claim_decision": {
            "status": "approved" if not validation_result["missing_documents"] else "rejected",
            "reason": "All documents valid" if not validation_result["missing_documents"] else "Missing or inconsistent documents"
        }
    }
