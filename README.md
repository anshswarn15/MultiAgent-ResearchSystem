# 🔬 MultiAgent-ResearchSystem

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/Orchestration-LangChain-emerald.svg)](https://www.langchain.com/)
[![Groq LLM](https://img.shields.io/badge/LLM-Groq-orange.svg)](https://groq.com/)
[![Streamlit UI](https://img.shields.io/badge/UI-Streamlit-red.svg)](https://streamlit.io/)

An open-source, autonomous **Multi-Agent Research Assistant** built with **LangChain, Groq LLMs, and Tavily**. The system deploys a swarm of specialized AI agents working collaboratively to automate web research, deep resource extraction, report synthesis, and peer audit.

---

## 🌟 Features

- 🤖 **Autonomous Multi-Agent Swarm**: Four specialized agents collaborate seamlessly (`Search Agent` → `Reader Agent` → `Writer Chain` → `Critic Chain`).
- 🔍 **Live Web Intelligence**: Real-time information gathering powered by Tavily Search API.
- 📄 **Deep Web Content Scraping**: Multi-strategy web parser using BeautifulSoup4, Trafilatura, and Readability-lxml.
- ✍️ **Intelligent Report Generation**: Structured, publication-ready research reports powered by Groq high-speed LLM inference.
- 🧐 **Automated Peer Review & Quality Audit**: Critic chain evaluates depth, accuracy, and structural completeness.
- 🎨 **Modern Glassmorphic UI**: Sleek dark-mode Streamlit dashboard with interactive prompt suggestions and tabbed deliverables.
- 🛡️ **Fault-Tolerant Error Handling**: Gracefully catches API quota and rate-limit exceptions without crashing.

---

## 🏗️ System Architecture

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Streamlit UI (app.py)                           │
│                     ResearcherAgent Pro Dashboard                      │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   Multi-Agent Execution Pipeline                       │
└───────┬──────────────────┬──────────────────┬──────────────────┬───────┘
        │                  │                  │                  │
        ▼                  ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│ 🔍 Search     │  │ 📄 Reader     │  │ ✍️ Writer     │  │ 🧐 Critic     │
│    Agent      │  │    Agent      │  │    Chain      │  │    Chain      │
└───────┬───────┘  └───────┬───────┘  └───────┬───────┘  └───────┬───────┘
        │                  │                  │                  │
        ▼                  ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│ Live Tavily   │  │ Web Scraper   │  │ Markdown      │  │ Peer Review & │
│ Web Results   │  │ Extracted Body│  │ Synthesis     │  │ Quality Score │
└───────────────┘  └───────────────┘  └───────────────┘  └───────────────┘
```

### Agent Roles & Responsibilities

| Agent / Chain | Function | Primary Tools / Engine |
| :--- | :--- | :--- |
| **🔍 Search Agent** | Discovers live web sources & authoritative URLs | Tavily Web Search API |
| **📄 Reader Agent** | Scrapes & extracts clean body text from top web sources | Trafilatura, BeautifulSoup4, Readability |
| **✍️ Writer Chain** | Synthesizes search & scraped data into a Markdown report | Groq LLM Inference |
| **🧐 Critic Chain** | Audits report for structural completeness & accuracy | Groq LLM Inference |

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python 3.11+** | Core Programming Language |
| **LangChain** | Agent Orchestration & Chain Workflows |
| **Groq API** | High-Speed LLM Inference Engine |
| **Tavily API** | Real-time AI Web Search & Source Discovery |
| **Streamlit** | Interactive Web Interface & Custom CSS Dashboard |
| **Trafilatura / BeautifulSoup4 / Readability** | Multi-Strategy Web Content Parsing & Scraping |
| **python-dotenv** | Environment Variable Management |

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/anshswarn15/MultiAgent-ResearchSystem.git
cd MultiAgent-ResearchSystem
```

### 2. Create & Activate Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate on macOS / Linux:
source venv/bin/activate

# Activate on Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of the project:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

> **Get API Keys:**
> - 🔑 **Groq Console**: [console.groq.com](https://console.groq.com/)
> - 🔑 **Tavily API**: [tavily.com](https://tavily.com/)

---

## 💡 Usage

### 🌐 Option A: Run Streamlit Web Application (Recommended)

```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

### 🖥️ Option B: Run CLI Pipeline Script

```bash
python main.py
```

---

## 📁 Repository Structure

```text
MultiAgent-ResearchSystem/
├── app.py                   # Streamlit web application & UI styling
├── main.py                  # CLI pipeline runner
├── requirements.txt         # Python package dependencies
├── README.md                # Project documentation
├── LICENSE                  # MIT License
│
└── src/
    ├── agents/
    │   └── agents.py        # Search, Reader, Writer, and Critic agent definitions
    ├── tools/
    │   └── tools.py         # Web search and multi-strategy scraping tools
    └── pipelines/
        └── pipeline.py      # Pipeline orchestration logic
```

---

## 🛡️ Error & Quota Handling

The application includes built-in exception handling for API limits or missing quota keys:
- Intercepts rate limit (`429`) & quota errors cleanly.
- Displays a user-friendly status banner without crashing the interface.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open a Pull Request or issue.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.

---

## 👨‍💻 Author & Maintainer

**Anshuk Kumar Swarnkar**
- GitHub: [@anshswarn15](https://github.com/anshswarn15)
- Repository: [MultiAgent-ResearchSystem](https://github.com/anshswarn15/MultiAgent-ResearchSystem)
