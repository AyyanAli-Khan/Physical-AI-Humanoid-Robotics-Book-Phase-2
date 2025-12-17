# Research: OpenRouter RAG Backend

## Decision: OpenAI Agents SDK Import and Initialization
**Rationale**: Based on research of the OpenAI Agents SDK documentation, the correct import pattern is to use `from agents import Agent, Runner` and related components. For OpenRouter integration, we'll use `set_default_openai_client` with a custom AsyncOpenAI client configured with the OpenRouter base URL.

**Implementation**:
```python
from openai import AsyncOpenAI
from agents import Agent, Runner, set_default_openai_client

# Configure OpenRouter client
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
set_default_openai_client(client)
```

## Decision: Qdrant Client Setup
**Rationale**: Based on Qdrant documentation, the preferred approach is to use the QdrantClient with async operations for upserting vectors. We'll use PointStruct for data points with vectors and metadata.

**Implementation**:
```python
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

client = QdrantClient(url="http://localhost:6333")
# For async operations: AsyncQdrantClient

# Create collection
client.create_collection(
    collection_name="docusaurus_docs",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE),  # Assuming OpenAI embeddings
)

# Upsert points
client.upsert(
    collection_name="docusaurus_docs",
    points=[
        PointStruct(
            id=1,
            vector=[0.05, 0.61, 0.76, 0.74],  # embedding vector
            payload={"source": "doc.md", "content": "text content", "url": "/docs/doc"}
        )
    ]
)
```

## Decision: FastAPI Agent Integration
**Rationale**: Based on FastAPI documentation, async endpoints should be used for agent integration to handle long-running operations without blocking. We'll use async def for endpoints that interact with the agent and implement proper session state management using request-scoped dependencies.

**Implementation**:
```python
from fastapi import FastAPI, Depends
import asyncio

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(query: str):
    # Run agent asynchronously
    result = await Runner.run(agent, query)
    return {"response": result.final_output}
```

## Decision: Docker Compose for Qdrant
**Rationale**: Based on Qdrant documentation, the standard approach is to use the official qdrant/qdrant Docker image with proper port mapping and persistent storage.

**Implementation**:
```yaml
version: '3.8'
services:
  qdrant:
    image: qdrant/qdrant
    container_name: qdrant
    ports:
      - "6333:6333"
      - "6334:6334"
    volumes:
      - ./qdrant_storage:/qdrant/storage:z
    restart: unless-stopped
```

## Decision: ChatKit Integration Pattern
**Rationale**: For frontend integration with Docusaurus, we'll implement a CORS-enabled FastAPI backend that can serve the necessary endpoints for ChatKit to communicate with our RAG agent.

**Implementation**: FastAPI with CORS middleware enabled to allow requests from the Docusaurus frontend domain.