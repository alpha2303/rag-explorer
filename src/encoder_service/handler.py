from pathlib import Path

from .lib import EncoderService
from ..common_utils import TextChunker, TextEmbedder, load_config
from ..common_utils.vector_db import ChromaDBManager
from ..common_utils.config import RAGExplorerConfig

def encoder_service_handler(config: RAGExplorerConfig) -> None:
    chroma_db_manager = ChromaDBManager(config.database_conn_string)
    text_chunker: TextChunker = TextChunker()
    text_embedder: TextEmbedder = TextEmbedder("all-MiniLM-L6-v2")

    encoder_service: EncoderService = EncoderService(chroma_db_manager, text_chunker, text_embedder)
    embeddings = encoder_service.encode_text(Path("documents/AI_Engg_Preface.txt"))
    print(embeddings)
