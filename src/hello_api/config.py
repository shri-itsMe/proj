from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pathlib import Path

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    # proj_name: str = "Hello FastAPI Project"
    os.environ["PROJ_NAME"] = Path(__file__).parent.name # Retrieves the parent directory of this python package folder

    proj_name: str = os.getenv("PROJ_NAME") # Puts in the env var

class Config:
    env_file = '.env'
    env_file_encoding = 'utf-8'

app_settings = Settings()