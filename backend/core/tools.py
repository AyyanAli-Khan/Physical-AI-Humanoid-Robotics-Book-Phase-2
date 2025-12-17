from typing import List, Dict, Any
from .database import qdrant_manager
from .config import settings
from openai import AsyncOpenAI
import asyncio
import logging
from agents import function_tool
from qdrant_client.http import models


@function_tool
async def query_qdrant(query: str) -> Dict[str, Any]:
    """
    Query the Qdrant vector database for documentation chunks relevant to the input query.
    This function is designed to be used as a tool with the OpenAI Agents SDK.

    Args:
        query: The search query string

    Returns:
        A dictionary containing the search results
    """
    try:
        # Initialize OpenAI client for embedding generation
        # Note: This will be configured to use OpenRouter in the agent setup
        client = AsyncOpenAI(
            api_key=settings.openrouter_api_key,
            base_url="https://openrouter.ai/api/v1"
        )

        # Generate embedding for the query
        response = await client.embeddings.create(
            input=query,
            model="text-embedding-ada-002"  # Standard OpenAI embedding model
        )
        query_embedding = response.data[0].embedding

        # Search in Qdrant collection
        search_results = qdrant_manager.get_client().search(
            collection_name="documentation_chunks",
            query_vector=query_embedding,
            limit=5,  # Return top 5 results
            with_payload=True
        )

        # Format results with proper source attribution
        results = []
        for hit in search_results:
            results.append({
                "id": hit.id,
                "content": hit.payload.get("content", ""),
                "source_url": hit.payload.get("source_url", ""),
                "source_title": hit.payload.get("source_title", ""),
                "score": hit.score
            })

        # Return formatted results
        formatted_results = {
            "query": query,
            "results": results,
            "count": len(results),
            "sources": [f"[{result['source_title']}]({result['source_url']})" for result in results]
        }

        logging.info(f"Query '{query}' returned {len(results)} results")
        return formatted_results

    except Exception as e:
        logging.error(f"Error in query_qdrant: {str(e)}")
        return {
            "query": query,
            "results": [],
            "error": str(e),
            "count": 0,
            "sources": []
        }