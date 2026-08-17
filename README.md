# 🕵️‍♂️ MarketSpy AI

## Autonomous Multi-Agent Competitive Intelligence Platform

> **Transforming raw competitor websites into structured financial intelligence, competitive analysis, and C-suite-ready strategic briefings — autonomously.**

<p align="center">
  <img src="assets/screenshots/dashboard.png" alt="MarketSpy AI Dashboard" width="900"/>
</p>

<p align="center">
  <strong>⚡ Async Web Reconnaissance &nbsp;•&nbsp; 🤖 Multi-Agent Intelligence &nbsp;•&nbsp; 📊 Executive Analytics</strong>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Async-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-000000?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge\&logo=postgresql\&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-LLM-4285F4?style=for-the-badge\&logo=google\&logoColor=white)

</p>

---

## 📌 Overview

**MarketSpy AI** is an asynchronous, multi-agent competitive intelligence platform designed to automate competitor research, financial data extraction, quantitative analysis, and strategic reporting.

Instead of manually browsing competitor websites, searching for pricing information, collecting financial metrics, comparing companies, and preparing executive reports, MarketSpy AI coordinates a complete AI-powered intelligence pipeline.

The system:

```text
Competitor Domains
        ↓
Async Web Reconnaissance
        ↓
Gemini Structured Extraction
        ↓
Pydantic Validation
        ↓
PostgreSQL Persistence
        ↓
CrewAI Multi-Agent Analysis
        ↓
Financial Intelligence
        ↓
Strategic Synthesis
        ↓
Executive Briefing
        ↓
Streamlit Dashboard
```

### 🚀 Project Status

**Production-Ready / Stable Version 1.0**

---

# 🎯 Why MarketSpy AI?

Competitive intelligence is often a repetitive and fragmented process.

Business analysts and product teams may spend hours:

* Browsing competitor websites
* Finding pricing pages
* Collecting financial information
* Copying data into spreadsheets
* Comparing competitors
* Identifying strategic differences
* Preparing reports for decision-makers

MarketSpy AI automates this workflow using a combination of **asynchronous Python, LLM-based extraction, database persistence, and specialized AI agents**.

---

# 🛑 The Problem

Traditional competitive research introduces three major challenges.

### 1. Unstructured Data

Competitor information is distributed across:

* HTML pages
* Pricing tables
* Product descriptions
* About pages
* Financial announcements
* Long-form company content

Manually converting this information into structured data is slow and difficult to scale.

### 2. LLM Hallucinations

Generic AI chatbots can generate impressive explanations but are not inherently reliable for structured financial analytics.

Potential issues include:

* Incorrect numbers
* Missing fields
* Inconsistent formatting
* Unstructured responses
* Difficulty generating reliable charts

### 3. Information Siloing

Quantitative information such as:

* Revenue
* Pricing
* Subscription tiers
* Pricing differences
* Financial metrics

is often stored separately from qualitative information such as:

* Competitive positioning
* Strategic risks
* Market opportunities
* Recommended actions

MarketSpy AI brings both dimensions together.

---

# 🎯 The Solution

MarketSpy AI implements a **two-phase agentic intelligence pipeline**.

```text
                 ┌──────────────────────┐
                 │  Competitor Domains   │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Async Web Spidering  │
                 │   HTTPX + AsyncIO    │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │   Raw Web Content    │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │    Google Gemini     │
                 │ Structured Extraction│
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Pydantic Validation  │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │     PostgreSQL       │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │  CrewAI Collective   │
                 │                      │
                 │ Financial Analyst    │
                 │          ↓           │
                 │ Market Strategist    │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Executive Intelligence│
                 │       Briefing       │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Streamlit Dashboard  │
                 └──────────────────────┘
```

---

# 🕷️ Phase 1 — Reconnaissance & Structured Extraction

The first phase converts unstructured competitor websites into validated structured intelligence.

## ⚡ Concurrent Web Reconnaissance

MarketSpy AI uses:

* `asyncio`
* `httpx`

to perform asynchronous network operations.

Instead of waiting for every request sequentially, relevant competitor pages can be retrieved concurrently.

Target resources can include:

* Homepage
* `/pricing`
* `/about`
* Product pages
* Company information

This makes the reconnaissance layer suitable for network-heavy workloads.

---

## 🧠 LLM-Powered Data Extraction

Raw web content is passed to **Google Gemini** for structured information extraction.

Instead of requesting free-form text, the system defines expected fields and structures.

