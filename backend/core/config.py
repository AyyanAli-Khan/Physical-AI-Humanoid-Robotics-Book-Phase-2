from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    openrouter_api_key: str = Field(..., validation_alias="OPENROUTER_API_KEY")
    qdrant_url: str = Field(..., validation_alias="QDRANT_URL")
    qdrant_api_key: str = Field(..., validation_alias="QDRANT_API_KEY")
    environment: str = Field(default="development", validation_alias="ENVIRONMENT")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="forbid",
    )


settings = Settings()
