from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config import settings


def get_embeddings():
    return GoogleGenerativeAIEmbeddings(
        google_api_key=settings.GOOGLE_API_KEY,
        model=settings.GEMINI_EMBED_MODEL,
    )


def get_vectorstore():
    return Chroma(
        collection_name=settings.COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=settings.CHROMA_DIR,
    )
