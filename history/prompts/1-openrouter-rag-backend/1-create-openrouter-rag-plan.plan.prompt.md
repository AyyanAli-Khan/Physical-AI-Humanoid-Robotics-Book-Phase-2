---
id: 1
title: Create OpenRouter RAG Plan
stage: plan
date: 2025-12-17
surface: agent
model: claude-sonnet-4-5-20250929
feature: 1-openrouter-rag-backend
branch: 1-openrouter-rag-backend
user: Ayyan Ali Khan
command: /sp.plan
labels: ["plan", "openrouter", "rag", "qdrant", "fastapi", "agents-sdk"]
links:
  spec: specs/1-openrouter-rag-backend/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-openrouter-rag-backend/plan.md
 - specs/1-openrouter-rag-backend/research.md
 - specs/1-openrouter-rag-backend/data-model.md
 - specs/1-openrouter-rag-backend/contracts/api-contract.yaml
 - specs/1-openrouter-rag-backend/quickstart.md
tests:
 - none
---

## Prompt

/sp.plan

Based on the Specification (including the OpenRouter requirement), create a robust, step-by-step implementation plan.

**Crucial Architecture Verification (MANDATORY PRE-PLAN STEP):**
Before generating the plan steps below, you MUST perform these research tasks:
1.  **OpenAI Agents SDK Imports:** Use `context7` to find the *exact* and latest Python import statements and object initialization patterns for the Agents SDK.
2.  **Qdrant Client Setup:** Use `context7` to find the current Python client connection syntax for Qdrant (e.g., initialization, creating a collection, and the preferred method for bulk point insertion/upsert).
3.  **FastAPI Agent Integration:** Use `context7` to find the standard pattern for integrating a long-running Agent/Chat session inside a FastAPI endpoint (e.g., handling asynchronous processing and session state).

**Plan Structure (Incorporating Research and OpenRouter):**

1.  **Environment Setup (backend/):**
    * Create `backend/` directory.
    * Create `requirements.txt` listing all necessary packages (FastAPI, uvicorn, qdrant-client, openai-agents-sdk, etc.)
    * Setup `.env` file for `OPENROUTER_API_KEY`, `QDRANT_URL`, etc.

2.  **Qdrant Service Setup:**
    * Define a Docker Compose file (`docker-compose.yml`) to spin up the Qdrant service locally.
    * **MCP Check:** Use `Playwright` to find a simple, up-to-date Qdrant Docker Compose example.

3.  **Data Ingestion Script (`ingestion/ingest.py`):**
    * Develop a Python script to iterate through the Docusaurus content (`book/docs/*.md`).
    * **Text Processing:** Implement a method (e.g., using LlamaIndex/LangChain if needed, or simple custom logic) to load, chunk, and embed the text.
    * **Qdrant Write:** Implement the logic to connect to Qdrant and upsert the chunks, ensuring correct metadata is stored to link chunks back to their source document URL.

4.  **Agent Logic Development (`app/agent.py`):**
    * **OpenRouter Client Setup:** Implement the code to override the default OpenAI client with the OpenRouter `base_url` and use the selected free model.
    * **Qdrant Tool:** Define the `query_qdrant` function that serves as the Agent's tool.
    * **Agent Initialization:** Instantiate the `Agent()` with the tool and the OpenRouter model.

5.  **Runtime Serving (FastAPI):**
    * Develop the main `backend/main.py` FastAPI app.
    * Implement **CORS support** (critical for Docusaurus frontend connection).
    * Implement necessary endpoints for the ChatKit integration (e.g., `/chat/session`, `/chat/message`).
    * **MCP Check:** Use `context7` to verify the necessary JSON payload structure expected by ChatKit for the response.

6.  **Docusaurus UI Integration:**
    * Identify the exact Docusaurus file to `swizzle` or edit (e.g., `Root.js` or `Layout.js`).
    * Add the ChatKit client script tag, pointing it to the new FastAPI backend URL.

Ensure the plan separates "Data Ingestion" (steps 2-3) from "Runtime Serving" (steps 4-5) for clear deployment.

## Response snapshot

Completed implementation plan for OpenRouter RAG Backend with comprehensive research, data models, API contracts, and quickstart guide.

## Outcome

- ✅ Impact: Created complete implementation plan with research on OpenAI Agents SDK, Qdrant client, and FastAPI integration for OpenRouter-based RAG system
- 🧪 Tests: none
- 📁 Files: specs/1-openrouter-rag-backend/plan.md, specs/1-openrouter-rag-backend/research.md, specs/1-openrouter-rag-backend/data-model.md, specs/1-openrouter-rag-backend/contracts/api-contract.yaml, specs/1-openrouter-rag-backend/quickstart.md
- 🔁 Next prompts: /sp.tasks to create implementation tasks
- 🧠 Reflection: Successfully integrated research findings to create a comprehensive plan for RAG backend using OpenRouter with proper architecture for documentation ingestion and chat interface.

## Evaluation notes (flywheel)

- Failure modes observed: Script .specify/scripts/bash/create-phr.sh not found, had to create PHR manually using template
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Ensure PHR creation script is available in expected location for future use