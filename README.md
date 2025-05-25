# 🏥 HealthPay Claim Document Processor

A FastAPI-based backend pipeline that processes medical claim PDFs using LLMs and agentic workflows.

## 🔧 Architecture

- **FastAPI**: Main API server
- **Agent Modules**:
  - `ClassifierAgent`: Classifies PDFs as bill, discharge_summary, or ID
  - `BillAgent`: Extracts bill-related fields via LLM
  - `DischargeAgent`: Extracts discharge summary details
  - `ValidationAgent`: Validates structure and checks for missing/inconsistent data
- **PDF Parser**: PyMuPDF used to extract text from uploads
- **LLM**: OpenRouter + GPT 3.5 Turbo (or Gemini)

## 🔁 Flow

1. Upload multiple PDFs to `/process-claim`
2. Each is classified using LLM
3. Text is routed to bill/discharge agents
4. Extracted JSON is validated
5. Final claim decision is returned

## 🤖 AI Tools Used

- **OpenRouter**: for LLM access
- **ChatGPT**: for agent prompting & architecture design
- **Cursor**: for fast in-editor prompting and test generation

### Prompt Examples:

#### Classifier Agent

Classify the following text as one of: bill, discharge_summary, id_card. Return only the label.

### Bill Agent

--Extract the following from the hospital bill: hospital_name, total_amount, date_of_service. Return as JSON.

### Discharge Agent

--Extract patient_name, diagnosis, admission_date, discharge_date. Return as a JSON object.

🧪 Testing
Upload sample PDFs via Swagger (/docs)

See JSON output with validation and claim status

📁 Project Structure

healthpay-backend/
│
├── app/                       # Main application code
│   ├── main.py                # FastAPI app instance
│   ├── api.py                 # Route for /process-claim
│   │
│   ├── agents/                # LLM-powered agents
│   │   ├── base_agent.py
│   │   ├── classifier_agent.py
│   │   ├── bill_agent.py
│   │   ├── discharge_agent.py
│   │   └── validation_agent.py
│   │
│   ├── services/              # Supporting services
│   │   ├── pdf_service.py     # PDF text extraction
│   │   └── llm_service.py     # OpenRouter API wrapper
│   │
│   ├── models/                # (Optional) Pydantic models
│   │   └── schema.py
│
├── tests/                     # Test cases
│   └── test_processor.py
│
├── .env.example               # Sample environment file (no secrets)
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker container configuration
├── README.md                  # Project documentation
└── .dockerignore              # Files to exclude from Docker image
