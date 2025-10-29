-----------------------------------

import os
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

APP_NAME = "AI Desktop Assistant"
MODEL_NAME = "gpt-4o-mini"
DEBUG_MODE = Trueor


if not OPENAI_API_KEY:
    raise ValueError("❌ Missing OpenAI API key! Please set OPENAI_API_KEY in your environment or .env file.")
