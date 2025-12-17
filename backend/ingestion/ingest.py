import os
import asyncio
from pathlib import Path
from typing import List, Dict, Any
import markdown
from core.database import qdrant_manager
from core.config import settings
from .chunker import TextChunker, DocumentChunk
from openai import AsyncOpenAI
import logging


class DocumentationIngestor:
    """
    Class responsible for ingesting documentation from various sources
    and storing it in the Qdrant vector database.
    """

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.openrouter_api_key,
            base_url="https://openrouter.ai/api/v1"
        )
        self.chunker = TextChunker()
        self.qdrant_client = qdrant_manager.get_client()

    async def ingest_from_directory(self, source_path: str, collection_name: str = "documentation_chunks") -> Dict[str, Any]:
        """
        Ingest all markdown files from a directory into the vector database.

        Args:
            source_path: Path to the directory containing documentation files
            collection_name: Name of the Qdrant collection to store the chunks

        Returns:
            Dictionary with ingestion statistics
        """
        source_dir = Path(source_path)
        if not source_dir.exists():
            raise ValueError(f"Source directory does not exist: {source_path}")

        # Create the collection if it doesn't exist
        await qdrant_manager.create_documentation_collection(collection_name)

        # Include both .md and .mdx files for documentation
        markdown_files = list(source_dir.rglob("*.md")) + list(source_dir.rglob("*.mdx"))
        total_documents = len(markdown_files)
        total_chunks = 0

        for file_path in markdown_files:
            try:
                # Read the markdown file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Generate a relative URL for the source
                relative_path = file_path.relative_to(source_dir)
                source_url = f"/docs/{relative_path.as_posix()}"
                source_title = file_path.stem.replace('_', ' ').replace('-', ' ').title()

                # Extract content and metadata from markdown
                extracted_content = self._extract_markdown_content(content, source_url, source_title)

                # Chunk the content
                chunks = self.chunker.chunk_markdown(extracted_content['content'], source_url, extracted_content['title'])

                # Process and store each chunk
                for chunk in chunks:
                    await self._store_chunk(chunk, collection_name)
                    total_chunks += 1

                logging.info(f"Processed {file_path.name}: {len(chunks)} chunks created")

            except Exception as e:
                logging.error(f"Error processing {file_path}: {str(e)}")
                continue

        return {
            "success": True,
            "message": f"Successfully processed {total_documents} documents and created {total_chunks} chunks",
            "documents_processed": total_documents,
            "chunks_created": total_chunks
        }

    def _extract_markdown_content(self, content: str, source_url: str, source_title: str) -> Dict[str, str]:
        """
        Extract content and metadata from markdown text.

        Args:
            content: Raw markdown content
            source_url: URL of the source document
            source_title: Title of the source document

        Returns:
            Dictionary containing extracted content and metadata
        """
        # Extract title from markdown if it exists (first H1)
        lines = content.split('\n')
        title = source_title  # Default to the filename-based title

        for line in lines:
            if line.strip().startswith('# '):
                title = line.strip()[2:]  # Remove '# ' prefix
                break

        # Remove metadata/frontmatter if present
        if content.strip().startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2]  # Skip frontmatter

        # Convert markdown to plain text for better embedding
        # (In a real implementation, we might want to preserve more structure)
        html_content = markdown.markdown(content)
        # Remove HTML tags to get plain text
        import re
        plain_text = re.sub('<[^<]+?>', '', html_content)

        return {
            "title": title,
            "content": plain_text.strip()
        }

    async def _store_chunk(self, chunk: DocumentChunk, collection_name: str):
        """
        Store a document chunk in the Qdrant vector database.

        Args:
            chunk: DocumentChunk object to store
            collection_name: Name of the Qdrant collection
        """
        # Generate embedding for the chunk content
        embedding = await self._generate_embedding(chunk.content)

        # Prepare the payload
        payload = {
            "content": chunk.content,
            "source_url": chunk.source_url,
            "source_title": chunk.source_title,
            "metadata": chunk.metadata
        }

        # Upsert the point to Qdrant
        from qdrant_client.http import models
        self.qdrant_client.upsert(
            collection_name=collection_name,
            points=[
                models.PointStruct(
                    id=str(chunk.id),  # Ensure ID is a string
                    vector=embedding,
                    payload=payload
                )
            ]
        )

    async def _generate_embedding(self, text: str) -> List[float]:
        """
        Generate embedding for the given text using OpenAI API via OpenRouter.

        Args:
            text: Text to generate embedding for

        Returns:
            List of floats representing the embedding vector
        """
        try:
            response = await self.client.embeddings.create(
                input=text,
                model="text-embedding-ada-002"  # Using OpenAI embeddings via OpenRouter
            )
            return response.data[0].embedding
        except Exception as e:
            logging.error(f"Error generating embedding: {str(e)}")
            # Return a zero vector as fallback (this should be improved in production)
            return [0.0] * 1536  # Assuming 1536-dim embeddings


async def main():
    """
    Main function to run the ingestion process.
    This can be called from command line or as part of an API endpoint.
    """
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m backend.ingestion.ingest <source_directory>")
        return

    source_path = sys.argv[1]
    ingestor = DocumentationIngestor()

    result = await ingestor.ingest_from_directory(source_path)
    print(result)


if __name__ == "__main__":
    # Run the ingestion if called directly
    import asyncio
    asyncio.run(main())