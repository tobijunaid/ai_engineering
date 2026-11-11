from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Small Business Inventory API"
    app_env: str = "development"
    secret_key: str
    database_url: str
    redis_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )
    
    access_token_expire_minutes: int = 30
    algorithm: str = "HS256"


settings = Settings()  # type: ignore