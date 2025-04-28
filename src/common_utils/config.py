from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class DBConfig(BaseModel):
    database_conn_string: str


class RAGExplorerSettings(BaseSettings):
    DATABASE_CONN_STRING: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=True)


class RAGExplorerConfig(BaseModel):
    database_conn_string: str

@lru_cache()
def load_config():
    settings: RAGExplorerSettings = RAGExplorerSettings() # type: ignore
    return RAGExplorerConfig(database_conn_string=settings.DATABASE_CONN_STRING)