```text
Raw Website Content
        ↓
      Gemini
        ↓
Structured Object
        ↓
Pydantic Validation
        ↓
PostgreSQL
```

This allows Gemini to function as an **intelligent ETL layer** rather than simply a conversational chatbot.

---

## 🛡️ Strict Schema Enforcement

AI-generated information is validated through **Pydantic v2** before being persisted.

This provides:

* Strong data contracts
* Type validation
* Required fields
* Consistent structures
* Predictable downstream processing

The result is a much more reliable pipeline for quantitative analysis.

---

## 📸 Screenshot Checkpoint #1 — Async Reconnaissance

> **Recommended screenshot:** VS Code terminal showing the asynchronous crawling and Gemini extraction process.

Example:

```text
[INFO] Starting competitor reconnaissance...
[INFO] Fetching competitor homepage...
[INFO] Fetching pricing page...
[INFO] Fetching about page...
[INFO] Gemini extraction started...
[INFO] Structured JSON generated
[INFO] Pydantic validation successful
[INFO] Data persisted successfully
```

Add your screenshot here:

<p align="center">
  <img src="assets/screenshots/async-reconnaissance.png" alt="Async Web Reconnaissance" width="850"/>
</p>

---

# 🤖 Phase 2 — CrewAI Multi-Agent Intelligence

Once structured competitor information has been stored in PostgreSQL, the multi-agent analysis pipeline begins.

MarketSpy AI uses specialized agents instead of relying on one general-purpose AI agent.

---

## 👨‍💼 Senior Financial Analyst

The **Senior Financial Analyst** focuses on quantitative intelligence.

Responsibilities include:

* Querying PostgreSQL
* Retrieving competitor metrics
* Comparing pricing structures
* Calculating pricing deltas
* Analyzing financial metrics
* Identifying quantitative competitive advantages
* Producing numerical findings

The analyst is intentionally focused on **data-driven reasoning**.

---

## 🧠 Lead Market Strategist

The **Lead Market Strategist** consumes the analyst's findings and converts them into strategic intelligence.

Responsibilities include:

* Executive-level interpretation
* Competitive positioning
* Strategic vulnerabilities
* Market opportunities
* Countermeasures
* Actionable recommendations
* Boardroom-ready summaries

The final output follows a **BLUF — Bottom Line Up Front** approach.

---

## 🔄 Agent Collaboration

```text
                PostgreSQL
                    │
                    ↓
        ┌──────────────────────┐
        │ Senior Financial     │
        │ Analyst              │
        └──────────┬───────────┘
                   │
                   │ Numerical Analysis
                   ↓
        ┌──────────────────────┐
        │ Lead Market          │
        │ Strategist           │
        └──────────┬───────────┘
                   │
                   │ Strategic Synthesis
                   ↓
        ┌──────────────────────┐
        │ Executive Briefing   │
        └──────────────────────┘
```

---

## 📸 Screenshot Checkpoint #2 — CrewAI Execution

> **Recommended screenshot:** Terminal showing the CrewAI agents executing sequentially.

Capture something similar to:

```text
Crew started
      ↓
Senior Financial Analyst
      ↓
Database Tool
      ↓
Financial Analysis
      ↓
Lead Market Strategist
      ↓
Strategic Synthesis
      ↓
Executive Briefing Generated
```

Add your screenshot here:

<p align="center">
  <img src="assets/screenshots/crewai-agents.png" alt="CrewAI Multi-Agent Execution" width="850"/>
</p>

---

# 🏗️ Architecture

MarketSpy AI follows a decoupled full-stack architecture.

```text
┌─────────────────────────────────────────────┐
│              STREAMLIT FRONTEND             │
│                                             │
│ Dashboard • Reports • Charts • Metrics      │
└──────────────────────┬──────────────────────┘
                       │ HTTP
                       ↓
┌─────────────────────────────────────────────┐
│               FASTAPI BACKEND               │
│                                             │
│ Competitors • Reports • Metrics • Tasks     │
└──────────────────────┬──────────────────────┘
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
┌──────────────────────┐   ┌──────────────────┐
│ Async Web Engine     │   │ CrewAI Agents    │
│ HTTPX + AsyncIO      │   │ Analyst          │
│                      │   │ Strategist       │
└──────────┬───────────┘   └────────┬─────────┘
           │                        │
           └────────────┬───────────┘
                        ↓
              ┌───────────────────┐
              │   Google Gemini   │
              │   Intelligence    │
              └─────────┬─────────┘
                        ↓
              ┌───────────────────┐
              │    PostgreSQL     │
              │ Structured Data   │
              └───────────────────┘
```

