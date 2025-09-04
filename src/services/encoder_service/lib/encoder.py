from pathlib import Path
from typing import List, Optional
import numpy as np

from ....common_utils import TextChunker, TextEmbedder
from ....common_utils.vector_db import BaseVDBManager


class EncoderService:
    def __init__(
        self,
        vector_db_manager: BaseVDBManager,
        text_chunker: TextChunker,
        text_embedder: TextEmbedder,
    ):
        self._vector_db_manager = vector_db_manager
        self._text_chunker = text_chunker
        self._text_embedder = text_embedder

    def encode_text(self, file_path: Path) -> Optional[np.ndarray]:
        with open(file_path, "r", encoding="utf-8") as file_object:
            print("Chunking text file...")
            text_chunks: List[str] = self._text_chunker.chunk_text_file(file_object)
            print("Generating embeddings...")
            embeddings = self._text_embedder.generate_embeddings(text_chunks)
            if embeddings is not None:
                print("Storing to vector database...")
                self._vector_db_manager.insert_documents(text_chunks, embeddings)
        return embeddings
