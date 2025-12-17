from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


class ChatRequest(BaseModel):
    message: str = Field(..., description="The user's message to the chatbot")
    session_id: Optional[str] = Field(None, description="Unique identifier for the conversation session")
    thread_id: Optional[str] = Field(None, description="Unique identifier for the conversation thread")


class ChatResponse(BaseModel):
    response: str = Field(..., description="The chatbot's response to the user's message")
    session_id: str = Field(..., description="The session ID for the conversation")
    sources: Optional[List[Dict[str, Any]]] = Field(None, description="Sources used to generate the response")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="When the response was generated")


class IngestionRequest(BaseModel):
    source_path: str = Field(..., description="Path to the documentation source to be ingested")
    collection_name: str = Field(default="documentation_chunks", description="Name of the Qdrant collection to store the chunks")
    force_refresh: bool = Field(default=False, description="Whether to force refresh existing content")


class IngestionResponse(BaseModel):
    success: bool = Field(..., description="Whether the ingestion was successful")
    message: str = Field(..., description="Status message about the ingestion process")
    documents_processed: int = Field(..., description="Number of documents processed")
    chunks_created: int = Field(..., description="Number of chunks created from the documents")


class DocumentationChunk(BaseModel):
    id: str = Field(..., description="Unique identifier for the chunk")
    content: str = Field(..., description="The text content of the documentation chunk")
    source_url: str = Field(..., description="URL or path to the original documentation source")
    source_title: str = Field(..., description="Title of the documentation source")
    embedding: Optional[List[float]] = Field(None, description="Vector embedding of the content")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata about the chunk")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="When the chunk was created")


class QueryResponse(BaseModel):
    results: List[Dict[str, Any]] = Field(..., description="List of relevant documentation chunks found")
    query: str = Field(..., description="The original query that was searched for")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="When the query was executed")


class HealthResponse(BaseModel):
    status: str = Field(..., description="Health status of the service")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="When the health check was performed")
    version: str = Field(default="0.1.0", description="Version of the service")