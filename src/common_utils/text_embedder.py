from typing import List, Optional

from sentence_transformers import SentenceTransformer
import numpy as np


class TextEmbedder:
    def __init__(self, model_name: str) -> None:
        self._model_name = model_name
        self._sentence_transformer: SentenceTransformer = SentenceTransformer(
            self._model_name
        )
        self._texts: List[str] = []
        self._embeddings: Optional[np.ndarray] = None

    def generate_embeddings(self, texts: List[str]) -> Optional[np.ndarray]:
        # Implement embedding generation logic here
        self._embeddings: Optional[np.ndarray] = self._sentence_transformer.encode(
            texts
        )

        return self._embeddings
