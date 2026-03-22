import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    GEMINI_EMBED_MODEL = os.getenv("GEMINI_EMBED_MODEL", "gemini-embedding-001")

    UPLOAD_DIR = os.getenv("UPLOAD_DIR", "data/uploads")
    CHROMA_DIR = os.getenv("CHROMA_DIR", "data/chroma")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "enterprise_docs")
    TOP_K = int(os.getenv("TOP_K", "6"))
    MAX_FILE_MB = int(os.getenv("MAX_FILE_MB", "20"))


settings = Settings()
