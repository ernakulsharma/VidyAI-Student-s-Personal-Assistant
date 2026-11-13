# VidyAI — AI-Powered Academic Intelligence & Multi-Source RAG Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-FF6F00?style=for-the-badge)](https://www.trychroma.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama_(Gemma)-000000?style=for-the-badge)](https://ollama.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

> **VidyAI** is a local-first, privacy-preserving academic assistant engineered to transform fragmented lecture notes, textbooks, and research papers into an interactive, citation-grounded knowledge base using **Document Intelligence (Docling)**, **BGE-M3 dense retrieval**, and **local Gemma inference**.

---

## 1. Project Overview & Problem Statement

### The Challenge
University students and researchers routinely navigate dozens of unstructured PDFs, slide decks, and study notes per course. Existing study workflows suffer from three critical bottlenecks:
1. **Information Fragmentation:** Synthesizing concepts across multiple syllabus documents requires hours of manual cross-referencing.
2. **Layout Loss in Standard Parsers:** Naive text extractors corrupt multi-column academic papers, structured tables, and hierarchical headings, degrading downstream retrieval accuracy.
3. **Cloud Cost & Privacy Trade-offs:** Relying on proprietary cloud LLM APIs incurs recurring token costs and exposes proprietary academic materials to external servers.

### The Solution
**VidyAI** resolves these challenges through a modular, end-to-end Retrieval-Augmented Generation (RAG) backend built with **FastAPI**. By combining layout-aware document parsing (**Docling**), semantic chunking with relational metadata (**PostgreSQL** + **ChromaDB**), and local open-weights inference (**Ollama + Gemma**), VidyAI delivers zero-cost, hallucination-resistant academic assistance.

---

## 2. Core Capabilities

* **Layout-Aware Document Intelligence:** Ingests complex PDFs, DOCX files, and lecture slides via **Docling**, preserving document hierarchy, tables, and structural boundaries prior to chunking.
* **High-Precision Semantic Retrieval:** Embeds semantic chunks using **BAAI/bge-m3** and indexes vectors in **ChromaDB**, paired with **PostgreSQL** metadata filtering for targeted document- or course-level scoping.
* **Grounded Contextual Q&A:** Answers syllabus and technical questions strictly anchored to retrieved source passages, returning verifiable document and section citations.
* **Automated Study Briefs & Summarization:** Distills lengthy chapters and multi-document modules into structured, exam-ready concept summaries.
* **Active-Recall Quiz Generation:** Automatically synthesizes multiple-choice and conceptual assessment questions calibrated to uploaded course material.

---

## 3. System Architecture

```mermaid
flowchart LR
    A[Academic Documents<br/>PDF / DOCX / Slides] --> B[Document Intelligence Engine<br/>Docling Parser]
    B --> C[Semantic Chunker &<br/>Metadata Extractor]
    C --> D[(PostgreSQL<br/>Document & Chunk Metadata)]
    C --> E[BGE-M3 Embedding Model]
    E --> F[(ChromaDB<br/>Vector Store)]

    G[Student Query /<br/>Task Request] --> H[FastAPI Orchestrator]
    H --> E
    F <-->|Top-K Semantic Retrieval| H
    D <-->|Metadata Filtering| H
    H --> I[Ollama Local Runtime<br/>Gemma LLM]
    I --> J[Grounded Q&A /<br/>Summaries / Quizzes]
```

### Architectural Breakdown

| Layer | Component | Responsibility |
| :--- | :--- | :--- |
| **Ingestion & Parsing** | `Docling` | Extracts clean Markdown/structured representations from multi-column PDFs, tables, and slide decks. |
| **Chunking & Metadata** | Custom Semantic Splitter + `PostgreSQL` | Splits documents along structural boundaries and tracks document IDs, course tags, and source offsets. |
| **Embedding & Indexing** | `BGE-M3` + `ChromaDB` | Generates dense semantic embeddings and performs low-latency similarity search across knowledge bases. |
| **Inference & Workflows** | `Ollama (Gemma)` | Executes local prompt pipelines for citation-backed Q&A, structured summarization, and quiz synthesis. |
| **API Gateway** | `FastAPI` | Exposes asynchronous REST endpoints with Pydantic schema validation and interactive OpenAPI docs. |

