import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "claude-3-5-sonnet-202401022")
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))

    @classmethod
    def validate(cls):
        if not cls.ANTHROPIC_API_KEY:
            raise ValueError("ANTHROPIC_API_KEY is not set in the environment variables.")