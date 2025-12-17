---
description: "Task list for OpenRouter RAG Backend implementation"
---

# Tasks: OpenRouter RAG Backend

**Input**: Design documents from `/specs/1-openrouter-rag-backend/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create backend directory structure per implementation plan
- [X ] T002 [P] Create requirements.txt with FastAPI, uvicorn, qdrant-client, openai-agents  , python-dotenv dependencies
- [X] T003 Create .env file template with OPENROUTER_API_KEY placeholder
- [X] T004 Create docker-compose.yml for Qdrant service

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T005 Set up Qdrant client connection in backend/qdrant_client.py
- [X] T006 [P] Configure environment variables loading with python-dotenv
- [X] T007 Set up OpenRouter client configuration using set_default_openai_client
- [X] T008 Create Documentation Chunk model based on data-model.md
- [X] T009 Create Chat Session model based on data-model.md
- [X] T010 Configure CORS middleware for FastAPI app
- [X] T011 Set up basic FastAPI application structure

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Docusaurus Content Search (Priority: P1) 🎯 MVP

**Goal**: Enable users to ask questions about documentation content and receive relevant answers through a chat interface

**Independent Test**: The user can enter a question in the chat interface and receive an accurate response based on the documentation content, without needing to navigate through the traditional search or browse the documentation structure

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T012 [P] [US1] Contract test for POST /chat/message endpoint in backend/tests/contract/test_chat_api.py
- [X] T013 [P] [US1] Integration test for user documentation search journey in backend/tests/integration/test_documentation_search.py

### Implementation for User Story 1

- [X] T014 [P] [US1] Create Qdrant collection for docusaurus_docs with proper vector configuration
- [X] T015 [P] [US1] Implement query_qdrant function as a tool for the Agent in backend/app/agent.py
- [X] T016 [US1] Create OpenAI Agent with OpenRouter configuration in backend/app/agent.py
- [X] T017 [US1] Implement POST /chat/message endpoint in backend/app/main.py
- [X] T018 [US1] Add citation/references to documentation pages in chat responses
- [X] T019 [US1] Add error handling for OpenRouter API unavailability

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - RAG System Configuration (Priority: P2)

**Goal**: Configure the RAG backend to use OpenRouter instead of OpenAI's direct API, ensuring cost-effective model usage

**Independent Test**: The system can be configured to route all LLM requests through OpenRouter API with the specified base URL and model, without requiring changes to the core application logic

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T020 [P] [US2] Contract test for OpenRouter API configuration in backend/tests/contract/test_openrouter_config.py
- [X] T021 [P] [US2] Integration test for model routing verification in backend/tests/integration/test_model_routing.py

### Implementation for User Story 2

- [X] T022 [P] [US2] Verify system routes all LLM requests through OpenRouter API endpoint
- [X] T023 [US2] Configure system to use Google Gemini 2.0 Flash Experimental (free) model
- [X] T024 [US2] Add configuration validation for OpenRouter API settings
- [X] T025 [US2] Implement fallback mechanism when free model quota is exceeded

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Documentation Content Ingestion (Priority: P3)

**Goal**: Automatically ingest and index the Docusaurus documentation content into the Qdrant vector database

**Independent Test**: The system can parse Docusaurus documentation files, convert them to vector embeddings, and store them in Qdrant, making them available for semantic search

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T026 [P] [US3] Contract test for ingestion API endpoints in backend/tests/contract/test_ingestion_api.py
- [X] T027 [P] [US3] Integration test for documentation ingestion process in backend/tests/integration/test_documentation_ingestion.py

### Implementation for User Story 3

- [X] T028 [P] [US3] Create ingestion script to iterate through book/docs/*.md files
- [X] T029 [P] [US3] Implement text chunking logic with appropriate sizing in backend/ingestion/chunker.py
- [X] T030 [US3] Implement logic to connect to Qdrant and upsert documentation chunks with metadata
- [X] T031 [US3] Create POST /ingestion/trigger endpoint in backend/app/main.py
- [X] T032 [US3] Create GET /ingestion/status/{job_id} endpoint in backend/app/main.py
- [X] T033 [US3] Add proper metadata storage to link chunks back to source document URL

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T034 [P] Add documentation for the backend API endpoints in backend/docs/
- [X] T035 Code cleanup and refactoring across all modules
- [X] T036 Performance optimization to ensure <5s response time
- [X] T037 [P] Add comprehensive unit tests in backend/tests/unit/
- [X] T038 Security hardening for API endpoints
- [X] T039 Run quickstart.md validation to ensure deployment works correctly

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for POST /chat/message endpoint in backend/tests/contract/test_chat_api.py"
Task: "Integration test for user documentation search journey in backend/tests/integration/test_documentation_search.py"

# Launch all models for User Story 1 together:
Task: "Create Qdrant collection for docusaurus_docs with proper vector configuration"
Task: "Implement query_qdrant function as a tool for the Agent in backend/app/agent.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence