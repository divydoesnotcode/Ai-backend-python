Here is a production-quality README.md you can directly copy into your GitHub repository.

⸻

AI Vendor Generation System (FastAPI + Ollama + PostgreSQL)

An AI-powered procurement vendor generation system that uses a local LLM (Ollama) to generate vendors when they are not found in the PostgreSQL database, and stores them for future use.

This system follows a Database-First, LLM-Fallback architecture to ensure efficiency, speed, and reduced LLM usage.

⸻

Features
	•	FastAPI backend
	•	Ollama LLM integration (ministral-3:8b)
	•	PostgreSQL database storage
	•	Database-first vendor search
	•	Automatic vendor generation using LLM
	•	Duplicate vendor prevention
	•	Structured JSON output
	•	Production-ready architecture

⸻

Architecture

User Request
    ↓
FastAPI Endpoint
    ↓
Check PostgreSQL Database
    ↓
Found → Return Vendors
Not Found → Call Ollama LLM
              ↓
         Generate Vendors
              ↓
         Store in PostgreSQL
              ↓
         Return Response


⸻

Tech Stack
	•	FastAPI
	•	Ollama (ministral-3:8b)
	•	PostgreSQL
	•	Python 3.10+
	•	psycopg2
	•	Pydantic

⸻

Project Structure

project/
│
├── main.py
├── ollama_service.py
├── vendor_repository.py
├── db.py
├── requirements.txt
└── README.md


⸻

Installation

1. Clone repository

git clone https://github.com/yourusername/ai-vendor-generation.git

cd ai-vendor-generation


⸻

2. Create virtual environment

python -m venv venv

source venv/bin/activate   # Mac/Linux

venv\Scripts\activate      # Windows


⸻

3. Install dependencies

pip install -r requirements.txt


⸻

Install and Run Ollama

Install Ollama:

brew install ollama  # Ollama Application for MAC is available and recommended

Start Ollama:

ollama serve

Pull model:

ollama pull ministral-3:8b

Verify:

ollama list


⸻

PostgreSQL Setup

Create database:

CREATE DATABASE ai_python;

Create table:

CREATE TABLE vendors (
    id SERIAL PRIMARY KEY,
    item_name TEXT NOT NULL,
    location TEXT NOT NULL,
    vendor_name TEXT NOT NULL,
    address TEXT,
    phone TEXT,
    email TEXT,
    website TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(item_name, location, vendor_name)
);


⸻

Configure Database Connection

Update db.py:

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="ai_python",
        user="postgres",
        password="your_password"
    )


⸻

Run FastAPI Server

uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000

Swagger Docs:

http://127.0.0.1:8000/docs


⸻

API Endpoint

Generate Vendors

POST

/vendors

Request:

{
  "item": "cement",
  "location": "Ahmedabad"
}

Response (Database):

{
  "source": "database",
  "count": 5,
  "vendors": [...]
}

Response (LLM):

{
  "source": "llm",
  "generated": 5,
  "saved": 5,
  "vendors": [...]
}


⸻

How It Works

Step 1: User sends request
Step 2: System checks PostgreSQL
Step 3: If vendors exist → return
Step 4: If not → use Ollama LLM
Step 5: Save vendors to database
Step 6: Return response

⸻

Duplicate Prevention

Duplicates are prevented using:
	•	Database UNIQUE constraint
	•	Data normalization
	•	Conflict handling

⸻

Requirements

requirements.txt

fastapi
uvicorn
psycopg2-binary
requests
pydantic


⸻

Future Improvements
	•	Vendor verification system
	•	Vendor ranking
	•	Confidence scoring
	•	Admin dashboard
	•	RAG integration
	•	Vector database support

⸻

Author

Divy Barot

⸻

License

MIT License

⸻
