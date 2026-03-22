from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import settings

SYSTEM = """You are an enterprise document assistant.
Rules:
- Use ONLY the provided context.
- If the answer is not in the context, say: "I couldn’t find that in the uploaded documents."
- Always provide citations in [source | page/chunk] format.
"""


def format_context(docs):
    lines = []
    for d in docs:
        src = d.metadata.get("source", "unknown")
        page = d.metadata.get("page", d.metadata.get("chunk_id", "?"))
        lines.append(f"[{src} | {page}] {d.page_content}")
    return "\n\n".join(lines)


def generate_answer(question: str, docs):
    print("DEBUG: generate_answer() started")
    llm = ChatGoogleGenerativeAI(
        google_api_key=settings.GOOGLE_API_KEY,
        model=settings.GEMINI_MODEL,
        temperature=0.1,
    )

    context = format_context(docs)
    print("DEBUG: context prepared")

    user = f"QUESTION:\n{question}\n\nCONTEXT:\n{context}\n\nAnswer with citations."
    resp = llm.invoke(
        [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]
    )

    print("DEBUG: generate_answer() finished")
    return resp.content
