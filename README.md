# Azure AI Agent Platform

This project is a backend AI service built with FastAPI and OpenAI.

## Features

- FastAPI backend
- AI-powered endpoint (/ask)
- Health check endpoint (/health)
- Docker-ready setup

## Use Case

This platform simulates an internal AI service where users can:

- Ask questions
- Get AI-generated answers
- Extend into agent-based systems in the future

## Tech Stack

- Python
- FastAPI
- OpenAI API
- Docker (setup ready)

## API Endpoints

### GET /
Basic status check

### GET /health
Health check endpoint

### POST /ask
Ask a question to the AI

#### Example request:

```json
{
  "question": "What is Azure?"
}

Run Locally

python -m uvicorn app.main:app --reload

Notes

Docker setup is included but not yet executed due to local environment setup
Future improvements:
	Azure deployment
	Multi-agent system
	RAG architecture


## Architecture Overview

This project simulates a simple AI platform with agent-based routing and retrieval.

### Components

- **API Layer (FastAPI)**  
  Handles incoming requests.

- **Agent Router**  
  Decides which agent should handle the request:
  - Weather agent
  - AI agent (OpenAI)

- **Retrieval System (RAG - simplified)**  
  Selects the most relevant knowledge section based on the user question.

---

## Retrieval Logic

The system uses a simple similarity scoring mechanism:

- Splits knowledge into sections
- Compares question words with each section
- Selects the best matching section

This simulates a basic vector search system.

---

## Example Response

```json
{
  "agent": "ai",
  "source": "FastAPI",
  "answer": "FastAPI is a modern Python web framework..."
}

Future Improvements
    Replace keyword scoring with embeddings
    Add vector database (e.g. Azure AI Search)
    Implement multi-agent orchestration
    Deploy to Azure Container Apps

## Example API Response

```json
{
  "agent": "ai",
  "source": "FastAPI",
  "score": 2,
  "answer": "FastAPI is a modern Python web framework...",
  "request_id": "123e4567-e89b-12d3-a456-426614174000"
}