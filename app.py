import streamlit as st
import time
from src.agents.agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchAgent AI | Autonomous Multi-Agent Workspace",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap');

/* ── Global Reset & Variables ── */
:root {
    --bg-main: #060b13;
    --bg-card: rgba(15, 23, 42, 0.65);
    --bg-card-hover: rgba(30, 41, 59, 0.75);
    --border-cyan: rgba(56, 189, 248, 0.25);
    --border-purple: rgba(168, 85, 247, 0.25);
    --cyan-glow: rgba(56, 189, 248, 0.4);
    --purple-glow: rgba(168, 85, 247, 0.4);
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--text-primary);
}

.stApp {
    background-color: var(--bg-main);
    background-image: 
        radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 0%, rgba(168, 85, 247, 0.12) 0px, transparent 50%),
        radial-gradient(at 50% 100%, rgba(16, 185, 129, 0.08) 0px, transparent 50%),
        linear-gradient(180deg, #060b13 0%, #0b1329 100%);
    background-attachment: fixed;
}

/* ── Hide Streamlit Elements ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 2.5rem 3rem 4rem !important;
    max-width: 1280px;
}

/* ── Hero Section ── */
.hero-container {
    text-align: center;
    padding: 2.5rem 1rem 2rem;
    position: relative;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 9999px;
    padding: 0.35rem 1.1rem;
    font-family: 'Fira Code', monospace;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.15em;
    color: #38bdf8;
    text-transform: uppercase;
    margin-bottom: 1.25rem;
    box-shadow: 0 0 20px rgba(56, 189, 248, 0.15);
}

.hero-badge-pulse {
    width: 7px;
    height: 7px;
    background-color: #38bdf8;
    border-radius: 50%;
    box-shadow: 0 0 10px #38bdf8;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(56, 189, 248, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(56, 189, 248, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(56, 189, 248, 0); }
}

.hero-title {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(2.8rem, 5.5vw, 4.8rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.03em;
    color: #ffffff;
    margin: 0 0 1.2rem;
}

.hero-title-gradient {
    background: linear-gradient(135deg, #38bdf8 0%, #8b5cf6 50%, #ec4899 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-desc {
    font-size: 1.1rem;
    font-weight: 400;
    color: var(--text-secondary);
    max-width: 650px;
    margin: 0 auto;
    line-height: 1.65;
    text-align: center !important;
}

/* ── Top Feature Bar ── */
.agent-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 2rem 0;
}

.agent-mini-card {
    background: rgba(15, 23, 42, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 14px;
    padding: 0.9rem 1.1rem;
    display: flex;
    align-items: center;
    gap: 0.8rem;
    backdrop-filter: blur(10px);
    transition: all 0.2s ease;
}
.agent-mini-card:hover {
    border-color: rgba(56, 189, 248, 0.3);
    background: rgba(15, 23, 42, 0.7);
    transform: translateY(-2px);
}

.agent-icon {
    font-size: 1.3rem;
    background: rgba(255, 255, 255, 0.05);
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.08);
}

.agent-name {
    font-family: 'Outfit', sans-serif;
    font-weight: 600;
    font-size: 0.88rem;
    color: #f8fafc;
}
.agent-role {
    font-size: 0.73rem;
    color: var(--text-muted);
}

/* ── Divider ── */
.glowing-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.3), rgba(168, 85, 247, 0.3), transparent);
    margin: 2rem 0 2.5rem;
}

/* ── Card Containers ── */
.glass-card {
    background: var(--bg-card);
    border: 1px solid var(--border-cyan);
    border-radius: 20px;
    padding: 2rem;
    backdrop-filter: blur(16px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.35);
}

/* ── Input Styling ── */
.stTextInput > div > div > input {
    background: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid rgba(56, 189, 248, 0.3) !important;
    border-radius: 12px !important;
    color: #ffffff !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.85rem 1.1rem !important;
    transition: all 0.25s ease !important;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.4) !important;
}
.stTextInput > div > div > input:focus {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.18), inset 0 2px 4px rgba(0,0,0,0.4) !important;
}
.stTextInput > label {
    font-family: 'Fira Code', monospace !important;
    font-size: 0.76rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: #38bdf8 !important;
    font-weight: 500 !important;
    margin-bottom: 0.6rem !important;
}

