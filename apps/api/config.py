"""
SONIQ MASTER AI
Application configuration.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SONIQ MASTER AI"
    app_env: str = "development"
    debug: bool = True

    api_host: str = "0.0.0.0"
    api_port: int = 8000

    database_url: str = "sqlite:///./soniq_master_ai.db"

    upload_dir: str = "storage/uploads"
    master_dir: str = "storage/masters"

    max_upload_size_mb: int = 500

    default_sample_rate: int = 44100
    default_bit_depth: int = 24

    target_lufs: float = -14.0
    true_peak_db: float = -1.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
