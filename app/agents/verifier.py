from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import settings
from app.rag.generator import format_context

VERIFY_PROMPT = """
Determine whether the answer is supported by the provided context.

Return JSON only in this format:
{
  "supported": true,
  "reason": "short explanation"
}
"""


def verify_answer(answer: str, docs):
    llm = ChatGoogleGenerativeAI(
        google_api_key=settings.GOOGLE_API_KEY,
        model=settings.GEMINI_MODEL,
        temperature=0.0,
    )

    context = format_context(docs)

    user = f"""
ANSWER:
{answer}

CONTEXT:
{context}
"""

    resp = llm.invoke(
        [
            {"role": "system", "content": VERIFY_PROMPT},
            {"role": "user", "content": user},
        ]
    )

    return resp.content
