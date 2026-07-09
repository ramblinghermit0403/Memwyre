---
title: Memwyre Latency & Performance Benchmarks
description: Read the performance and latency benchmark report comparing Memwyre's retrieval with Mem0, Zep, and Supermemory.
---
# Performance & Recall Benchmarks

To evaluate the efficiency of Memwyre's context retrieval, we benchmark our engine against standard Retrieval-Augmented Generation (RAG) setups on the **LoCoMo benchmark dataset**. 

The evaluation consists of **1,540 test questions** spanning **5 distinct context categories**, measuring both accuracy and the compactness of the generated context.

---

## Core Metrics

Memwyre maintains a high recall rate while drastically reducing the number of tokens fed into the LLM context window:

* **Overall Accuracy**: **73.5%** average score across all categories.
* **Mean Context Size**: **3,000 tokens**. By utilizing dynamic context pruning and re-ranking, Memwyre avoids bloating prompts with entire raw documents, saving costs and latency.

---

## Category Breakdown

<LocomoChart />

| Retrieval Category | Standard RAG | Memwyre | Improvement |
| :--- | :---: | :---: | :---: |
| **Single-hop Retrieval** <br> (Direct facts and simple lookups) | 53.0% | **80.0%** | **+27.0%** |
| **Multi-hop Retrieval** <br> (Connecting links across disparate facts) | 24.0% | **45.0%** | **+21.0%** |
| **Open-domain Retrieval** <br> (Broad topics and semantic themes) | 50.0% | **76.0%** | **+26.0%** |
| **Temporal Retrieval** <br> (Time-sensitive facts and recent updates) | 48.0% | **74.0%** | **+26.0%** |

---

## Evaluation Setup

To ensure an objective, standardized comparison, these benchmarks were run under the following configuration:

* **Evaluation Framework**: **MemoryBench**, an open-source evaluation harness for comparing AI memory providers.
* **Answering Model**: `gpt-4o-mini` (generating answers based on retrieved context).
* **Judge Model**: `gpt-4o-mini` (using a standardized LLM-as-a-judge grading rubric to evaluate response correctness).

---

## Key Performance Drivers

The performance differences are driven by three core optimizations in Memwyre's retrieval pipeline:

1. **Deterministic Entity Filtering**: Instead of relying solely on fuzzy semantic vector matches, Memwyre matches the specific entities mentioned in your prompt to direct facts in your memory graph. This drastically boosts accuracy in **Single-hop** and **Multi-hop** tasks.
2. **Dynamic Context Pruning**: Rather than loading whole pages or files, Memwyre only retrieves active, high-priority snippets. This keeps the mean context size down to **3,000 tokens** while preserving high recall.
3. **Temporal Recency Boost**: In **Temporal** tasks, Memwyre applies a decay factor to older facts, ensuring that when facts update (e.g. changing configuration keys or codebases), the LLM receives the latest active guidelines.
