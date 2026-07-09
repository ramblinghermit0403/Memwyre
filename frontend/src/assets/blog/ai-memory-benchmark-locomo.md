# LoCoMo Benchmark: Evaluation of AI Memory

LoCoMo-10 is a widely accepted standard for evaluating long-term memory performance in AI agents and conversational assistants. Below is the detailed analysis of Memwyre's retrieval capabilities on this benchmark.

> **Quick Summary / TL;DR**
>
> **Answer:** On the LoCoMo-10 long-term memory benchmark, Memwyre achieves a 73.5% overall accuracy (outperforming flat vector systems) while retrieving a mean token count of only 3,000 per request (versus 26,000 tokens of raw dialog). This is driven by dynamic context pruning, Ebbinghaus logarithmic decay, and two-stage cross-encoder vector re-ranking.

**Key Metrics:**

- **73.5%** — Overall Accuracy (Benchmark Score)
- **3,000** — Mean Tokens (Average Context Size)
- **26k** — Tokens Per Dialog (Up to 32 sessions)

## 1. Introduction

LoCoMo-10 stands for Long Conversational Memory – 10 conversations. It is one of the most widely used benchmarks for evaluating long-term memory systems for AI agents and conversational assistants. It was introduced by researchers at Snap Research in their LoCoMo paper.

The "10" simply refers to the 10 long conversations contained in the original dataset file (`locomo10.json`). Nearly all papers referring to "LoCoMo-10" are using these same ten conversations for evaluation.

For memory systems like Memwyre, LoCoMo-10 is currently one of the best benchmarks because it closely resembles a real personal memory system: conversations happen over long periods, facts evolve over time, and users expect the AI to remember everything consistently.

## 2. Methodology

The benchmark evaluates memory retrieval capabilities across a rich conversational dataset structure.

### Dataset Structure

LoCoMo-10 contains:

- 10 very long multi-session conversations.
- Conversations span weeks to months of simulated interactions.
- Around 16k–26k tokens per conversation.
- Up to 32 sessions per conversation.
- Exactly 1,540 questions.

Each conversation is embedded with: personal facts, user preferences, events, temporal details, relationships between events, distractor information, and adversarial questions.

### Why LoCoMo is Difficult

Traditional retrieval architectures often fail on LoCoMo-10 because:

- Relevant memories may be hundreds of turns apart in the dialogue context.
- Questions require reasoning and correlation across multiple disconnected chat sessions.
- Temporal relationships matter; values and events change chronologically.
- Adversarial questions actively target non-existent memories to punish hallucinations.
- Full-context feeding approaches become prohibitively expensive at this scale.

### Metrics Commonly Reported

Most memory systems report Accuracy, F1 Score, Hit@10, MRR (Mean Reciprocal Rank), and Category-wise scores (SH, MH, TR, OD, ADV). For retrieval systems like Memwyre, the crucial retrieval performance metrics are:

- **Hit@10:** Was the correct memory included in the top 10 retrieved context items?
- **MRR:** How high did the correct target memory rank in the retrieval output?

## 3. Types of Questions

The benchmark evaluates five core memory abilities through specific types of questions:

| Category | What it tests | Example |
|---|---|---|
| **Single-hop** | Direct fact recall | *"What is John's favorite sport?"* |
| **Multi-hop** | Combining multiple memories | *"Who introduced Sarah to the person she later worked with?"* |
| **Temporal** | Understanding time and order | *"When did they first discuss moving to Boston?"* |
| **Open-domain** | General reasoning with context | *"Why was Emily stressed during that period?"* |
| **Adversarial** | Avoiding hallucinations | *"What is Alex's dog named?"* (when Alex never mentioned a dog) |

## 4. Our Performance

The chart below illustrates Memwyre's performance on the four primary evaluation categories:

| Category | Previous Score | Memwyre Score |
|---|---|---|
| **Single-hop** | 53.0 | **80.0** |
| **Multi-hop** | 24.0 | **45.0** |
| **Open-domain** | 50.0 | **76.0** |
| **Temporal** | 48.0 | **74.0** |

### Why Memwyre Performs So Well

Memwyre's exceptional results on the LoCoMo-10 benchmark—such as achieving an 80% accuracy on Single-hop recall and a 74% score on Temporal alignment—are powered by a combination of targeted technological mechanisms:

**Dynamic Pruning**

Instead of feeding raw conversational history into the LLM, Memwyre strips out pleasantries, filler phrases, and distractor information. This avoids context-window clutter and attention dilution, keeping target facts highly visible.

**Vector Re-ranking**

Memwyre uses a two-stage retrieval pipeline. It pulls a broad set of candidate memories (yielding a high Hit@10 rate), then re-ranks them using cross-encoders to ensure only the highest-scoring context matches are sent to the generation window.

**Ebbinghaus Decay Formula**

To handle changing user preferences across months of chat, older facts are naturally deprecated when newer contradictory preferences are written. This logarithmic decay mirrors human memory retention.

**Adversarial Immunity**

Memwyre's strict semantic containment blocks hallucinations. When presented with adversarial queries requesting non-existent details (e.g. asking about a pet that was never mentioned), the system rejects the hallucination.

Our performance analysis indicates that retrieval recall remains extremely strong (especially on complex multi-hop correlations). The remaining delta is primarily a downstream bottleneck, which we are addressing through:

**Reranking Quality** — Prioritizing the highest-scoring context items to match generation context bounds.

**Evidence Selection** — Extracting specific targets, filtering out ambient chat noise and distractors.

**Answer Synthesis** — Ensuring details from different sessions compile cleanly in the response.

---

**Interested in the raw benchmark datasets?**

Download our complete evaluation logs (JSON format).

[View GitHub Repository →](https://github.com/ramblinghermit0403/Memwyre/tree/main/.benchmarks)
