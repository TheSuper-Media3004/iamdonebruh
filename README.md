# RAG with Ollama + FastAPI + ChromaDB

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using:

- **Ollama** – local LLM inference
- **FastAPI** – backend API
- **ChromaDB** – vector database for embeddings

The system is designed to work with **any document**, although it was primarily built for a specific use case.

# Insert your document
========
1.app
  -rag.py
  -main.py
2.data
  i.docs <---- here

---
# Cloning

### Clone
========
```bash
git clone <placeholder for the git repo https or ssh>
```
---
# Installation

## 1. Install Python Dependencies inside your virtual environment

Install the required packages using **uv** or **pip**.

### Using uv (thats what i did)

```bash
uv add -r requirements.txt
```

#### or

```bash
uv pip install -r requirements.txt
```
---
### 2. Install Ollama in WSL or in windows(1143 port)

***Install [Ollama](https://ollama.com/download/linux)***

```bash
ollama pull mistral
```
and them

```bash
ollama serve
```
---
## Execution

### 1. Make a /chroma_db directory to store your vector embeddings

```bash
mkdir chroma_db
```

### 2. Run the ingestion pipeline

```bash
python ingestion.py
```

### 3. Set ur base url inside the .env file

```bash
touch .env
vi .env
```

```vi
BASE_URL = <your local host at port 1143 "127.0.0.0"--->example>
```

### 4. Run the api

```bash
fastapi dev app/main.py
```

---

### 5. Implementaion

go to

```
http://127.0.0.1/docs
```

#Test it in the swagger


