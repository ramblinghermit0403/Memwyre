"""
Ingestion Service: Handle text chunking and embedding generation
"""
from typing import List, Dict
from langchain_text_splitters import RecursiveCharacterTextSplitter
import uuid

class IngestionService:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize the ingestion service with a text splitter.
        
        Args:
            chunk_size: Maximum size of each chunk
            chunk_overlap: Number of characters to overlap between chunks
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
    
    def chunk_text(self, text: str) -> List[str]:
        """
        Chunk text using RecursiveCharacterTextSplitter.
        
        Args:
            text: The text to chunk
            
        Returns:
            List of text chunks
        """
        return self.text_splitter.split_text(text)
    
    def process_text(
        self, 
        text: str, 
        document_id: int, 
        title: str, 
        doc_type: str = "memory"
    ) -> tuple[List[str], List[str], List[Dict]]:
        """
        Process text into chunks with metadata for vector store.
        
        Args:
            text: The text to process
            document_id: ID of the parent document
            title: Title of the document
            doc_type: Type of document ('memory' or 'file')
            
        Returns:
            Tuple of (embedding_ids, chunk_texts, metadatas)
        """
        chunks = self.chunk_text(text)
        
        embedding_ids = []
        chunk_texts = []
        metadatas = []
        
        for i, chunk_text in enumerate(chunks):
            embedding_id = str(uuid.uuid4())
            
            embedding_ids.append(embedding_id)
            chunk_texts.append(chunk_text)
            metadatas.append({
                "document_id": document_id,
                "chunk_index": i,
                "title": title,
                "type": doc_type
            })
        
        return embedding_ids, chunk_texts, metadatas

# Global instance
ingestion_service = IngestionService()
