from typing import List
from pgvector.psycopg import register_vector
import psycopg
from sentence_transformers import SentenceTransformer
import numpy as np

from .base_vdb_manager import BaseVDBManager


class PGVectorManager(BaseVDBManager):
    def __init__(self, connection_string: str, model_name: str) -> None:
        self._connection_string: str = connection_string
        self._model_name: str = model_name

        if self._connection_string is None:
            raise ValueError("Connection string is required")

        self._init_db()

        self._sentence_transformer: SentenceTransformer = SentenceTransformer(
            self._model_name
        )
        self._texts: List[str] = []
        self._embeddings: np.ndarray | None = None

    def _init_db(self):
        self._conn = psycopg.connect(self._connection_string, autocommit=True)
        self._conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
        self._conn.execute(
            "CREATE TABLE IF NOT EXISTS documents (id SERIAL PRIMARY KEY, text TEXT, embedding VECTOR(384))"
        )
        register_vector(self._conn)

    def insert_documents(self, texts: List[str], embeddings: np.ndarray) -> None:
        if len(texts) != len(embeddings):
            raise ValueError("Embeddings and texts must have the same length")

        self._conn.execute(
            "INSERT INTO documents (text, embedding) VALUES (%s, %s)",
            (texts, embeddings),
        )
