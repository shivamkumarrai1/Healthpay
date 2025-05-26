from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_claim_no_files():
    response = client.post("/api/process-claim", files={})
    assert response.status_code == 422  # Missing required files

