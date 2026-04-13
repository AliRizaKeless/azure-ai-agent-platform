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

