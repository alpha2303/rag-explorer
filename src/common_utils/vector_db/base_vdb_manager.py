from typing import List
import numpy as np

class BaseVDBManager:
    def insert_documents(self, texts: list[str], embeddings: np.ndarray) -> None:
        raise NotImplementedError()