---

## 4. Repository Structure

```text
VidyAI-Student-s-Personal-Assistant/
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── ingest.py          # Document upload & background parsing endpoints
│   │       ├── qa.py              # Grounded RAG Q&A endpoints
│   │       └── study_tools.py     # Summarization & quiz generation workflows
│   ├── core/
│   │   ├── config.py              # Environment & model configuration
│   │   └── database.py            # PostgreSQL session & connection management
│   ├── ingestion/
│   │   ├── parser.py              # Docling layout-aware extraction pipeline
│   │   └── chunker.py             # Semantic chunking & metadata enrichment
│   ├── rag/
│   │   ├── embedder.py            # BGE-M3 embedding wrapper
│   │   ├── vector_store.py        # ChromaDB collection & retrieval logic
│   │   └── generator.py           # Ollama (Gemma) prompt orchestration
│   ├── models/
│   │   └── schemas.py             # SQLAlchemy & Pydantic data models
│   └── main.py                    # FastAPI application entrypoint
├── .env.example                   # Environment variable template
├── requirements.txt               # Python dependencies
└── README.md
```

---

## 5. Setup & Local Installation Guide

### Prerequisites
* **Python** 3.10 or higher
* **PostgreSQL** 15+ running locally or via Docker
* **Ollama** installed locally ([Download Ollama](https://ollama.com/))

### Step 1: Clone the Repository
```bash
git clone [https://github.com/ernakulsharma/VidyAI-Student-s-Personal-Assistant.git](https://github.com/ernakulsharma/VidyAI-Student-s-Personal-Assistant.git)
cd VidyAI-Student-s-Personal-Assistant
```

### Step 2: Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Pull the Local Gemma Model via Ollama
```bash
ollama pull gemma2
```

### Step 4: Configure Environment Variables
Copy the example environment file and update your database and model settings:
```bash
cp .env.example .env
```

```env
# PostgreSQL Configuration
DATABASE_URL=postgresql://postgres:password@localhost:5432/vidyai_db

# Vector Store & Embeddings
CHROMA_PERSIST_DIR=./data/chroma_db
EMBEDDING_MODEL=BAAI/bge-m3

# Ollama Inference Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma2
```

### Step 5: Launch the Application
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
Once running, access the interactive Swagger API documentation at **`http://localhost:8000/docs`**.

---

## 6. Core API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/v1/ingest/upload` | Parses an uploaded document via Docling, chunks text, stores metadata in PostgreSQL, and indexes vectors in ChromaDB. |
| `POST` | `/api/v1/qa/ask` | Retrieves top-K relevant chunks and generates a citation-backed answer using Gemma. |
| `POST` | `/api/v1/study/summarize` | Generates a structured hierarchical summary for a specified document or topic. |
| `POST` | `/api/v1/study/quiz` | Produces an auto-graded MCQ and short-answer quiz from indexed course content. |

---

## 7. Future Roadmap

 **Hybrid Sparse-Dense Retrieval:** Combine BGE-M3 dense vectors with BM25 lexical scoring for exact formula and acronym matching.
 **Spaced-Repetition Export:** Direct `.apkg` (Anki) flashcard deck export from auto-generated quizzes.
 **Docker Compose Stack:** Single-command orchestration bundling FastAPI, PostgreSQL, and Ollama.

---

## 8. Author

**Nakul Sharma**  
B.E. in Computer Science & Business Systems — Thapar Institute of Engineering and Technology  
GitHub: [@ernakulsharma](https://github.com/ernakulsharma)
