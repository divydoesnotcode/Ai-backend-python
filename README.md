# 🤖 AI Vendor Generation System

An AI-powered procurement vendor generation system built using **FastAPI ⚡, Ollama 🧠, and PostgreSQL 🗄️**.

This system follows a **Database-First, LLM-Fallback architecture** to ensure fast response, reduced LLM usage, and efficient vendor storage.

---

## ✨ Features

- ⚡ FastAPI high-performance backend  
- 🧠 Ollama LLM integration (ministral-3:8b)  
- 🗄️ PostgreSQL vendor database  
- 🔍 Database-first vendor search  
- 🤖 Automatic vendor generation using AI  
- 🚫 Duplicate vendor prevention  
- 📦 Structured JSON output  
- 🏗️ Production-ready architecture  

---

## 🧠 System Architecture

```
👤 User Request
     ↓
⚡ FastAPI Server
     ↓
🗄️ PostgreSQL Database
     ↓
✅ Vendors Found → Return Result
❌ Vendors Not Found → 🧠 Ollama LLM
                          ↓
                    🤖 Generate Vendors
                          ↓
                    💾 Save to Database
                          ↓
                    📤 Return Response
```

---

## 🛠️ Tech Stack

| Technology | Icon | Purpose |
|----------|------|---------|
| Python | 🐍 | Core programming language |
| FastAPI | ⚡ | Backend framework |
| Ollama | 🧠 | LLM runtime |
| ministral-3:8b | 🤖 | AI model |
| PostgreSQL | 🗄️ | Database |
| psycopg2 | 🔌 | Database connector |
| JSON | 📦 | Data format |

---

## 📁 Project Structure

```
📦 ai-vendor-generation
│
├── 📝 README.md            # Documentation
├── 🐍 database.py         
├── 🐍 db.py
├── 🐍 main.py
├── 🐍 models.py
├── 🐍 ollama_service.py
├── 📄 requirements.txt
├── 🐍 schemas.py
└── 🐍 vendor_repo.py     
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```
git clone https://github.com/yourusername/ai-vendor-generation.git
cd ai-vendor-generation
```

---

### 2️⃣ Create Virtual Environment

Mac/Linux 🍎🐧

```
python -m venv venv
source venv/bin/activate
```

Windows 🪟

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies 📦

```
pip install -r requirements.txt
```

---

## 🧠 Setup Ollama

Start Ollama server:

```
ollama serve
```

Pull AI model:

```
ollama pull ministral-3:8b
```

Verify installation:

```
ollama list
```

---

## 🗄️ PostgreSQL Setup

Create database:

```
CREATE DATABASE ai_python;
```

Create vendors table:

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

## ▶️ Run FastAPI Server

```
uvicorn main:app --reload
```

Server URL 🌐

```
http://127.0.0.1:8000
```

Swagger Docs 📄

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Example

### 📥 Request

```
POST /vendors
```

```
{
  "item": "cement",
  "location": "Ahmedabad"
}
```

---

### 📤 Response (Database)

```
{
  "source": "database",
  "count": 5,
  "vendors": [...]
}
```

---

### 📤 Response (LLM)

```
{
  "source": "llm",
  "generated": 5,
  "saved": 5,
  "vendors": [...]
}
```

---

## 🔄 Workflow

```
👤 User Request
   ↓
⚡ FastAPI
   ↓
🗄️ PostgreSQL Check
   ↓
❌ Not Found → 🧠 Ollama
   ↓
💾 Save Vendors
   ↓
📤 Return Response
```

---

## 🚫 Duplicate Prevention

Uses multiple safety layers:

- 🧠 Data normalization
- 🗄️ PostgreSQL UNIQUE constraint
- ⚡ Conflict handling logic

---

## 🎯 Use Cases

- 🏭 Procurement automation  
- 🏢 Vendor discovery systems  
- 🤖 AI supply chain tools  
- 📊 Vendor intelligence platforms  

---

## 👨‍💻 Author

**Divy Barot**  
---

## 🚀 Future Improvements

- 📊 Vendor ranking system  
- 🧠 Confidence scoring  
- 🔎 Vendor verification  
- 🌐 Admin dashboard  
- 📦 Vector database integration  

---

## 📜 License

MIT License 📄