---

# 🧰 Technology Stack

| Layer            | Technology     | Purpose                             |
| ---------------- | -------------- | ----------------------------------- |
| Language         | Python 3.11+   | Core development                    |
| Frontend         | Streamlit      | Interactive dashboard               |
| Data Processing  | Pandas         | Data manipulation and visualization |
| Backend          | FastAPI        | REST API                            |
| Async Processing | asyncio        | Concurrent processing               |
| HTTP Client      | HTTPX          | Asynchronous web requests           |
| LLM              | Google Gemini  | AI extraction and reasoning         |
| Agent Framework  | CrewAI         | Multi-agent orchestration           |
| Agent Tools      | LangChain      | Tool integration                    |
| Validation       | Pydantic v2    | Data validation                     |
| ORM              | SQLAlchemy 2.0 | Database abstraction                |
| DB Driver        | asyncpg        | Async PostgreSQL connectivity       |
| Database         | PostgreSQL     | Persistent intelligence storage     |

---

# 📊 Streamlit Intelligence Dashboard

The Streamlit Control Center provides a unified interface for exploring generated competitive intelligence.

The dashboard combines:

### 📑 Qualitative Intelligence

* Executive briefing
* BLUF summary
* Strategic findings
* Competitive vulnerabilities
* Recommendations

### 📈 Quantitative Intelligence

* Financial metrics
* Pricing comparisons
* Pricing deltas
* Competitor comparisons
* Data visualizations

---

## 📸 Screenshot Checkpoint #3 — Final Executive Dashboard

> **Recommended screenshot:** Your best-looking final dashboard showing the generated report and charts together.

Ideally capture:

```text
┌────────────────────────────┬─────────────────────┐
│                            │                     │
│ Executive Briefing         │ Pricing Comparison │
│                            │                     │
│ BLUF                       │ █████████           │
│ Strategic Risks            │ ███████             │
│ Recommendations            │ █████               │
│                            │                     │
│                            │ Financial Metrics   │
│                            │                     │
└────────────────────────────┴─────────────────────┘
```

Add your screenshot here:

<p align="center">
  <img src="assets/screenshots/executive-dashboard.png" alt="MarketSpy Executive Intelligence Dashboard" width="950"/>
</p>

---

# 🗄️ PostgreSQL Intelligence Layer

MarketSpy AI does not rely solely on transient LLM responses.

Validated intelligence is persisted inside PostgreSQL.

This provides a structured foundation for:

* Historical analysis
* Competitor comparison
* Agent queries
* Pricing calculations
* Report generation
* Future trend analysis

---

## 📸 Screenshot Checkpoint #4 — Database

> **Recommended screenshot:** PostgreSQL client showing actual competitor records and extracted metrics.

For example:

```text
competitors
──────────────────────────────────
id | name     | domain
1  | Netflix  | netflix.com
2  | Shopify  | shopify.com


financial_metrics
──────────────────────────────────
competitor | revenue | pricing
Netflix    | ...     | ...
Shopify    | ...     | ...
```

Add your screenshot here:

<p align="center">
  <img src="assets/screenshots/postgresql-data.png" alt="MarketSpy PostgreSQL Data" width="850"/>
</p>

---

# 🔄 End-to-End Workflow

The complete MarketSpy pipeline works as follows:

### 1️⃣ Submit Competitors

The user provides competitor domains through the Streamlit dashboard.

### 2️⃣ Start Reconnaissance

FastAPI receives the request and initiates the intelligence workflow.

### 3️⃣ Concurrent Crawling

HTTPX and asyncio retrieve relevant competitor pages.

### 4️⃣ AI Extraction

Google Gemini extracts the required structured metrics.

### 5️⃣ Validation

Pydantic validates the generated data.

### 6️⃣ Persistence

Validated information is stored in PostgreSQL.

### 7️⃣ Agent Activation

CrewAI launches the specialized analytical agents.

### 8️⃣ Financial Analysis

The Senior Financial Analyst retrieves database information and performs quantitative comparisons.

### 9️⃣ Strategic Synthesis

The Lead Market Strategist transforms the findings into strategic recommendations.

### 🔟 Visualization

The Streamlit dashboard displays the final intelligence report and charts.

---

## 📸 Screenshot Checkpoint #5 — Complete Pipeline

