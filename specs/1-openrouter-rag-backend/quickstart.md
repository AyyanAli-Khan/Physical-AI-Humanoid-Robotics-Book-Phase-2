# Quickstart: OpenRouter RAG Backend

## Prerequisites
- Python 3.11+
- Docker and Docker Compose
- OpenRouter API key
- Node.js (for Docusaurus frontend)

## Setup

### 1. Clone and Prepare Repository
```bash
# Already in the repository
cd D:\Robotic-book-backend
```

### 2. Create Backend Directory Structure
```bash
mkdir -p backend/{app,ingestion,tests}
```

### 3. Set up Environment
```bash
# Create .env file in backend/
cat > backend/.env << EOF
OPENROUTER_API_KEY=your_openrouter_api_key_here
QDRANT_URL=http://localhost:6333
EMBEDDING_MODEL=text-embedding-3-small  # or appropriate model
EOF
```

### 4. Install Dependencies
```bash
cd backend
pip install fastapi uvicorn python-dotenv openai qdrant-client PyYAML
```

### 5. Start Qdrant Service
```bash
# From repository root
docker-compose up -d
# Or if creating docker-compose.yml:
docker run -d --name qdrant -p 6333:6333 -p 6334:6334 qdrant/qdrant
```

### 6. Run Ingestion
```bash
cd backend
python ingestion/ingest.py
```

### 7. Start the API Server
```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

## Usage

### Ingest Documentation
The ingestion script will parse all `.md` files in `book/docs` and store them in Qdrant.

### Chat with the Agent
Send requests to `http://localhost:8000/chat/message` with the message content.

### Integrate with Docusaurus
Add the ChatKit script to your Docusaurus site to connect to the backend API.

## Testing
```bash
# Run unit tests
python -m pytest tests/unit/

# Run integration tests
python -m pytest tests/integration/
```