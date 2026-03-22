\# System Architecture

\## Overview

The Enterprise RAG Agents application is a Generative AI–based enterprise document query system that combines document ingestion, semantic retrieval, answer generation, and agent-based verification.

The system enables users to upload enterprise documents and ask natural language questions about their contents. Responses are generated using Retrieval-Augmented Generation (RAG), where answers are grounded in retrieved document chunks rather than relying solely on the language model’s parametric knowledge.

\## High-Level Architecture

```text

&nbsp;               ┌───────────────────── ┐

&nbsp;               │   Streamlit UI      	│

&nbsp;               │ Upload + Chat        │

&nbsp;               └─────────┬─────────── ┘

&nbsp;                         │

&nbsp;                         ▼

&nbsp;                ┌─────────────────┐

&nbsp;                │ FastAPI Backend │

&nbsp;                │ /upload /ask    │

&nbsp;                └───────┬─────────┘

&nbsp;                        │

&nbsp;          ┌──────────  ─┼─────────────┐

&nbsp;          ▼                           ▼

&nbsp; Document Ingestion            Question Query

&nbsp;PDF/TXT/CSV/XLSX               Natural Language

&nbsp;          │                           │

&nbsp;          ▼                           ▼

&nbsp;     Chunking                   Vector Search

&nbsp;          │                           │

&nbsp;          ▼                           ▼

&nbsp;   Gemini Embeddings           ChromaDB Retrieval

&nbsp;          │                           │

&nbsp;          └─────────────┬─────────────┘

&nbsp;                        ▼

&nbsp;                 Gemini LLM

&nbsp;                (Answer Agent)

&nbsp;                        │

&nbsp;                        ▼

&nbsp;                Verifier Agent

&nbsp;                        │

&nbsp;                        ▼

&nbsp;                   Response

```
