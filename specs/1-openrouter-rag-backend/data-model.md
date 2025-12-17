# Data Model: OpenRouter RAG Backend

## Entities

### Documentation Chunk
- **id**: string - Unique identifier for the chunk
- **vector**: list[float] - Embedding vector representation of the content
- **content**: string - The actual text content of the documentation chunk
- **source_file**: string - Path to the original documentation file
- **url**: string - URL to the documentation page
- **metadata**: dict - Additional metadata (title, headings, etc.)
- **created_at**: datetime - Timestamp when the chunk was created

### Qdrant Vector Store
- **collection_name**: string - Name of the Qdrant collection ("docusaurus_docs")
- **vectors_config**: VectorParams - Configuration for vector dimensions and distance metric
- **points**: list[PointStruct] - List of all document chunks stored as vectors with payloads

### Chat Session
- **session_id**: string - Unique identifier for the conversation session
- **user_id**: string - Identifier for the user (optional, for tracking)
- **messages**: list[dict] - List of messages in the conversation (role, content, timestamp)
- **created_at**: datetime - When the session was created
- **updated_at**: datetime - When the session was last updated
- **context**: dict - Additional context for the conversation

## Relationships
- Each Documentation Chunk belongs to one Qdrant Vector Store collection
- Each Chat Session may reference multiple Documentation Chunks through the RAG process
- Documentation Chunks maintain their source file and URL relationships for citations

## Validation Rules
- Documentation Chunk content must be non-empty and less than 10000 characters
- Vector embeddings must have the correct dimensionality (1536 for OpenAI ada-002 or similar)
- Chat Session messages must have valid roles (user, assistant)
- Source file paths must exist within the Docusaurus documentation structure

## State Transitions
- Documentation Chunk: PENDING_EMBEDDING → EMBEDDED → INDEXED_IN_QDRANT
- Chat Session: CREATED → ACTIVE → ENDED