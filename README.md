\# Enterprise RAG Agents



A Generative AI–powered enterprise document question-answering system built with Gemini, Retrieval-Augmented Generation (RAG), ChromaDB, FastAPI, LangChain, LangGraph, and Streamlit.



\## Overview



This project allows users to upload enterprise documents in multiple formats and ask natural language questions about their contents. The system processes uploaded documents, converts them into semantic embeddings, stores them in a vector database, retrieves relevant chunks for a given query, and generates grounded answers using Google Gemini.



An agent-based workflow coordinates retrieval, answer generation, and verification to improve reliability and reduce hallucinations.



\## Features



\- Upload documents in PDF, TXT, CSV, XLSX, and XLS formats

\- Semantic chunking and embedding generation

\- Vector similarity search using ChromaDB

\- Retrieval-Augmented Generation with Gemini

\- Agent-based reasoning workflow using LangGraph

\- Verification step for answer support

\- Streamlit frontend for user interaction

\- FastAPI backend with documented API endpoints



\## Technology Stack



\- \*\*User Interface:\*\* Streamlit

\- \*\*Backend API:\*\* FastAPI

\- \*\*LLM:\*\* Google Gemini

\- \*\*Embeddings:\*\* Gemini Embedding Model

\- \*\*Vector Database:\*\* ChromaDB

\- \*\*RAG Framework:\*\* LangChain

\- \*\*Agent Workflow:\*\* LangGraph

\- \*\*Programming Language:\*\* Python



\## Project Structure



```text

enterprise-rag-agents/

│

├── README.md

├── .gitignore

├── Dockerfile

├── requirements.txt

├── .env.example

├── ui\_streamlit.py

│

├── docs/

│   ├── ARCHITECTURE.md

│   └── LIMITATIONS.md

│

├── app/

│   ├── main.py

│   ├── config.py

│   ├── schemas.py

│   │

│   ├── ingestion/

│   │   ├── loaders.py

│   │   ├── chunking.py

│   │   └── indexer.py

│   │

│   ├── rag/

│   │   ├── vectorstore.py

│   │   ├── retriever.py

│   │   └── generator.py

│   │

│   ├── agents/

│   │   ├── graph.py

│   │   ├── tools.py

│   │   └── verifier.py

│   │

│   └── safety/

│       └── guardrails.py

│

└── data/

&nbsp;   ├── uploads/

&nbsp;   └── chroma/

