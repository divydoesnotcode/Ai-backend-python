# AI Vendor Generation System

An AI-powered procurement vendor generation system built using FastAPI, Ollama, and PostgreSQL.

The system follows a database-first approach. It checks the database for vendors and uses the LLM only if vendors are not found.

---

## Features

- FastAPI backend
- Ollama LLM integration (ministral-3:8b)
- PostgreSQL database storage
- Database-first search logic
- Automatic vendor generation using LLM
- Duplicate prevention using database constraints
- Structured JSON responses

---

## Architecture

User Request  
↓  
FastAPI  
↓  
Check PostgreSQL  
↓  
If Found → Return Vendors  
If Not Found → Call Ollama  
↓  
Generate Vendors  
↓  
Store in PostgreSQL  
↓  
Return Response  

---

## Tech Stack

- Python
- FastAPI
- Ollama
- ministral-3:8b
- PostgreSQL
- psycopg2

---

## Project Structure

```
ai-vendor-generation/
│
├── main.py
├── db.py
├── ollama_service.py
├── vendor_repository.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone repository

```
git clone https://github.com/yourusername/ai-vendor-generation.git
cd ai-vendor-generation
```

### 2. Create virtual environment

Mac/Linux:

```
python -m venv venv
source venv/bin/activate
```

Windows:

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Setup Ollama

Start Ollama:

```
ollama serve
```

Pull model:

```
ollama pull ministral-3:8b
```

Check installed models:

```
ollama list
```

---

## PostgreSQL Setup

Create database:

```
CREATE DATABASE ai_python;
```

Create table:

```
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
```

---

## Configure Database

Update db.py:

```
host="localhost"
database="ai_python"
user="postgres"
password="your_password"
```

---

## Run FastAPI Server

```
uvicorn main:app --reload
```

Open browser:

```
http://127.0.0.1:8000/docs
```

---

## API Example

Endpoint:

```
POST /vendors
```

Request:

```
{
  "item": "cement",
  "location": "Ahmedabad"
}
```

Response:

```
{
  "source": "database",
  "count": 5,
  "vendors": [...]
}
```

OR

```
{
  "source": "llm",
  "generated": 5,
  "saved": 5,
  "vendors": [...]
}
```

---

## Workflow

1. User sends request
2. System checks PostgreSQL
3. If vendors found → return
4. If not found → use Ollama
5. Save vendors to database
6. Return response

---

## Requirements

```
fastapi
uvicorn
psycopg2-binary
requests
pydantic
```

---

## Author

Divy Barot

Final Year Project  
AI Vendor Generation System

---

## License

MIT License
