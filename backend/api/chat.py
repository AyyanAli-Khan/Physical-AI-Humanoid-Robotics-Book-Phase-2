from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from core.models import ChatRequest, ChatResponse
from app.agent import rag_agent
from datetime import datetime

router = APIRouter()


@router.post("/chat/message", response_model=ChatResponse)
async def chat_message(chat_request: ChatRequest):
    """
    Process a chat message and return a response from the RAG agent.
    """
    try:
        # Process the message using the RAG agent
        result = await rag_agent.chat(chat_request.message, chat_request.session_id)

        # Create the response with proper structure
        response = ChatResponse(
            response=result["response"],
            session_id=result["session_id"],
            sources=result.get("sources", []),
            timestamp=datetime.utcnow()
        )

        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat message: {str(e)}")


@router.post("/ingestion/process")
async def process_ingestion(source_path: str, collection_name: str = "documentation_chunks", force_refresh: bool = False):
    """
    Trigger the documentation ingestion process.
    """
    try:
        from ..ingestion.ingest import DocumentationIngestor
        import asyncio

        ingestor = DocumentationIngestor()
        result = await ingestor.ingest_from_directory(source_path, collection_name)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing ingestion: {str(e)}")


@router.get("/session/{session_id}")
async def get_session(session_id: str):
    """
    Get information about a specific session.
    """
    # This would be implemented with actual session management
    return {
        "session_id": session_id,
        "status": "active",
        "created_at": datetime.utcnow(),
        "last_activity": datetime.utcnow()
    }


@router.post("/session")
async def create_session():
    """
    Create a new chat session.
    """
    import uuid
    session_id = str(uuid.uuid4())

    return {
        "session_id": session_id,
        "created_at": datetime.utcnow()
    }