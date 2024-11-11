import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    TTS_API_KEY = os.getenv('TTS_API_KEY')

    @staticmethod
    def validate_config():
        required_vars = ['OPENAI_API_KEY', 'TTS_API_KEY']
        missing_vars = [var for var in required_vars if not getattr(Config, var)]
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}") 