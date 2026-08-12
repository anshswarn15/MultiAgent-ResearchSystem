
# 🔬 LangChain Multi-Agent Research System
An AI-powered research assistant built with **LangChain, Groq, and Tavily** that automates the complete research workflow — from web search and content extraction to report generation and AI-based evaluation.
<p align="center">
  <strong>🔬 Research Automation • 🤖 Multi-Agent Orchestration • 📝 Intelligent Report Generation</strong>
</p>
---
## 🌟 Features
- **Multi-Agent Architecture** — Specialized agents for searching, reading, writing, and reviewing
- **Automated Web Research** — Searches the web using Tavily
- **Smart Content Extraction** — Extracts useful content from webpages using multiple extraction strategies
- **AI-Powered Report Generation** — Generates structured research reports using Groq-powered LLMs
- **AI-Based Quality Evaluation** — Reviews generated reports and provides scores and feedback
- **Interactive UI** — Streamlit-based interface for easy interaction
- **Pipeline Orchestration** — Coordinates the complete research workflow
- **Fast LLM Inference** — Uses Groq for high-speed inference
---
## 🏗️ Architecture
```text
┌─────────────────────────────────────────────────────┐
│                  Streamlit UI                       │
│                     app.py                          │
│        Multi-Agent Research Assistant               │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│               Research Pipeline                     │
│                  pipeline.py                         │
│          Coordinates the complete workflow           │
└──────────────────────┬──────────────────────────────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
   ┌────────────┐ ┌────────────┐ ┌────────────┐
   │   Search   │ │   Reader   │ │   Writer   │
   │   Agent    │ │   Agent    │ │   Chain    │
   └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
         │              │              │
         └──────────────┼──────────────┘
                        │
                        ▼
                 ┌─────────────┐
                 │    Tools    │
                 │             │
                 │ web_search  │
                 │ scrape_url  │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │   Critic    │
                 │   Chain     │
                 └──────┬──────┘
                        │
                        ▼
             ┌──────────────────────┐
             │ Report + Evaluation  │
             └──────────────────────┘

```

### Agent Responsibilities

| Component | Responsibility |
| --- | --- |
| **Search Agent** | Discovers relevant sources using Tavily |
| **Reader Agent** | Extracts clean and useful content from webpages |
| **Writer Chain** | Generates a structured research report |
| **Critic Chain** | Evaluates the generated report and provides feedback |
| **Research Pipeline** | Coordinates the complete workflow |
| **Tools Layer** | Provides web search and webpage extraction tools |
| **Streamlit UI** | Provides the user-facing interface |

---

## 🛠️ Technologies Used

| Technology | Purpose |
| --- | --- |
| **Python** | Core programming language |
| **LangChain** | Agent orchestration and LLM workflow management |
| **Groq** | Fast LLM inference |
| **Tavily API** | Web search and information retrieval |
| **Streamlit** | Interactive web interface |
| **BeautifulSoup4** | HTML parsing and content extraction |
| **Trafilatura** | Web content extraction |
| **Readability-lxml** | Article content extraction |
| **python-dotenv** | Environment configuration |
| **Rich** | Terminal output formatting |

---

## 📋 Prerequisites

Before running the project, make sure you have:

