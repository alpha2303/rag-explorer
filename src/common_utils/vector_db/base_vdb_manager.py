from typing import List
import numpy as np
from abc import ABC, abstractmethod

class BaseVDBManager(ABC):
    @abstractmethod
    def insert_documents(self, texts: List[str], embeddings: np.ndarray) -> None:
        pass
