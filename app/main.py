import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.config import settings
from app.safety.guardrails import validate_upload
from app.ingestion.loaders import load_document
from app.ingestion.chunking import chunk_documents
from app.ingestion.indexer import index_chunks
from app.schemas import AskRequest, AskResponse
from app.agents.graph import build_graph

app = FastAPI(title="Enterprise RAG Agents (Gemini)")

graph = build_graph()


@app.get("/")
async def root():
    return {
        "message": "Enterprise RAG Agents API is running",
        "docs": "/docs",
        "status": "ok",
    }


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    try:
        validate_upload(file.filename, len(content), settings.MAX_FILE_MB)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    save_path = os.path.join(settings.UPLOAD_DIR, file.filename)
    with open(save_path, "wb") as f:
        f.write(content)

    try:
        docs = load_document(save_path)
        for d in docs:
            d.metadata["source"] = file.filename
        chunks = chunk_documents(docs)
        n = index_chunks(chunks)
        return {"status": "ok", "file": file.filename, "chunks_indexed": n}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {e}")


@app.post("/ask", response_model=AskResponse)
async def ask(req: AskRequest):
    if not req.question or len(req.question.strip()) < 3:
        raise HTTPException(status_code=400, detail="Question is too short.")

    try:
        state = graph.invoke({"question": req.question})

        return AskResponse(
            answer=state.get("answer", ""),
            verification=state.get(
                "verification",
                '{"supported": false, "reason": "No verification returned."}',
            ),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query failed: {e}")