> **Optional but highly recommended:** Capture a terminal showing the entire execution from competitor input to final report.

```text
Competitor Input
      ↓
Web Crawling
      ↓
Gemini Extraction
      ↓
Pydantic Validation
      ↓
PostgreSQL
      ↓
Financial Analyst
      ↓
Market Strategist
      ↓
Executive Report
```

Add your screenshot here:

<p align="center">
  <img src="assets/screenshots/end-to-end-pipeline.png" alt="MarketSpy End-to-End Pipeline" width="850"/>
</p>

---

# 📡 API Layer

The FastAPI backend provides a clean API boundary between the frontend and intelligence engine.

Typical resource categories include:

```text
/competitors
/reports
/metrics
```

FastAPI automatically generates interactive API documentation.

---

## 📸 Screenshot Checkpoint #6 — FastAPI Swagger

> **Recommended:** Open `http://127.0.0.1:8000/docs` and capture your API endpoints.

Add your screenshot here:

<p align="center">
  <img src="assets/screenshots/api-docs.png" alt="MarketSpy FastAPI Swagger Documentation" width="900"/>
</p>

---

# ✨ Key Features

## ⚡ Asynchronous Processing

Uses asynchronous I/O for network-heavy competitor reconnaissance.

## 🕷️ Concurrent Web Crawling

Retrieves multiple competitor resources efficiently.

## 🧠 Structured LLM Extraction

Uses Google Gemini to convert unstructured web content into structured intelligence.

## 🛡️ Data Validation

Pydantic validates AI-generated objects before persistence.

## 🤖 Multi-Agent Architecture

CrewAI coordinates specialized financial and strategic agents.

## 🗄️ Persistent Data Layer

PostgreSQL stores structured competitor intelligence.

## 📈 Automated Analytics

Calculates pricing and financial comparisons.

## 📑 Executive Reporting

Produces concise, strategic, decision-oriented reports.

## 🎨 Interactive Dashboard

Streamlit provides a visual interface for exploring the results.

## 🔌 Decoupled Architecture

FastAPI and Streamlit operate as independent application layers.

---

# 📁 Project Structure

```text
MARKETSPY AI/
│
├── .vscode/
│
├── backend/
│   │
│   ├── alembic/
│   │   ├── __pycache__/
│   │   ├── versions/
│   │   ├── env.py
│   │   ├── README
│   │   └── script.py.mako
│   │
│   ├── app/
│   │   ├── __pycache__/
│   │   │
│   │   ├── agents/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── crew.py
│   │   │   └── tools.py
│   │   │
│   │   ├── core/
│   │   │   ├── __pycache__/
│   │   │   └── ai_service.py
│   │   │
│   │   ├── crud/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── competitor.py
│   │   │   ├── metrics.py
│   │   │   └── report.py
│   │   │
│   │   ├── db/
│   │   │   ├── __pycache__/
│   │   │   └── session.py
│   │   │
│   │   ├── models/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── competitor.py
│   │   │   ├── metrics.py
│   │   │   └── report.py
│   │   │
│   │   ├── routers/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── competitor.py
│   │   │   ├── metrics.py
│   │   │   └── report.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── __pycache__/
│   │   │   ├── competitor.py
│   │   │   ├── metrics.py
│   │   │   └── report.py
│   │   │
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── main.py
│   │
│   ├── venv/
│   │
│   ├── .gitignore
│   ├── alembic.ini
│   └── requirements.txt
│
└── frontend/
    └── dashboard.py
```
---

# 💻 Installation & Local Setup

## Prerequisites

Make sure you have:

* Python 3.11+
* PostgreSQL
* Git
* Google AI Studio API Key

Check Python:

```bash
python --version
```

Check Git:

```bash
git --version
```

Make sure PostgreSQL is running locally.

---

# 1. Clone the Repository

```bash
git clone https://github.com/yourusername/marketspy-ai.git
cd marketspy-ai
```

Replace `yourusername` with your GitHub username.

---

# 2. Create a Virtual Environment

### Windows PowerShell

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 3. Install Dependencies

```bash
pip install fastapi sqlalchemy asyncpg pydantic-settings google-genai httpx crewai langchain streamlit pandas
```

For reproducible installation:

```bash
pip freeze > requirements.txt
```

Then future installations can use:

```bash
pip install -r requirements.txt
```

---

# 4. Configure PostgreSQL

Create a PostgreSQL database named:

```text
marketspy
```

