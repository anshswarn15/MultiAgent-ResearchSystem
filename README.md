# 🔬 LangChain Multi-Agent Research System

An AI-powered research assistant built with **LangChain, Groq, and Tavily** that automates the research workflow — from web search and content extraction to report generation and AI-based evaluation.

## ✨ Features

- 🤖 **Multi-Agent Research** — Specialized agents for different research tasks
- 🔎 **Web Search** — Real-time information retrieval using Tavily
- 🌐 **Web Scraping** — Extracts useful content from webpages
- 📝 **Report Generation** — Creates structured research reports using Groq-powered LLMs
- 🧐 **AI Critic** — Reviews generated reports and provides quality scores
- ⚡ **Fast Inference** — Uses Groq for high-speed LLM inference
- 🎨 **Streamlit UI** — Simple interface for interacting with the research system
- 🔗 **LangChain Workflow** — Modular agent and pipeline architecture

---

## 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │    Streamlit UI     │
                         │       app.py        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Research Pipeline │
                         │    pipeline.py      │
                         └──────────┬──────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
             ▼                      ▼                      ▼
      ┌─────────────┐        ┌─────────────┐        ┌─────────────┐
      │Search Agent │        │Reader Agent │        │Writer Chain │
      └──────┬──────┘        └──────┬──────┘        └──────┬──────┘
             │                      │                      │
             └──────────────────────┼──────────────────────┘
                                    │
                                    ▼
                            ┌───────────────┐
                            │ Critic Chain  │
                            └───────┬───────┘
                                    │
                                    ▼
                         Report + Evaluation
