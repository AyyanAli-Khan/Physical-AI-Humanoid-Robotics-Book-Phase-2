# Feature Specification: OpenRouter RAG Backend

**Feature Branch**: `1-openrouter-rag-backend`
**Created**: 2025-12-17
**Status**: Draft
**Input**: User description: "I want to build the RAG backend, but **strictly using OpenRouter** instead of OpenAI's direct API to utilize free/cheaper models.

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
-   **Frontend:** Integration steps for the ChatKit widget in Docusaurus."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Docusaurus Content Search (Priority: P1)

A user visits the Docusaurus documentation site and wants to ask questions about the content using a chat interface. The user types their query into the chat widget and receives relevant answers based on the Docusaurus documentation content.

**Why this priority**: This is the core value proposition - enabling users to search and get answers from the documentation using natural language, which improves the user experience significantly.

**Independent Test**: The user can enter a question in the chat interface and receive an accurate response based on the documentation content, without needing to navigate through the traditional search or browse the documentation structure.

**Acceptance Scenarios**:

1. **Given** the user is on the Docusaurus site with the chat widget available, **When** the user enters a question related to the documentation content, **Then** the system returns accurate, contextually relevant answers from the documentation.
2. **Given** the user enters a query that matches documentation content, **When** the query is processed through the RAG system, **Then** the response includes citations or references to the specific documentation pages where the information was found.

---

### User Story 2 - RAG System Configuration (Priority: P2)

The system administrator needs to configure the RAG backend to use OpenRouter instead of OpenAI's direct API, ensuring that the system uses cost-effective models while maintaining performance.

**Why this priority**: Critical for cost control and operational efficiency - the system must be configured to use OpenRouter's free/cheaper models as specified.

**Independent Test**: The system can be configured to route all LLM requests through OpenRouter API with the specified base URL and model, without requiring changes to the core application logic.

**Acceptance Scenarios**:

1. **Given** the RAG backend is configured with OpenRouter settings, **When** a query is processed, **Then** all LLM requests are routed through the OpenRouter API endpoint.
2. **Given** the system is configured with the free model ID, **When** a query is processed, **Then** the specified free model is used for inference.

---

### User Story 3 - Documentation Content Ingestion (Priority: P3)

The system needs to automatically ingest and index the Docusaurus documentation content into the Qdrant vector database to enable RAG functionality.

**Why this priority**: Essential for the RAG system to have access to the documentation content - without proper ingestion, the chat functionality cannot provide relevant answers.

**Independent Test**: The system can parse Docusaurus documentation files, convert them to vector embeddings, and store them in Qdrant, making them available for semantic search.

**Acceptance Scenarios**:

1. **Given** new documentation content is added to the Docusaurus site, **When** the ingestion process runs, **Then** the new content becomes available for semantic search in the RAG system.
2. **Given** documentation content exists in the Docusaurus site, **When** the ingestion process runs, **Then** the content is properly chunked, embedded, and stored in Qdrant.

---

### Edge Cases

- What happens when the OpenRouter API is temporarily unavailable?
- How does the system handle queries that don't match any documentation content?
- What happens when the free model quota is exceeded?
- How does the system handle very large documentation files during ingestion?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST route all LLM requests through OpenRouter API endpoint at "https://openrouter.ai/api/v1"
- **FR-002**: System MUST use the Google Gemini 2.0 Flash Experimental (free) model (`google/gemini-2.0-flash-exp:free`) for cost-effective inference
- **FR-003**: System MUST provide a `query_qdrant(query: str)` function that the Agent can call to retrieve relevant documentation content
- **FR-004**: System MUST ingest Docusaurus `.md` files from `book/docs` directory and store them in Qdrant vector database
- **FR-005**: System MUST expose FastAPI endpoints to serve the chat interface
- **FR-006**: System MUST integrate with Docusaurus to provide ChatKit widget in the frontend
- **FR-007**: System MUST chunk documentation content into appropriate sizes for embedding and retrieval
- **FR-008**: System MUST provide proper error handling when OpenRouter API is unavailable
- **FR-009**: System MUST return citations/references to original documentation pages in chat responses

### Key Entities

- **Documentation Chunk**: Represents a segment of documentation content that has been processed and vectorized for storage in Qdrant; includes content, metadata, and source reference
- **Qdrant Vector Store**: Container for storing vector embeddings of documentation chunks with associated metadata for efficient similarity search
- **Chat Session**: Represents a conversation context between user and the RAG agent, maintaining conversation history and context

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can ask questions about documentation content and receive relevant answers within 5 seconds response time
- **SC-002**: System successfully routes 100% of LLM requests through OpenRouter API instead of direct OpenAI API
- **SC-003**: At least 90% of documentation content from `book/docs` is successfully ingested into Qdrant vector database
- **SC-004**: Documentation search accuracy is at least 85% based on relevance of returned results to user queries
- **SC-005**: System operates within free tier usage limits of OpenRouter for at least 95% of the time