from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    LLM_PROVIDER: str = "gemma"

    GOOGLE_API_KEY: str = os.getenv('GOOGLE_API_KEY')
    GOOGLE_MODEL: str = "gemma-3-27b-it"

settings = Settings()