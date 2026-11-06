# VidyAI — Academic Assistant MVP

VidyAI is an academic assistant that lets students upload study PDFs, ask questions about their material, and receive answers with source references.

## MVP scope

- Upload PDF study material (up to 25 MB per file).
- Parse and index documents with the existing Docling, BGE-M3, and ChromaDB pipeline.
- Ask questions against the indexed material using retrieval-augmented generation (RAG) and Ollama.
- Show the source document and section used for each answer.

The first iteration is intentionally focused on document-grounded chat. Authentication, conversation persistence, workspace isolation, and richer library management are not part of this MVP slice yet.

## Project structure

- `backend/` — FastAPI API, document ingestion, embeddings, ChromaDB retrieval, and Ollama generation.
- `frontend/` — Next.js application. The academic chat workspace is available at `/chat`.

## Run locally

### 1. Backend

From the `backend` directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create `.env` in `backend/` with the values required by `app/core/settings.py`:

```dotenv
APP_NAME=VidyAI
APP_VERSION=1.0.0
DEBUG=true
STORAGE_PATH=./storage
DOCUMENTS_PATH=./storage/documents
CHROMA_PATH=./storage/chroma
EMBEDDING_MODEL=BAAI/bge-m3
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2
TOP_K=5
DATABASE_URL=sqlite:///./vidyai.db
```

Make sure Ollama is running and that the model configured by `OLLAMA_MODEL` is available locally. Start the API:

```powershell
uvicorn app.main:app --reload
```

The API is served at `http://localhost:8000`; interactive API documentation is at `http://localhost:8000/docs`.

> The database URL above is a local-development example. Use the database configuration supported by your environment and existing migrations.

### 2. Frontend

From the `frontend` directory:

```powershell
npm install
Copy-Item .env.example .env.local
npm run dev
```

Open [http://localhost:3000/chat](http://localhost:3000/chat). Set `NEXT_PUBLIC_API_URL` in `.env.local` if the backend is not running at `http://localhost:8000`.

## API endpoints used by the workspace

- `POST /documents/upload` — accepts a PDF as multipart form data under the `file` field.
- `POST /rag/query` — accepts JSON `{"query":"..." }` and returns `answer` plus `sources`.

## Current MVP limitations

- The current RAG index is shared; per-user and per-workspace retrieval filters need to be added before multi-user deployment.
- Chat history is held in the browser session and is not persisted.
- Document upload runs the ingestion pipeline synchronously; large documents may take time to process.
- Configure the allowed frontend origin in `backend/app/main.py` before deploying the frontend to another origin.
- Review authentication, upload quotas, retention, and production database configuration before public deployment.
