from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # -----------------------------
    # Application
    # -----------------------------

    app_name: str = Field(alias="APP_NAME")
    app_version: str = Field(alias="APP_VERSION")
    debug: bool = Field(alias="DEBUG")

    # -----------------------------
    # Storage
    # -----------------------------

    storage_path: Path = Field(alias="STORAGE_PATH")
    documents_path: Path = Field(alias="DOCUMENTS_PATH")
    chroma_path: Path = Field(alias="CHROMA_PATH")

    # -----------------------------
    # Embeddings
    # -----------------------------

    embedding_model: str = Field(alias="EMBEDDING_MODEL")

    # -----------------------------
    # Ollama
    # -----------------------------

    ollama_host: str = Field(alias="OLLAMA_HOST")
    ollama_model: str = Field(alias="OLLAMA_MODEL")

    # -----------------------------
    # Retrieval
    # -----------------------------

    top_k: int = Field(alias="TOP_K")

    # -----------------------------
    # Database
    # -----------------------------

    database_url: str = Field(alias="DATABASE_URL")

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()