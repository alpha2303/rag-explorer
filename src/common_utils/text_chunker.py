from enum import Enum
from typing import List
from io import TextIOWrapper


class ChunkMode(Enum):
    SIZE = "size"
    SENTENCE = "sentence"
    PARA = "para"


class TextChunker:
    def __init__(self, chunk_mode: ChunkMode = ChunkMode.PARA, chunk_size: int = 1024):
        self._chunk_mode: ChunkMode = chunk_mode
        self._chunk_size = chunk_size

    def chunk_text_file(self, file_object: TextIOWrapper) -> List[str]:
        text_chunks: List[str] = []
        match self._chunk_mode:
            case ChunkMode.SIZE:
                while True:
                    chunk = file_object.read(self._chunk_size)
                    if not chunk:
                        break
                    text_chunks.append(str(chunk))
            case ChunkMode.SENTENCE:
                buffer = ""
                while True:
                    chunk = file_object.read(self._chunk_size)
                    if not chunk:
                        break
                    buffer += str(chunk)
                    period_index = buffer.find(". ")
                    if period_index != -1:
                        text_chunks.append(buffer[: period_index + 1])
                        buffer = buffer[period_index + 2 :]
                if buffer:
                    text_chunks.append(buffer)
            case ChunkMode.PARA:
                buffer = ""
                while True:
                    chunk = file_object.read(self._chunk_size)
                    if not chunk:
                        break
                    buffer += str(chunk)
                    period_index = buffer.find("\n\n")
                    if period_index != -1:
                        text_chunks.append(buffer[:period_index])
                        buffer = buffer[period_index + 2 :]
                if buffer:
                    text_chunks.append(buffer)

        return text_chunks
