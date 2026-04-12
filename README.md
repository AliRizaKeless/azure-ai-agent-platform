\# Azure AI Agent Platform



This project is a backend AI service built with FastAPI and OpenAI.



\## Features



\- FastAPI backend

\- AI-powered endpoint (/ask)

\- Docker-ready setup



\## Tech Stack



\- Python

\- FastAPI

\- OpenAI API

\- Docker



\## Run locally



```bash

uvicorn app.main:app --reload

API Docs

http://127.0.0.1:8000/docs

## Endpoints

- `GET /` -> basic status
- `GET /health` -> health check
- `POST /ask` -> ask AI a question

## Example request

```json
{
  "question": "What is Azure?"
}

Notes
Docker files are included
Docker run is pending because local WSL/Docker setup is not ready yet
