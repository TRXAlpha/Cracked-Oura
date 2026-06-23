from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional
import os

class Settings(BaseSettings):
    env: str = Field(
        default="LOCAL_DEV", 
        description="Environment: LOCAL_DEV or CLOUD_PROD"
    )
    database_url: Optional[str] = Field(
        default=None, 
        description="PostgreSQL connection string for CLOUD_PROD"
    )
    proxy_url: Optional[str] = Field(
        default=None, 
        description="Proxy URL for the scraper in CLOUD_PROD"
    )
    
    # Render specific disk config
    data_dir: str = Field(
        default="./data", 
        description="Directory for local data storage (like SQLite)"
    )
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        extra="ignore"
    )
    
    @property
    def is_cloud(self) -> bool:
        return self.env.upper() == "CLOUD_PROD"

settings = Settings()
