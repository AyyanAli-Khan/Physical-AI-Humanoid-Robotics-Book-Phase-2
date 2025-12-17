# Implementation Plan: OpenRouter RAG Backend

**Branch**: `1-openrouter-rag-backend` | **Date**: 2025-12-17 | **Spec**: [specs/1-openrouter-rag-backend/spec.md](specs/1-openrouter-rag-backend/spec.md)
**Input**: Feature specification from `/specs/1-openrouter-rag-backend/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a RAG backend that uses OpenRouter instead of OpenAI's direct API to utilize free/cheaper models. The system will ingest Docusaurus documentation content into Qdrant vector database and serve a chatbot using the OpenAI Agents SDK with OpenRouter integration. The frontend will integrate with the existing Docusaurus site using ChatKit.

## Technical Context

**Language/Version**: Python 3.11, TypeScript/JavaScript for frontend
**Primary Dependencies**: FastAPI, OpenAI Agents SDK, Qdrant Client, OpenRouter API, uvicorn, python-dotenv
**Storage**: Qdrant Vector Database (local Docker container)
**Testing**: pytest for backend, manual testing for integration
**Target Platform**: Linux server, cross-platform compatibility
**Project Type**: Web application (backend service with API endpoints)
**Performance Goals**: <5s response time for queries, handle multiple concurrent users
**Constraints**: <5s p95 latency for chat responses, must use OpenRouter API with free model
**Scale/Scope**: Single instance, up to 100 concurrent users initially

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

All code must comply with Research Before Output protocol; All external APIs must be validated using documentation tools before implementation; All integrations must pass end-to-end testing before approval; Project must maintain proper separation between frontend and backend

## Project Structure

### Documentation (this feature)

```text
specs/1-openrouter-rag-backend/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── app/
│   ├── __init__.py
│   ├── agent.py          # OpenAI Agent with OpenRouter integration
│   └── main.py           # FastAPI app entry point
├── ingestion/
│   ├── __init__.py
│   ├── ingest.py         # Docusaurus content ingestion script
│   └── chunker.py        # Text chunking logic
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── docker-compose.yml    # Qdrant service
└── tests/
    ├── __init__.py
    ├── unit/
    └── integration/
```

**Structure Decision**: Backend service with API endpoints to serve chat functionality, separate ingestion script for processing Docusaurus content, and Docker Compose for Qdrant vector database.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [None] | [N/A] | [N/A] |