* Python 3.11 or higher
* Groq API Key
* Tavily API Key
* Git

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone [https://github.com/yourusername/LangChain-Multi-Agent-Research-System.git](https://github.com/yourusername/LangChain-Multi-Agent-Research-System.git)
cd LangChain-Multi-Agent-Research-System

```

*(Replace `yourusername` with your GitHub username.)*

### 2. Create a Virtual Environment

**Using Conda**

```bash
conda create -n langagent python=3.11 -y
conda activate langagent

```

**Using venv**

```bash
python -m venv venv

```

**Activate the environment:**

* **macOS / Linux:** `source venv/bin/activate`
* **Windows:** `venv\Scripts\activate`

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

```

Get your API keys from:

* Groq Console
* Tavily

> ⚠️ **Never commit your `.env` file or expose your API keys publicly.**

Add the following to `.gitignore`:

```text
.env
venv/
.venv/
__pycache__/
*.pyc

```

---

## 💡 Usage

### Run with Streamlit UI

The recommended way to run the application is through Streamlit.

```bash
streamlit run app.py

```

Then open `http://localhost:8501` in your browser.

### Run as a Script

The research pipeline can also be executed directly:

```bash
python main.py

```

You can modify the `topic` variable in `main.py` to research different topics.

*Example:*

```python
topic = "Impact of Generative AI on Software Development"

```

---

## 🔄 Workflow

The system follows a sequential research pipeline:

```text
Research Topic
      │
      ▼
Search Agent
      │
      ▼
Tavily Web Search
      │
      ▼
Relevant Sources
      │
      ▼
Reader Agent
      │
      ▼
Content Extraction
      │
      ▼
Writer Chain
      │
      ▼
Research Report
      │
      ▼
Critic Chain
      │
      ▼
Quality Score + Feedback

```

1. **User Input**
The user provides a research topic through the Streamlit interface or command line.
2. **Search Phase**
The Search Agent uses Tavily to search the web and identify relevant sources.
3. **Reading Phase**
The Reader Agent processes the discovered URLs and extracts useful information using multiple strategies:

* BeautifulSoup
* Trafilatura
* Readability

4. **Writing Phase**
The Writer Chain receives the collected information and uses a Groq-powered LLM to generate a structured research report.
5. **Review Phase**
The Critic Chain evaluates the generated report checking factors such as:

* Relevance
* Completeness
* Clarity
* Structure
* Quality of information

6. **Final Output**
The final output contains the generated research report along with the critic’s evaluation and improvement suggestions.

---

## 📊 Example

Suppose the user enters:
`Applications of Artificial Intelligence in Chemical Engineering`

The system performs:

```text
                    User Input
                        │
                        ▼
                  Search Agent
                        │
                        ▼
                   Tavily API
                        │
                        ▼
                Relevant Web Sources
                        │
                        ▼
                  Reader Agent
                        │
                        ▼
                Extracted Content
                        │
                        ▼
                  Writer Chain
                        │
                        ▼
                Research Report
                        │
                        ▼
                  Critic Chain
                        │
                ┌───────┴───────┐
                ▼               ▼
          Quality Score      Feedback

```

---

## 📝 Example Output

The generated research report can contain:

* Introduction
* Background
* Key findings
* Detailed explanations
* Important insights
* Sources
* Conclusion

The Critic Chain additionally provides:

```text
Quality Score: 8/10
Feedback:
- Report is well structured
- Sources are relevant
- Some sections require additional supporting information
- Conclusion can be improved

```

---

## 📁 Project Structure

```text
LangChain-Multi-Agent-Research-System/
│
├── app.py                      # Streamlit web interface
├── main.py                     # CLI entry point
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── LICENSE                     # License file
├── demo.excalidraw             # Architecture diagram
│
└── src/
    ├── __init__.py
    ├── agents/
    │   ├── __init__.py
    │   └── agents.py           # Search, Reader, Writer and Critic components
    ├── tools/
    │   ├── __init__.py
    │   └── tools.py            # Web search and webpage scraping tools
    └── pipelines/
        ├── __init__.py
        └── pipeline.py         # Research workflow orchestration

```

---

## 🧩 Core Components

* **Search Agent:** Responsible for discovering relevant sources from the web using Tavily.
* **Reader Agent:** Responsible for extracting useful information from webpages.
* **Writer Chain:** Responsible for synthesizing the collected information into a structured research report.
* **Critic Chain:** Responsible for evaluating the generated report and providing a Quality Score, Feedback, and Improvement Suggestions.

---

## 🔧 Tools

* **web_search:** Searches the web using Tavily.
* **scrape_url:** Extracts readable content from a webpage. The scraping layer uses multiple extraction strategies to improve reliability across different website structures.

---

## ⚡ Why Groq?

This project uses Groq as the LLM inference provider.
The research workflow requires multiple LLM operations (`Search → Read → Write → Critique`). Because these operations are part of a multi-step pipeline, fast inference helps reduce the overall response time, making Groq well suited for this type of agentic workflow.

---

## 🎯 Why Multi-Agent Architecture?

Instead of relying on a single LLM call to perform the entire research task, the system divides the workflow into specialized components.

**Benefits:**

* Separation of responsibilities
* Modular architecture
* Easier debugging
* Better workflow control
* Independent component development
* Easy integration of additional tools
* More maintainable codebase

---

## 🔮 Future Improvements

* Parallel research agents
* Source credibility scoring
* Automatic citation generation
* PDF report generation
* Research history
* Human-in-the-loop review
* Additional search providers
* Automatic report refinement using critic feedback
* Persistent research memory
* Multiple LLM provider support
* Source comparison and fact verification
* Research result export
* Streaming agent responses

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Commit your changes (`git add .` then `git commit -m "Add new feature"`)
5. Push your branch (`git push origin feature/new-feature`)
6. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for more information.

---

## 🙏 Acknowledgements

This project was built using:

* LangChain — LLM and agent orchestration
* Groq — Fast LLM inference
* Tavily — Web search and research
* Streamlit — Interactive web interface
* BeautifulSoup — HTML parsing
* Trafilatura — Web content extraction
* Readability — Article extraction

---

## 👨‍💻 Author

**Anshuk Swarnkar**

Built as a project to explore:

* Multi-Agent AI Systems
* LangChain
* Groq LLMs
* Web Research Automation
* LLM-powered Report Generation
* AI-based Report Evaluation

---
