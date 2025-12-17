from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class AgentSession(BaseModel):
    """
    Model representing an agent session with conversation history.
    """
    session_id: str
    created_at: datetime
    updated_at: datetime
    conversation_history: List[Dict[str, str]]  # List of {'role': 'user'|'assistant', 'content': 'message'}
    metadata: Optional[Dict[str, Any]] = None


class AgentResponse(BaseModel):
    """
    Model representing the response from the RAG agent.
    """
    session_id: str
    response: str
    sources: Optional[List[Dict[str, Any]]] = None
    timestamp: datetime = datetime.utcnow()
    success: bool = True
    error: Optional[str] = None


class AgentRequest(BaseModel):
    """
    Model representing a request to the RAG agent.
    """
    session_id: Optional[str] = None
    message: str
    include_sources: bool = True