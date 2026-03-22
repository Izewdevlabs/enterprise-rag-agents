from langchain_core.documents import Document
from app.rag.vectorstore import get_vectorstore


def index_chunks(chunks: list[Document]) -> int:
    vs = get_vectorstore()
    vs.add_documents(chunks)
    return len(chunks)
