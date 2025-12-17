import re
import uuid
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class DocumentChunk:
    """Represents a chunk of a document with metadata."""
    id: str
    content: str
    source_url: str
    source_title: str
    metadata: Dict[str, Any]


class TextChunker:
    """
    Utility class for chunking text content into smaller pieces suitable for
    vector database storage and retrieval.
    """

    def __init__(self, chunk_size: int = 1000, overlap: int = 100):
        """
        Initialize the chunker with specified parameters.

        Args:
            chunk_size: Maximum size of each chunk in characters
            overlap: Number of overlapping characters between chunks
        """
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text: str, source_url: str, source_title: str) -> List[DocumentChunk]:
        """
        Split text into overlapping chunks.

        Args:
            text: The text to be chunked
            source_url: URL or path of the source document
            source_title: Title of the source document

        Returns:
            List of DocumentChunk objects
        """
        if len(text) <= self.chunk_size:
            return [DocumentChunk(
                id=str(uuid.uuid5(uuid.NAMESPACE_URL, source_url + text[:50])),
                content=text,
                source_url=source_url,
                source_title=source_title,
                metadata={"position": 0, "total_chunks": 1}
            )]

        chunks = []
        start = 0
        chunk_num = 0

        while start < len(text):
            # Determine the end position
            end = start + self.chunk_size

            # If this is not the last chunk, try to break at a sentence boundary
            if end < len(text):
                # Look for sentence endings near the end of the chunk
                search_start = max(start, end - 200)  # Look back up to 200 chars
                sentence_end = -1

                for pattern in [r'[.!?]\s+', r'\n\s*\n', r'\n']:
                    matches = list(re.finditer(pattern, text[search_start:end]))
                    if matches:
                        # Get the last match
                        last_match = matches[-1]
                        potential_end = search_start + last_match.end()
                        if potential_end > sentence_end:
                            sentence_end = potential_end

                # If we found a good breaking point, use it
                if sentence_end > -1 and sentence_end > start + self.chunk_size // 2:
                    end = start + sentence_end
                else:
                    pass
                    # If no good breaking point, break at the max chunk size

            # Extract the chunk
            chunk_text = text[start:end]

            # Create a chunk with metadata
            chunk = DocumentChunk(
                id=str(uuid.uuid5(uuid.NAMESPACE_URL, source_url + str(start))),
                content=chunk_text,
                source_url=source_url,
                source_title=source_title,
                metadata={
                    "position": chunk_num,
                    "start_pos": start,
                    "end_pos": end,
                    "total_chunks": len(text) // self.chunk_size + 1
                }
            )

            chunks.append(chunk)

            # Move to the next chunk position with overlap
            start = end - self.overlap
            chunk_num += 1

            # Prevent infinite loops in case of issues
            if start >= end:
                start = end

        return chunks

    def chunk_markdown(self, markdown_text: str, source_url: str, source_title: str) -> List[DocumentChunk]:
        """
        Specialized chunking for markdown content, preserving document structure.

        Args:
            markdown_text: The markdown text to be chunked
            source_url: URL or path of the source document
            source_title: Title of the source document

        Returns:
            List of DocumentChunk objects
        """
        # Split by headers to maintain document structure
        sections = self._split_markdown_by_headers(markdown_text)

        all_chunks = []
        for section in sections:
            section_chunks = self.chunk_text(section, source_url, source_title)
            all_chunks.extend(section_chunks)

        return all_chunks

    def _split_markdown_by_headers(self, markdown_text: str) -> List[str]:
        """
        Split markdown text by headers to preserve document structure.

        Args:
            markdown_text: The markdown text to split

        Returns:
            List of text sections
        """
        # Pattern to match markdown headers (h1 to h6)
        header_pattern = r'^(#{1,6})\s+(.*)$'
        lines = markdown_text.split('\n')

        sections = []
        current_section = []

        for line in lines:
            if re.match(header_pattern, line.strip()):
                # If we have a current section, save it
                if current_section:
                    sections.append('\n'.join(current_section))
                    current_section = []
                # Add the header line to the new section
                current_section.append(line)
            else:
                current_section.append(line)

        # Add the last section if it exists
        if current_section:
            sections.append('\n'.join(current_section))

        # Filter out empty sections
        sections = [section.strip() for section in sections if section.strip()]

        return sections