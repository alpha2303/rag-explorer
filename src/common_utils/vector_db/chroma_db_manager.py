from typing import List
import chromadb
from .base_vdb_manager import BaseVDBManager
import numpy as np


class ChromaDBManager(BaseVDBManager):
    def __init__(self, config):
        self._client = chromadb.Client()
        self._collection: chromadb = self._create_collection("documents")

    def _create_collection(self, collection_name):
        return self._client.create_collection(collection_name, get_or_create=True)

    def insert_documents(self, texts: List[str], embeddings: np.ndarray):
        self._collection.add(
            ids=[str(i) for i in range(len(texts))],
            documents=texts,
            embeddings=embeddings,
        )

    def query_documents(self, query: str, top_k: int = 5) -> List[str]:
        return self._collection.query(query=query, n_results=top_k)