Example configuration:

```text
Host: localhost
Port: 5432
Database: marketspy
Username: postgres
```

Your credentials may differ depending on your local setup.

---

# 5. Configure Environment Variables

Create:

```text
backend/.env
```

Add:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/marketspy
GEMINI_API_KEY=your_google_ai_studio_api_key_here
```

### Environment Variables

| Variable         | Description                        |
| ---------------- | ---------------------------------- |
| `DATABASE_URL`   | PostgreSQL async connection string |
| `GEMINI_API_KEY` | Google Gemini API key              |

---

# 🔐 Security

Never commit your `.env` file.

Add the following to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

If an API key is accidentally exposed on GitHub, revoke it and generate a new one immediately.

---

# 🚀 Running the Application

MarketSpy AI uses a decoupled backend and frontend.

You need **two terminal windows**.

---

## Terminal 1 — FastAPI Backend

Navigate to the backend:

```bash
cd backend
fastapi dev main.py
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Terminal 2 — Streamlit Frontend

From the project root:

```bash
streamlit run frontend/dashboard.py
```

Dashboard:

```text
http://localhost:8501
```

---

# 🧪 Example Execution

Once both services are running:

```text
1. Open Streamlit Dashboard
            ↓
2. Enter competitor domains
            ↓
3. Start intelligence scan
            ↓
4. FastAPI receives request
            ↓
5. Async spiders collect pages
            ↓
6. Gemini extracts structured metrics
            ↓
7. Pydantic validates results
            ↓
8. PostgreSQL stores intelligence
            ↓
9. CrewAI launches Financial Analyst
            ↓
10. Financial analysis generated
            ↓
11. Market Strategist synthesizes findings
            ↓
12. Executive briefing generated
            ↓
13. Streamlit displays report + charts
```

---

# 🧠 Why Multi-Agent Architecture?

A single general-purpose AI agent could theoretically perform the entire workflow.

However, MarketSpy AI deliberately separates responsibilities.

```text
                    Intelligence
                         │
                         ↓
              ┌────────────────────┐
              │ Financial Analyst  │
              │                    │
              │ Quantitative       │
              │ Analysis           │
              └─────────┬──────────┘
                        │
                        ↓
              ┌────────────────────┐
              │ Market Strategist  │
              │                    │
              │ Strategic          │
              │ Interpretation     │
              └─────────┬──────────┘
                        │
                        ↓
               Executive Briefing
```

This approach provides:

* Clear responsibility boundaries
* Easier debugging
* Modular agent development
* Specialized reasoning
* Better maintainability
* Easier future expansion

Additional agents can later be introduced without redesigning the entire system.

---

# 🏆 Engineering Highlights

## Separation of Concerns

The system separates:

```text
Frontend
Backend
Web Intelligence
LLM Extraction
Database
Agent Orchestration
Reporting
```

## Async I/O

Network-bound operations use asynchronous processing to reduce unnecessary blocking.

## Strong Data Contracts

Pydantic models define explicit contracts between LLM output and application logic.

## Database-Backed AI

The agents operate on persisted structured intelligence rather than relying exclusively on transient conversation context.

## Specialized Agents

Each agent has a clearly defined analytical role.

## API-Driven Architecture

The Streamlit frontend communicates with the FastAPI backend through an API boundary.

---

# 🔮 Future Roadmap

* [ ] Automated scheduled competitor monitoring
* [ ] Historical competitor price tracking
* [ ] Competitor change detection
* [ ] Email-based executive reports
* [ ] PDF report generation
* [ ] Additional financial metrics
* [ ] More specialized AI agents
* [ ] Authentication
* [ ] Role-based access control
* [ ] Docker deployment
* [ ] Cloud deployment
* [ ] Redis-based task queues
* [ ] Agent observability
* [ ] Agent tracing
* [ ] Automated source citation
* [ ] Competitive trend analysis

---

# ☁️ Deployment Architecture

A future cloud deployment could separate the components into independently scalable services.

```text
                       INTERNET
                          │
                          ↓
                   Reverse Proxy
                          │
             ┌────────────┴────────────┐
             ↓                         ↓
       FastAPI Backend           Streamlit UI
             │
       ┌─────┴───────────┐
       ↓                 ↓
 PostgreSQL          Task Queue
                         │
                         ↓
                  Agent Workers
```

This architecture can eventually support:

* Independent scaling
* Background workers
* Distributed agent execution
* Persistent task queues
* Production monitoring

