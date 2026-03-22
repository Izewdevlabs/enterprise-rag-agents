from app.rag.vectorstore import get_vectorstore
from app.config import settings


def retrieve(query: str):
    print("DEBUG: retrieve() started")
    vs = get_vectorstore()
    docs = vs.similarity_search(query, k=settings.TOP_K)
    print(f"DEBUG: retrieve() finished with {len(docs)} docs")
    return docs
