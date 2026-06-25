import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Centralized Application Configuration.
    Automatically loads environment variables from a local .env file
    and validates them on system startup.
    """
    
    # Grabs your async postgres database connection string
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "postgresql+asyncpg://postgres:postgres@localhost:5432/marketspy"
    )
    
    # Grabs your Gemini API key securely from your hidden environment
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instantiate a single configuration object to share across your backend modules
settings = Settings()