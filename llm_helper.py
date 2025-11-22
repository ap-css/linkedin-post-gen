# /mnt/data/llm_helper.py
from dotenv import load_dotenv
import os
import logging

# Langchain / Groq client import (adjust if you used a different client name)
try:
    from langchain_groq import ChatGroq
except Exception:
    # If your environment uses a different package name, this will make the error clear.
    raise

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY not set in environment. Set it in your .env or environment variables."
    )

# Default model name — change this to a model you definitely have access to if needed.
MODEL_NAME = os.getenv("GROQ_MODEL_NAME", "deepseek-r1-distill-llama-70b")

logger.info("Initializing Groq client with model: %s", MODEL_NAME)

# Create the ChatGroq client instance
# If your version of the library expects different parameter names, adjust here.
llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=MODEL_NAME)



