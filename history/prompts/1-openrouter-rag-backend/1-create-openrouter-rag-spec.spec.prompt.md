---
id: 1
title: Create OpenRouter RAG Spec
stage: spec
date: 2025-12-17
surface: agent
model: claude-sonnet-4-5-20250929
feature: 1-openrouter-rag-backend
branch: 1-openrouter-rag-backend
user: Ayyan Ali Khan
command: /sp.specify
labels: ["specification", "openrouter", "rag", "docusaurus", "agents-sdk"]
links:
  spec: specs/1-openrouter-rag-backend/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-openrouter-rag-backend/spec.md
 - specs/1-openrouter-rag-backend/checklists/requirements.md
tests:
 - none
---

## Prompt

I want to build the RAG backend, but **strictly using OpenRouter** instead of OpenAI's direct API to utilize free/cheaper models.

**Research Step (Execute First):**
1.  **Docusaurus Analysis:** Use `ls -R book/` to understand my current content structure.
2.  **SDK Client Override:** Use Context7/Playwright to search the OpenAI Agents SDK documentation for:
    * `set_default_openai_client` or `ModelProvider`.
    * How to initialize the `Agent()` with a custom `base_url` (specifically "https://openrouter.ai/api/v1").
    * *Goal:* We must override the default OpenAI endpoint to point to OpenRouter.
3.  **Free Model Selection:** Use Playwright to browse `openrouter.ai/models` (or search) to find a **"Free"** or "High-Tier Free" model that supports **Tool Calling** (critical for RAG).
    * *Candidate to verify:* `google/gemini-2.0-flash-exp:free` or `liquid/lfm-40b`.
    * *Constraint:* The model MUST support "Tools" or "Function Calling" to query the vector database.

**Specification Requirements:**
-   **Ingestion Pipeline:** Define how we parse `.md` files from `book/docs`, split them, and store them in Qdrant.
-   **Agent Configuration:**
    * Specify the Python code to configure the Global Client using `base_url="https://openrouter.ai/api/v1"`.
    * Specify the exact Model ID (e.g., `google/gemini-2.0-flash-exp:free`) to be used in the `Agent(model=...)` definition.
-   **RAG Tool:** Define a function `query_qdrant(query: str)` that the Agent can call.
-   **API Layer:** FastAPI endpoints to serve the chat.
-   **Frontend:** Integration steps for the ChatKit widget in Docusaurus.

Create a robust PRD that proves you know how to route Agents SDK traffic through OpenRouter.

## Response snapshot

Completed specification for OpenRouter RAG Backend with proper research and configuration details.

## Outcome

- ✅ Impact: Created comprehensive specification for RAG backend using OpenRouter with free models
- 🧪 Tests: none
- 📁 Files: specs/1-openrouter-rag-backend/spec.md, specs/1-openrouter-rag-backend/checklists/requirements.md
- 🔁 Next prompts: /sp.plan to create implementation plan
- 🧠 Reflection: Successfully identified Google Gemini 2.0 Flash Experimental (free) model that supports tool calling and documented proper OpenAI Agents SDK configuration for OpenRouter.

## Evaluation notes (flywheel)

- Failure modes observed: Script .specify/scripts/bash/create-phr.sh not found, had to create PHR manually using template
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Ensure PHR creation script is available in expected location for future use