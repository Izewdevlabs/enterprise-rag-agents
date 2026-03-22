from app.rag.retriever import retrieve

def tool_retrieve(query: str):
    return retrieve(query)