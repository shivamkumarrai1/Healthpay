from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_claim_no_files():
    response = client.post("/api/process-claim", files={})
    assert response.status_code == 422  # Missing required files

# Add this once you have sample files
# def test_process_claim_valid_files():
#     with open("tests/sample_bill.pdf", "rb") as f1, open("tests/sample_discharge.pdf", "rb") as f2:
#         response = client.post(
#             "/api/process-claim",
#             files=[("files", ("bill.pdf", f1, "application/pdf")),
#                    ("files", ("discharge.pdf", f2, "application/pdf"))]
#         )
#         assert response.status_code == 200
#         data = response.json()
#         assert "documents" in data
#         assert "claim_decision" in data
