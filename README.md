
# 📄 IntelliDocs AI

## AI-Powered Document Question Answering System using Retrieval-Augmented Generation (RAG)

**IntelliDocs AI** is an AI-powered document intelligence platform that enables users to upload PDF documents and interact with them using natural language. The system combines semantic search with Retrieval-Augmented Generation (RAG) to provide accurate, context-aware responses based only on the uploaded documents.

---

# 📌 Overview

Traditional document searching requires users to manually browse large PDFs to locate information.

IntelliDocs AI automatically extracts document content, generates semantic embeddings, performs vector similarity search using FAISS, and uses a locally hosted Large Language Model (LLM) through Ollama to answer user queries.

---

# ✨ Features

## Authentication

- User Registration
- Secure Login
- JWT Authentication
- Protected API Routes

## Document Management

- Upload PDF Documents
- View Uploaded Documents
- Delete Documents
- Secure User-Specific Storage

## AI Pipeline

- Automatic PDF Text Extraction
- Intelligent Text Chunking
- Sentence Transformer Embeddings
- Semantic Search using FAISS
- Local LLM Integration using Ollama (Qwen 2.5)
- Conversational Question Answering

---

# 🏗 System Architecture

```text
User
 │
 ▼
FastAPI REST API
 │
 ├── Authentication
 ├── Document Upload
 └── Chat
      │
      ▼
PDF Extraction
      │
      ▼
Text Chunking
      │
      ▼
Sentence Transformers
      │
      ▼
FAISS Vector Store
      │
      ▼
Semantic Retrieval
      │
      ▼
Ollama (Qwen 2.5)
      │
      ▼
AI Generated Answer
```

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Backend | FastAPI |
| Language | Python 3.13 |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT |
| Migrations | Alembic |
| PDF Processing | PyMuPDF |
| Embeddings | Sentence Transformers |
| Vector Search | FAISS |
| LLM | Ollama (Qwen 2.5) |

---

# 📂 Project Structure

```text
intellidocs-ai/
├── app/
│   ├── ai/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── dependencies/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── uploads/
│   ├── documents/
│   └── vectors/
├── alembic/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env.example
```

---

# ⚙️ Installation

```bash
git clone <https://github.com/DevanshMishra-codes/intellidocs-ai>
cd intellidocs-ai

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

alembic upgrade head

ollama pull qwen2.5:3b

uvicorn app.main:app --reload
```

Visit:

```
http://127.0.0.1:8000/docs
```

---

# 🚀 API Endpoints

## Authentication

- POST `/auth/register`
- POST `/auth/login`

## Users

- GET `/users/me`

## Documents

- POST `/documents/upload`
- GET `/documents`
- DELETE `/documents/{document_id}`

## Chat

- POST `/chat`

---

# 💬 Example Request

```json
{
  "question": "Summarize this document."
}
```

Example Response

```json
{
  "question": "Summarize this document.",
  "answer": "..."
}
```

---

# 🔒 Security

- JWT Authentication
- Password Hashing
- Protected Routes
- UUID File Names
- User-Specific Documents

---

# 📈 Future Improvements

- DOCX Support
- OCR Support
- Multi-document Chat
- Source Citations
- Cloud Deployment
- Conversation History

---

# 👨‍💻 Author

**Devansh Mishra**

- GitHub: https://github.com/DevanshMishra-codes
- LinkedIn: https://linkedin.com/in/devansh-mishra-codes
- Email: devanshmishra4028@gmail.com

---

⭐ If you found this project useful, consider giving it a star on GitHub.
