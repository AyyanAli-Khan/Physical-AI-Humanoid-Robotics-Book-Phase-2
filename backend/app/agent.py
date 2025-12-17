from openai import AsyncOpenAI
from agents import Agent, set_default_openai_client, Runner
from agents import function_tool
from core.config import settings
from core.tools import query_qdrant
from typing import Optional
import asyncio
import logging


class RAGAgent:
    """
    RAG (Retrieval-Augmented Generation) Agent that uses OpenRouter API
    to query documentation stored in Qdrant vector database.
    """

    # def __init__(self, model: str = "mistralai/devstral-2512:free"):
    def __init__(self, model: str = "mistralai/devstral-2-2512:free"):
        # Configure OpenAI client to use OpenRouter
        self.client = AsyncOpenAI(
            api_key=settings.openrouter_api_key,
            base_url="https://openrouter.ai/api/v1"
        )

        # Set this client as the default for the agents framework
        set_default_openai_client(self.client)

        # Use a standard model name that the agents library recognizes
        # The actual model routing will be handled by the OpenRouter base_url
        self.model = "gpt-3.5-turbo"  # Using a standard name but it will be routed to OpenRouter

        # Create the agent with the Qdrant query tool
        self.agent = Agent(
            name="Documentation Assistant",
            instructions="You are a helpful documentation assistant. Use the query_qdrant tool to search for relevant documentation when answering questions. Always cite your sources and provide accurate information based on the documentation, if you provide the link to specific topic so it should like this `/docs/physical-ai/module-2/weeks-6-7/gazebo-simulation` always start from `/docs/physical-ai/{to specific topic}` this part is mandatory as base url `/docs/physical-ai`, Never provide link to `https://qdrant.com`  ",
            model=self.model,
            tools=[query_qdrant]
        )

    async def chat(self, message: str, session_id: Optional[str] = None):
        """
        Process a chat message using the RAG agent.

        Args:
            message: The user's message
            session_id: Optional session identifier for conversation history

        Returns:
            The agent's response
        """
        try:
            result = await Runner.run(
                self.agent,
                message
            )

            # Extract sources from the tool usage if available
            sources = []
            # In a more advanced implementation, we'd extract sources from the tool response

            return {
                "response": result.final_output,
                "session_id": session_id or "default_session",
                "sources": sources
            }
        except Exception as e:
            logging.error(f"Error in agent chat: {str(e)}")
            return {
                "response": f"Sorry, I encountered an error: {str(e)}",
                "session_id": session_id or "default_session",
                "sources": [],
                "error": str(e)
            }


# Global instance of the RAG agent
rag_agent = RAGAgent()