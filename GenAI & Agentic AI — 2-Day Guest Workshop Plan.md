# GenAI & Agentic AI — 2-Day Guest Workshop Plan

Nov 9, 2026 · @Amit Naik

A 2-day hands-on workshop: Day 1 covers Generative AI, Day 2 covers Agentic AI, and students leave with a working campus helpdesk agent.

The offer was originally for cloud computing, so confirm the switch with the college. If they need some cloud coverage, frame it as "GenAI and Agentic AI on Cloud" and keep one deployment session (session 9).

## Day 1: Generative AI

Day 1 takes students from how LLMs work to a working RAG chatbot.

| # | Session | Time | Topics | Lab |
| --- | --- | --- | --- | --- |
| 1 | How LLMs work | 1 hr | ML to deep learning to transformers (no heavy math); tokens, embeddings, context window, temperature, why LLMs hallucinate; open vs closed models (GPT, Claude, Gemini, Llama, Mistral) and how to choose | — |
| 2 | Prompt engineering | 1 hr | Zero-shot, few-shot, chain-of-thought, system prompts; structured output (JSON) for apps | Same feature with weak vs strong prompts, compared |
| 3 | Building with LLM APIs | 1 hr | Calling a model from Python, streaming, cost per token | Simple chatbot with conversation memory |
| 4 | RAG | 2 hrs | Embeddings, chunking, vector databases (Chroma, FAISS or managed); pipeline: ingest → chunk → embed → retrieve → answer with citations | Chat with the college syllabus or placement FAQs |
| 5 | Responsible AI | 30 min | Hallucination, bias, privacy, prompt injection, guardrails | — |

## Day 2: Agentic AI

Day 2 turns the Day 1 RAG bot into an agent that uses tools and can be deployed.

| # | Session | Time | Topics | Lab |
| --- | --- | --- | --- | --- |
| 6 | From chatbots to agents | 1 hr | What makes an agent: reasoning, tools, memory, actions; ReAct loop; workflows vs agents (when not to use an agent) | — |
| 7 | Tool calling and MCP | 1.5 hrs | Function calling step by step; Model Context Protocol and why it is becoming the standard for connecting tools | Agent calling a weather or timetable API, then the same tool as an MCP server |
| 8 | Agent frameworks and multi-agent systems | 1.5 hrs | LangGraph, CrewAI, OpenAI/Claude agent SDKs compared; orchestrator-worker, planner-executor, human-in-the-loop | Small research agent team (researcher + writer) |
| 9 | Taking agents to production | 1 hr | Evaluation, tracing and observability, cost and latency, safety and permissions; deploying as an API (serverless or container) | — |
| 10 | Mini project and careers | 1 hr | Extend the Day 1 RAG bot into a campus helpdesk agent with one tool; GenAI engineer, AI engineer, forward deployed engineer roles; what to learn next, portfolio ideas | Campus helpdesk agent |

## Practical tips

- Use Google Colab and a free or low-cost API (Gemini free tier or Groq) so students need no setup or credit card. Keep a backup API key in case of rate limits.
- Put all lab notebooks in a GitHub repo before the workshop so students can take them home.
- Adjust depth by year: for 2nd-year students, spend more time on prompting and RAG; for final-year or MCA students, go deeper into agents and MCP.

* [ ] Confirm the topic switch with the college
* [ ] Confirm student year and lab setup (laptops, internet, accounts)
* [ ] Publish lab notebooks to GitHub
