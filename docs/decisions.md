# Decision Records

Architecture decisions for this project. Newest at the bottom.
Format: ADR-lite (context / options / decision / consequences)
Decisions are never deleted. Superseded ones are marked and kept

---

## ADR-001 - No RAG framework in the core
**Date:** 15-07-2026 - **Status:** accepted

**Context.** LangChain and LlamaIndex would speed up the first prototype, but this project's goal is to understand every layer
of a RAG pipeline, not to ship fast.

**Options.**
- (a) LangChain: fastest to a demo, hides retrieval and prompting internals.
- (b) LlamaIndex: strong ingestion abstractions, same opacity problem.
- (c) Plain Python + minimal dependencies: slower, full control, every component explainable line by line.

**Decision.** (c). Frameworks are allowed later for peripheral tooling, never in `src/rag/`.

**Consequences.** More code to write in M1-M3. Chunking, RRF fusion and the eval metrics are implemented by hand, which is precisely the material the portfolio needs to show.