/* ── Button Styling ── */
.stButton > button {
    background: linear-gradient(135deg, #0284c7 0%, #38bdf8 50%, #8b5cf6 100%) !important;
    background-size: 200% 200% !important;
    color: #ffffff !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    letter-spacing: 0.03em !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.85rem 2rem !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 6px 20px rgba(56, 189, 248, 0.25) !important;
    width: 100%;
}
.stButton > button:hover {
    background-position: 100% 0 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 28px rgba(56, 189, 248, 0.4) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Pipeline Steps ── */
.section-title {
    font-family: 'Outfit', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 1.25rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}

.step-card {
    background: rgba(15, 23, 42, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 14px;
    padding: 1.15rem 1.4rem;
    margin-bottom: 0.9rem;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    backdrop-filter: blur(12px);
}
.step-card:hover {
    border-color: rgba(56, 189, 248, 0.2);
    transform: translateX(3px);
}
.step-card.active {
    border-color: rgba(56, 189, 248, 0.5);
    background: rgba(56, 189, 248, 0.08);
    box-shadow: 0 0 20px rgba(56, 189, 248, 0.12);
}
.step-card.done {
    border-color: rgba(34, 197, 94, 0.35);
    background: rgba(34, 197, 94, 0.06);
}
.step-card::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 4px;
    background: rgba(255, 255, 255, 0.08);
    transition: background 0.3s;
}
.step-card.active::before { background: #38bdf8; box-shadow: 0 0 10px #38bdf8; }
.step-card.done::before   { background: #22c55e; box-shadow: 0 0 10px #22c55e; }

.step-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}
.step-num {
    font-family: 'Fira Code', monospace;
    font-size: 0.7rem;
    font-weight: 500;
    color: #38bdf8;
    background: rgba(56, 189, 248, 0.12);
    padding: 0.2rem 0.5rem;
    border-radius: 6px;
    border: 1px solid rgba(56, 189, 248, 0.2);
}
.step-title {
    font-family: 'Outfit', sans-serif;
    font-size: 0.98rem;
    font-weight: 600;
    color: #f8fafc;
}
.step-status {
    margin-left: auto;
    font-family: 'Fira Code', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.05em;
    padding: 0.2rem 0.6rem;
    border-radius: 9999px;
}
.status-waiting  { color: #64748b; background: rgba(100, 116, 139, 0.1); }
.status-running  { color: #38bdf8; background: rgba(56, 189, 248, 0.15); animation: pulse 1.5s infinite; }
.status-done     { color: #22c55e; background: rgba(34, 197, 94, 0.15); }

/* ── Result Cards ── */
.report-card {
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 20px;
    padding: 2.2rem 2.5rem;
    margin-top: 1.5rem;
    backdrop-filter: blur(16px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
}
.report-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 1rem;
    margin-bottom: 1.5rem;
    border-bottom: 1px solid rgba(56, 189, 248, 0.2);
}
.report-tag {
    font-family: 'Fira Code', monospace;
    font-size: 0.78rem;
    font-weight: 500;
    color: #38bdf8;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.feedback-card {
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(34, 197, 94, 0.3);
    border-radius: 20px;
    padding: 2rem 2.5rem;
    margin-top: 1.5rem;
    backdrop-filter: blur(16px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
}
.feedback-header {
    padding-bottom: 0.9rem;
    margin-bottom: 1.2rem;
    border-bottom: 1px solid rgba(34, 197, 94, 0.2);
    font-family: 'Fira Code', monospace;
    font-size: 0.78rem;
    font-weight: 500;
    color: #22c55e;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* ── Sample Chips / Suggestion Buttons Override ── */
.stButton[key^="chip_"] > button {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    color: #cbd5e1 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.8rem !important;
    font-weight: 400 !important;
    padding: 0.4rem 0.9rem !important;
    border-radius: 8px !important;
    box-shadow: none !important;
    transition: all 0.2s ease !important;
}
.stButton[key^="chip_"] > button:hover {
    background: rgba(56, 189, 248, 0.12) !important;
    border-color: rgba(56, 189, 248, 0.4) !important;
    color: #38bdf8 !important;
    transform: translateY(-1px) !important;
}

/* ── Footer Notice ── */
.footer-notice {
    font-family: 'Fira Code', monospace;
    font-size: 0.75rem;
    color: var(--text-muted);
    text-align: center;
    margin-top: 4rem;
    letter-spacing: 0.05em;
    padding-top: 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
}
</style>
""", unsafe_allow_html=True)

# ── Session state init ────────────────────────────────────────────────────────
for key in ("results", "running", "done", "topic_input", "api_error"):
    if key not in st.session_state:
        if key == "results":
            st.session_state[key] = {}
        elif key in ("topic_input", "api_error"):
            st.session_state[key] = "" if key == "topic_input" else None
        else:
            st.session_state[key] = False


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">
        <span class="hero-badge-pulse"></span>
        Multi-Agent Intelligence System
    </div>
    <h1 class="hero-title">Research<span class="hero-title-gradient">Agent</span></h1>
    <p class="hero-desc" style="text-align: center !important;">
        Deploy a swarm of autonomous AI agents working in harmony to investigate, scrape deep content, synthesize research, and critically audit reports.
    </p>
</div>

<div class="agent-grid">
    <div class="agent-mini-card">
        <div class="agent-icon">🔍</div>
        <div>
            <div class="agent-name">Search Agent</div>
            <div class="agent-role">Live Web Intelligence</div>
        </div>
    </div>
    <div class="agent-mini-card">
        <div class="agent-icon">📄</div>
        <div>
            <div class="agent-name">Reader Agent</div>
            <div class="agent-role">Deep Resource Scraping</div>
        </div>
    </div>
    <div class="agent-mini-card">
        <div class="agent-icon">✍️</div>
        <div>
            <div class="agent-name">Writer Chain</div>
            <div class="agent-role">Synthesis & Drafting</div>
        </div>
    </div>
    <div class="agent-mini-card">
        <div class="agent-icon">🧐</div>
        <div>
            <div class="agent-name">Critic Chain</div>
            <div class="agent-role">Audit & Quality Scoring</div>
        </div>
    </div>
</div>

<div class="glowing-divider"></div>
""", unsafe_allow_html=True)


# ── Layout: Input Column vs Pipeline Progress ──────────────────────────────────
col_input, col_spacer, col_pipeline = st.columns([5, 0.4, 4.6])

with col_input:
    st.markdown('<div class="section-title"><span>🎯</span> Define Research Task</div>', unsafe_allow_html=True)
    
    topic = st.text_input(
        "Research Topic or Question",
        placeholder="e.g. Roadmap for AGI development in next 5 years",
        key="topic_input",
        label_visibility="visible",
    )

    run_btn = st.button(
        "🚀 Launch Agent Pipeline",
        use_container_width=True
    )

    # Interactive Prompt Suggestions
    st.markdown("""
    <div style="margin-top: 1.5rem; margin-bottom: 0.4rem; font-family: 'Fira Code', monospace; font-size: 0.7rem; color: #64748b; letter-spacing: 0.1em; text-transform: uppercase;">
        ⚡ Recommended Prompts
    </div>
    """, unsafe_allow_html=True)

    examples = [
        "Future of LLM architectures & reasoning agents",
        "Autonomous AI Agent Frameworks 2026 Comparison",
        "Roadmap for AGI development in next 5 years",
    ]

    def set_topic(val):
        st.session_state.topic_input = val

    chip_cols = st.columns(len(examples))
    for idx, (col, ex) in enumerate(zip(chip_cols, examples)):
        with col:
            st.button(ex, key=f"chip_{idx}", on_click=set_topic, args=(ex,))

with col_pipeline:
    st.markdown('<div class="section-title"><span>⚡</span> Agent Execution Flow</div>', unsafe_allow_html=True)

    r = st.session_state.results

    def s(step):
        if not r and not st.session_state.running:
            return "waiting"
        steps = ["search", "reader", "writer", "critic"]
        if step in r:
            return "done"
        if st.session_state.running:
            for k in steps:
                if k not in r:
                    return "running" if k == step else "waiting"
        return "waiting"

    def step_card(num: str, title: str, state: str, desc: str = ""):
        status_map = {
            "waiting": ("WAITING", "status-waiting"),
            "running": ("● ACTIVE", "status-running"),
            "done":    ("✓ COMPLETED", "status-done"),
        }
        label, cls = status_map.get(state, ("", ""))
        card_cls = {"running": "active", "done": "done"}.get(state, "")

        st.markdown(f"""
        <div class="step-card {card_cls}">
            <div class="step-header">
                <span class="step-num">{num}</span>
                <span class="step-title">{title}</span>
                <span class="step-status {cls}">{label}</span>
            </div>
            {"<div style='font-size:0.8rem; color:#94a3b8; margin-top:0.4rem; padding-left:0.1rem;'>"+desc+"</div>" if desc else ""}
        </div>
        """, unsafe_allow_html=True)

    step_card("01", "Search Agent", s("search"), "Queries web search engines for up-to-date sources")
    step_card("02", "Reader Agent", s("reader"), "Parses & extracts detailed textual content from URLs")
    step_card("03", "Writer Chain", s("writer"), "Synthesizes gathered intelligence into structured report")
    step_card("04", "Critic Chain", s("critic"), "Audits report for accuracy, depth, and structural quality")


# ── Pipeline Run Trigger & Handler ─────────────────────────────────────────────
if run_btn:
    if not topic.strip():
        st.warning("⚠️ Please enter a research topic before starting the pipeline.")
    else:
        st.session_state.results = {}
        st.session_state.running = True
        st.session_state.done = False
        st.session_state.api_error = None
        st.rerun()

if st.session_state.get("api_error"):
    st.markdown(f"""
    <div style="
        background: rgba(239, 68, 68, 0.12);
        border: 1px solid rgba(239, 68, 68, 0.4);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 1.5rem 0;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 25px rgba(239, 68, 68, 0.15);
        display: flex;
        align-items: center;
        gap: 1.2rem;
    ">
        <div style="font-size: 2rem;">⚠️</div>
        <div>
            <div style="font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 1.1rem; color: #fca5a5; margin-bottom: 0.3rem;">
                API Limit Reached / Quota Exceeded
            </div>
            <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 0.95rem; color: #fecaca;">
                Contact owner/developer of this application: <strong style="color: #ffffff; text-decoration: underline;">Anshuk Kumar Swarnkar</strong>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.running and not st.session_state.done:
    results = {}
    topic_val = st.session_state.topic_input
    st.session_state.api_error = None

    try:
        # Step 1: Search
        with st.spinner("🔍 Search Agent is querying live sources…"):
            search_agent = build_search_agent()
            sr = search_agent.invoke({
                "messages": [("user", f"Find recent, reliable and detailed information about: {topic_val}")]
            })
            results["search"] = sr["messages"][-1].content
            st.session_state.results = dict(results)

        # Step 2: Reader
        with st.spinner("📄 Reader Agent is extracting article body…"):
            reader_agent = build_reader_agent()
            rr = reader_agent.invoke({
                "messages": [(
                    "user",
                    f"Based on the following search results about '{topic_val}', "
                    f"pick the most relevant URL and scrape it for deeper content.\n\n"
                    f"Search Results:\n{results['search'][:800]}"
                )]
            })
            results["reader"] = rr["messages"][-1].content
            st.session_state.results = dict(results)

        # Step 3: Writer
        with st.spinner("✍️ Writer Chain is drafting research document…"):
            research_combined = (
                f"SEARCH RESULTS:\n{results['search']}\n\n"
                f"DETAILED SCRAPED CONTENT:\n{results['reader']}"
            )
            results["writer"] = writer_chain.invoke({
                "topic": topic_val,
                "research": research_combined
            })
            st.session_state.results = dict(results)

        # Step 4: Critic
        with st.spinner("🧐 Critic Chain is evaluating quality and accuracy…"):
            results["critic"] = critic_chain.invoke({
                "report": results["writer"]
            })
            st.session_state.results = dict(results)

        st.session_state.running = False
        st.session_state.done = True
        st.rerun()

    except Exception as e:
        st.session_state.running = False
        st.session_state.done = False
        st.session_state.api_error = (
            "API limit reached! Iss application ke owner se contact kro: **Anshuk Kumar Swarnkar**"
        )
        st.rerun()


# ── Results & Final Output Section ─────────────────────────────────────────────
r = st.session_state.results

if r:
    st.markdown('<div class="glowing-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title"><span>📊</span> Pipeline Intelligence & Reports</div>', unsafe_allow_html=True)

    # Tabs for raw data & final outputs
    tab_report, tab_critic, tab_raw = st.tabs(["📝 Final Research Report", "🧐 Critic Audit", "🔍 Raw Agent Logs"])

    with tab_report:
        if "writer" in r:
            word_count = len(r["writer"].split())
            st.markdown(f"""
            <div class="report-card">
                <div class="report-header">
                    <div class="report-tag">
                        <span>📝</span> Research Deliverable
                    </div>
                    <div style="font-family: 'Fira Code', monospace; font-size: 0.75rem; color: #64748b;">
                        {word_count} words
                    </div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown(r["writer"])
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.download_button(
                label="📥 Export Report as Markdown (.md)",
                data=r["writer"],
                file_name=f"ResearchReport_{int(time.time())}.md",
                mime="text/markdown",
                use_container_width=True
            )

    with tab_critic:
        if "critic" in r:
            st.markdown("""
            <div class="feedback-card">
                <div class="feedback-header">
                    <span>🧐</span> Critic Evaluation & Peer Review
                </div>
            """, unsafe_allow_html=True)

            st.markdown(r["critic"])
            st.markdown("</div>", unsafe_allow_html=True)

    with tab_raw:
        col_s, col_r = st.columns(2)
        with col_s:
            if "search" in r:
                with st.expander("🔍 Search Agent Raw Telemetry", expanded=True):
                    st.text_area("Search Logs", value=r["search"], height=300, disabled=True)
        with col_r:
            if "reader" in r:
                with st.expander("📄 Reader Agent Raw Telemetry", expanded=True):
                    st.text_area("Scrape Logs", value=r["reader"], height=300, disabled=True)


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-notice">
    RESEARCHAGENT PRO · MULTI-AGENT SWARM ARCHITECTURE · BUILT WITH LANGCHAIN & STREAMLIT
</div>
""", unsafe_allow_html=True)