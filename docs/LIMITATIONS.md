

---



\## `docs/LIMITATIONS.md`



```md

\# Limitations



\## Overview



While the Enterprise RAG Agents application successfully demonstrates a complete Generative AI and agentic RAG workflow, it has several practical limitations that should be acknowledged.



\## 1. Dependency on External API Services



The system depends on the Google Gemini API for both text generation and embeddings. As a result, application performance and availability are influenced by:

\- API quota limits

\- rate limits

\- account permissions

\- internet connectivity

\- upstream service availability



If Gemini quotas are exhausted or access is restricted, document ingestion or question answering may fail.



\## 2. Limited Document Understanding for Complex Layouts



Although the system supports PDF, TXT, CSV, XLSX, and XLS files, extraction quality depends on the underlying file structure.



Examples of limitations include:

\- scanned PDFs without OCR

\- tables with complex formatting

\- multi-column document layouts

\- images and diagrams embedded in documents



These cases may reduce retrieval quality because the extracted text may be incomplete or poorly structured.



\## 3. Context Window Constraints



The language model can only process a limited amount of retrieved context in a single request. If relevant information is distributed across many chunks or large documents, some useful context may be omitted. This can reduce answer completeness.



\## 4. Basic Retrieval Strategy



The project currently uses semantic similarity search with a fixed `TOP\_K` retrieval setting. While effective for many queries, it does not yet include:

\- hybrid search

\- reranking

\- metadata-based filtering

\- query expansion

\- adaptive retrieval strategies



These enhancements could improve retrieval precision in more complex enterprise settings.



\## 5. Verification Is Still Model-Based



The verification step is designed to assess whether the answer is supported by the retrieved context. However, the verifier itself is also an LLM-based component, which means it is not a formal proof system. It may still produce imperfect judgments in edge cases.



\## 6. No Authentication or Role-Based Access Control



The prototype is designed for academic demonstration and does not include:

\- user authentication

\- document ownership controls

\- access permissions

\- tenant isolation



In a real enterprise environment, these features would be essential.



\## 7. Limited Conversation Memory



The current system focuses on single-turn question answering over uploaded documents. It does not maintain long-term conversational memory or advanced session-aware follow-up reasoning.



\## 8. Limited Production Hardening



The project demonstrates core functionality but does not yet include full production features such as:

\- monitoring and observability

\- audit logging

\- secret management

\- autoscaling

\- background ingestion jobs

\- retry queues

\- CI/CD integration



\## 9. Local Storage Assumptions



Uploaded files and vector data are stored locally in the `data/uploads` and `data/chroma` directories. This is sufficient for prototyping but not ideal for enterprise-scale deployment, where object storage and managed databases would be more appropriate.



\## 10. Performance Trade-Offs



The application is optimized for clarity and educational value rather than maximum throughput. For larger workloads or multiple concurrent users, performance tuning would be required.



\## Future Improvements



Potential improvements include:

\- OCR support for scanned PDFs

\- hybrid retrieval and reranking

\- better spreadsheet parsing

\- user authentication and document access control

\- managed vector database support

\- conversation memory

\- evidence display panels

\- observability and usage analytics



\## Conclusion



These limitations are typical of academic and prototype implementations of RAG systems. Despite them, the application successfully demonstrates the core concepts of enterprise document ingestion, semantic search, LLM-based answer generation, and agent-based reasoning.

