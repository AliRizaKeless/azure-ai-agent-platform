# Azure AI Agent Platform

This project is a backend AI service built with FastAPI and OpenAI.

## Status

- Active Development
- FastAPI Backend
- AI + Agent + RAG Prototype

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

## Roadmap

- Azure deployment
- Terraform setup
- Vector database
- Frontend UI

## Quick Start

```bash
python -m uvicorn app.main:app --reload

Open:

/docs
/health
/metrics
/ping
/metrics
/info

## Running with Docker

Build the Docker image:

```bash
docker build -t azure-ai-agent-platform .
```

Run the container:

```bash
docker run --env-file .env -p 8000:8000 azure-ai-agent-platform
```
### Container Health Monitoring

The Docker image includes a built-in health check that validates the `/health` endpoint.

This helps ensure that the application is running correctly inside the container.

Available endpoints:

* http://localhost:8000/docs
* http://localhost:8000/health
* http://localhost:8000/metrics
* http://localhost:8000/version
* http://localhost:8000/uptime

## API Metadata

| Property | Value |
|----------|--------|
| Framework | FastAPI |
| AI Model | GPT-4o-mini |
| Containerized | Yes |
| Docker Support | Yes |
| RAG Support | Yes |

## Azure Deployment Preparation

A resource group has been created in Azure as the foundation for deployment.

| Resource | Value |
|----------|-------|
| Resource Group | rg-ai-agent-platform |
| Region | Norway East |
| Status | Created |

Next steps:

- Create Azure Container Registry
- Push Docker image to registry
- Deploy container to Azure Container Apps

## Cloud Infrastructure Status

### Azure

- Azure CLI configured
- Azure subscription connected
- Resource Group created
- Container deployment planned

Current target platform:

- Azure Container Apps

## Azure Resources

### Resource Group
- rg-ai-agent-platform

### Azure Container Registry
- acraliagentplatform.azurecr.io

Deployment target:
- Azure Container Apps

### Container Image

The Docker image has been pushed to Azure Container Registry:

```text
acraliagentplatform.azurecr.io/azure-ai-agent-platform:v1

### Azure Container Apps Environment

- Name: env-ai-agent-platform
- Region: Norway East
- Workload profile: Consumption
- Status: Created

### Runtime Configuration

The deployed Azure Container App uses environment variables for runtime configuration.

- `OPENAI_API_KEY` is configured as an Azure Container App environment variable.
- Secrets are not stored in the repository.
