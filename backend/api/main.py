from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.models import HealthResponse
from datetime import datetime
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


# Create FastAPI app instance
app = FastAPI(
    title="RAG Backend with OpenRouter Integration",
    description="API for documentation Q&A using RAG and OpenRouter",
    version="0.1.0"
)

# Add CORS middleware for Docusaurus frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and include chat router
from .chat import router as chat_router
app.include_router(chat_router, prefix="/api/v1", tags=["chat"])


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow(),
        version="0.1.0"
    )


@app.get("/")
async def root():
    """
    Root endpoint providing basic information about the API.
    """
    return {
        "message": "RAG Backend with OpenRouter Integration",
        "version": "0.1.0",
        "endpoints": [
            "/health",
            "/api/v1/chat/message",
            "/api/v1/ingestion/process"
        ]
    }


if __name__ == "__main__":
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)