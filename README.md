# RAG with Ollama + FastAPI + ChromaDB

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using:

- **Ollama** – local LLM inference
- **FastAPI** – backend API
- **ChromaDB** – vector database for embeddings

The system is designed to work with **any document**, although it was primarily built for a specific use case.

---

# Installation

## 1. Install Python Dependencies

Install the required packages using **uv** or **pip**.

### Using uv (recommended)

```bash
uv pip install -r requirements.txt
