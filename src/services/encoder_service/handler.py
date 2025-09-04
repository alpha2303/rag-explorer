from pathlib import Path

from .lib import EncoderService
from ...common_utils import TextChunker, TextEmbedder
from ...common_utils.vector_db import ChromaDBManager
from ...common_utils.config import RAGExplorerConfig

def encoder_service_handler(config: RAGExplorerConfig) -> None:
    print("Setting up Chroma DB...")
    chroma_db_manager = ChromaDBManager(config.database_conn_string)
    print("Chroma DB setup complete.")
    text_chunker: TextChunker = TextChunker()
    print("Setting up Text Embedder...")
    text_embedder: TextEmbedder = TextEmbedder("all-MiniLM-L6-v2")
    print("Text Embedder setup complete.")

    print("Setting up Encoder Service...")
    encoder_service: EncoderService = EncoderService(chroma_db_manager, text_chunker, text_embedder)
    print("Encoder Service setup complete. Starting embedding...")
    embeddings = encoder_service.encode_text(Path("documents/AI_Engg_Preface.txt"))
    print(embeddings)
