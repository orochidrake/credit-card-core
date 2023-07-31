from pydantic.v1 import BaseSettings
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv(".env")

class Settings(BaseSettings):
    app_name: str = "Credit Card Crud API"
    PORT: str
    
    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()