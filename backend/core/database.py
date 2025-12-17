from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import Optional
from .config import settings


class QdrantManager:
    def __init__(self):
        self.client = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key,
            prefer_grpc=True  # Use gRPC for better performance
        )

    def get_client(self) -> QdrantClient:
        """Return the Qdrant client instance."""
        return self.client

    async def create_documentation_collection(self, collection_name: str = "documentation_chunks", vector_size: int = 1536):
        """
        Create a collection for storing documentation chunks with embeddings.

        Args:
            collection_name: Name of the collection to create
            vector_size: Size of the embedding vectors (default 1536 for OpenAI embeddings)
        """
        try:
            # Check if collection already exists
            collections = self.client.get_collections()
            collection_names = [col.name for col in collections.collections]

            if collection_name not in collection_names:
                # Create the collection
                self.client.create_collection(
                    collection_name=collection_name,
                    vectors_config=models.VectorParams(
                        size=vector_size,
                        distance=models.Distance.COSINE
                    )
                )
                print(f"Collection '{collection_name}' created successfully.")
            else:
                print(f"Collection '{collection_name}' already exists.")
        except Exception as e:
            print(f"Error creating collection: {e}")
            raise


# Global instance
qdrant_manager = QdrantManager()