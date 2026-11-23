from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Small Business Inventory API"
    app_env: str = "development"
    secret_key: str
    database_url: str
    # Not used yet (reserved for caching / rate limiting), so it's optional.
    redis_url: str | None = None
    test_database_url: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )
    
    access_token_expire_minutes: int = 30
    algorithm: str = "HS256"

    @field_validator("database_url", "test_database_url")
    @classmethod
    def use_psycopg_driver(cls, value: str | None) -> str | None:
        # Hosted Postgres providers (Neon, Render, Heroku) hand out postgres:// or
        # postgresql:// URLs. SQLAlchemy needs the psycopg (v3) driver named explicitly.
        if value is None:
            return value
        for prefix in ("postgres://", "postgresql://"):
            if value.startswith(prefix):
                return "postgresql+psycopg://" + value[len(prefix):]
        return value


settings = Settings()  # type: ignore