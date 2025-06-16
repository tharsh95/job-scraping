import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MAX_CONTENT_LENGTH = 16300
    SECRET_KEY = "secret"


config = Config()
