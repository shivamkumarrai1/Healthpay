from pydantic import BaseModel
from typing import List, Optional

class BillDocument(BaseModel):
    type: str
    hospital_name: str
    total_amount: float
    date_of_service: str

class DischargeSummary(BaseModel):
    type: str
    patient_name: str
    diagnosis: str
    admission_date: str
    discharge_date: str

class ValidationResult(BaseModel):
    missing_documents: List[str]
    discrepancies: List[str]

class ClaimDecision(BaseModel):
    status: str
    reason: str

class ClaimResponse(BaseModel):
    documents: List[dict]
    validation: ValidationResult
    claim_decision: ClaimDecision