---

# ⚠️ Limitations

MarketSpy AI depends on the availability and quality of publicly accessible competitor information.

Potential limitations include:

* Websites blocking automated requests
* JavaScript-heavy websites
* Dynamic pricing
* Missing financial information
* Changes in website structures
* LLM extraction errors
* API rate limits
* Incomplete public data

Important financial or strategic decisions should always be independently verified.

---

# 🔒 Responsible Use

MarketSpy AI is intended for legitimate competitive research using publicly accessible information.

Users should:

* Respect website Terms of Service
* Respect applicable crawling policies
* Respect `robots.txt` where applicable
* Avoid private or restricted information
* Respect API and website rate limits
* Verify important financial information
* Protect API and database credentials

---

# 🎓 What This Project Demonstrates

MarketSpy AI demonstrates practical engineering experience across several modern AI and software development areas.

### AI Engineering

* Generative AI
* Google Gemini
* Structured LLM extraction
* CrewAI
* Multi-agent systems
* Tool-enabled agents

### Backend Engineering

* FastAPI
* REST APIs
* Async programming
* Background processing

### Data Engineering

* PostgreSQL
* SQLAlchemy
* asyncpg
* Pydantic
* Structured data pipelines

### Frontend Engineering

* Streamlit
* Pandas
* Data visualization
* Interactive dashboards

### Software Architecture

* Decoupled services
* Separation of concerns
* Asynchronous pipelines
* Agent specialization
* Database-backed AI systems

---

# 💡 Core Architecture Philosophy

MarketSpy AI demonstrates how LLMs can become components inside a structured software architecture rather than simply acting as conversational interfaces.

The system transforms:

```text
                    RAW WEB DATA
                         │
                         ↓
               ASYNCHRONOUS RETRIEVAL
                         │
                         ↓
                  LLM EXTRACTION
                         │
                         ↓
                SCHEMA VALIDATION
                         │
                         ↓
                    DATABASE
                         │
                         ↓
                MULTI-AGENT ANALYSIS
                         │
                ┌────────┴────────┐
                ↓                 ↓
         FINANCIAL             STRATEGIC
          ANALYSIS            REASONING
                │                 │
                └────────┬────────┘
                         ↓
                EXECUTIVE REPORT
                         │
                         ↓
                  VISUAL DASHBOARD
```

The result is an end-to-end **autonomous competitive intelligence pipeline**.

---

# 📸 Screenshot Gallery

For a strong GitHub portfolio, the recommended screenshot set is:

| Screenshot           | Filename                   | Priority |
| -------------------- | -------------------------- | -------- |
| Main Dashboard       | `dashboard.png`            | ⭐⭐⭐⭐⭐    |
| Async Reconnaissance | `async-reconnaissance.png` | ⭐⭐⭐⭐     |
| CrewAI Agents        | `crewai-agents.png`        | ⭐⭐⭐⭐⭐    |
| Executive Dashboard  | `executive-dashboard.png`  | ⭐⭐⭐⭐⭐    |
| PostgreSQL Data      | `postgresql-data.png`      | ⭐⭐⭐⭐     |
| End-to-End Pipeline  | `end-to-end-pipeline.png`  | ⭐⭐⭐      |
| FastAPI Swagger      | `api-docs.png`             | ⭐⭐⭐⭐     |

### Recruiter-Focused Priority

If you only have time to capture **three screenshots**, use:

```text
1️⃣ Main Dashboard
        ↓
2️⃣ CrewAI Multi-Agent Execution
        ↓
3️⃣ Executive Intelligence Dashboard
```

These three provide the strongest visual proof that MarketSpy AI is a **real, working AI engineering project** rather than simply an LLM demo.

---

# 👨‍💻 Author

## Your Name

**B.Tech Computer Science & Engineering**

### Interests

* 🤖 Artificial Intelligence
* 🧠 Generative AI
* 🔗 Multi-Agent Systems
* 🌐 Full-Stack Development
* 🔐 Cybersecurity
* ⚙️ AI Automation

---

# ⭐ Support

If you find **MarketSpy AI** interesting, consider giving the repository a ⭐ on GitHub.

---

# 📄 License

This project is available under the license specified in the repository's `LICENSE` file.

---

<p align="center">

<strong>Built with Python • FastAPI • Streamlit • PostgreSQL • Gemini • CrewAI</strong>

</p>

<p align="center">
  <sub>Turning competitive web data into actionable intelligence.</sub>
</p>

