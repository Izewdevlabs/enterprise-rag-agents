from pathlib import Path
import pandas as pd
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document

SUPPORTED = {".pdf", ".txt", ".csv", ".xlsx", ".xls"}


def load_document(file_path: str) -> list[Document]:
    path = Path(file_path)
    ext = path.suffix.lower()

    if ext == ".pdf":
        return PyPDFLoader(file_path).load()

    if ext == ".txt":
        return TextLoader(file_path, encoding="utf-8").load()

    if ext == ".csv":
        df = pd.read_csv(file_path)
        text = df.to_csv(index=False)
        return [
            Document(page_content=text, metadata={"source": path.name, "type": "csv"})
        ]

    if ext in [".xlsx", ".xls"]:
        df = pd.read_excel(file_path)
        text = df.to_csv(index=False)
        return [
            Document(page_content=text, metadata={"source": path.name, "type": "excel"})
        ]

    raise ValueError(f"Unsupported file type: {ext}")
