🚀 AI Vendor Generation System

An AI-powered procurement vendor generation system using FastAPI, Ollama (LLM), and PostgreSQL.
The system first checks the database for vendors and uses the LLM only when vendors are not found, ensuring efficiency and performance.

⸻

📌 Features
	•	⚡ FastAPI backend
	•	🤖 Ollama LLM integration (ministral-3:8b)
	•	🗄️ PostgreSQL database storage
	•	🔍 Database-first search
	•	🧠 LLM fallback vendor generation
	•	🚫 Duplicate vendor prevention
	•	📄 Structured JSON output
	•	🏗️ Production-ready architecture

⸻

🧠 Architecture

flowchart TD
    A[User Request] --> B[FastAPI]
    B --> C{Check Database}
    C -->|Found| D[Return Vendors]
    C -->|Not Found| E[Call Ollama LLM]
    E --> F[Generate Vendors]
    F --> G[Store in PostgreSQL]
    G --> H[Return Response]


⸻

🛠️ Tech Stack

Technology	Purpose
FastAPI	Backend Framework
Ollama	Local LLM
ministral-3:8b	AI Model
PostgreSQL	Database
Python	Core Language
psycopg2	Database Driver


⸻

📁 Project Structure

ai-vendor-generation/
│
├── main.py
├── db.py
├── ollama_service.py
├── vendor_repository.py
├── requirements.txt
└── README.md


⸻

⚙️ Installation

1. Clone Repository

git clone https://github.com/yourusername/ai-vendor-generation.git
cd ai-vendor-generation


⸻

2. Create Virtual Environment

python -m venv venv

source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows


⸻

3. Install Dependencies

pip install -r requirements.txt


⸻

🤖 Setup Ollama

Start Ollama:

ollama serve

Pull model:

ollama pull ministral-3:8b

Verify:

ollama list


⸻

🗄️ PostgreSQL Setup

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

▶️ Run Server

uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs


⸻

📡 API Example

Request

POST /vendors

{
  "item": "cement",
  "location": "Ahmedabad"
}


⸻

Response (Database)

{
  "source": "database",
  "count": 5,
  "vendors": [...]
}


⸻

Response (LLM)

{
  "source": "llm",
  "generated": 5,
  "saved": 5,
  "vendors": [...]
}


⸻

🔄 Workflow

User → FastAPI → Database → LLM (if needed) → PostgreSQL → Response


⸻

🚫 Duplicate Prevention

Uses:
	•	PostgreSQL UNIQUE constraint
	•	Data normalization
	•	Conflict handling

⸻

👨‍💻 Author

Divy Barot
Final Year Project – AI Vendor Generation System

⸻

⭐ Future Improvements
	•	Vendor ranking
	•	Confidence scoring
	•	Vector database integration
	•	Admin dashboard
	•	Vendor verification system

⸻

Why this looks better on GitHub

This version uses:
	•	Proper headings
	•	Emojis for visual structure
	•	Tables
	•	Code blocks
	•	Mermaid diagram
	•	Clean spacing

⸻

If you want, I can create an even more impressive README with:
	•	GitHub badges
	•	Screenshots section
	•	API diagrams
	•	Professional open-source layout
