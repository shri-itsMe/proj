from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    proj_name: str = "Hello FastAPI Project"

class Config:
    env_file = '.env'
    env_file_encoding = 'utf-8'

app_settings = Settings()