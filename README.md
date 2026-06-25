# 🕵️‍♂️ MarketSpy AI

An autonomous, asynchronous competitive market intelligence pipeline. This backend platform consumes competitor targets via a REST API, scrapes unstructured web data, and leverages Large Language Models (LLMs) to extract key financial metrics and generate comprehensive market analysis reports.

🚧 **Status:** Active Development (Phase 2 - AI Engine Integration)

---

## 🎯 The Vision & Final Achievement

MarketSpy AI is designed to eliminate the manual tracking of competitor updates, quarterly investor relations filings, and product announcements. 

**What we will achieve:** The final system will programmatically ingest messy, unstructured web text from target company portals, run it through an isolated AI reasoning loop in the background, and cleanly extract structured financial metrics alongside deep qualitative analysis reports. This data will be instantly saved into a relational database and served to front-end dashboards, providing zero-touch, real-time market intelligence.

---

## 🛑 The Problem Statement: The Cost of Manual Market Intelligence

In modern enterprise environments, keeping track of competitive landscapes is a chaotic, labor-intensive bottleneck. Product managers, financial analysts, and executives spend hundreds of aggregate hours manually browsing competitor websites, monitoring investor relations portals, reading press releases, and auditing regulatory filings. 

This manual approach introduces three critical failure points:
1. **Unstructured Data Ingestion Exhaustion:** Corporate updates are buried in messy HTML, PDFs, and long-form prose. Extracting clean data from these sources manually does not scale.
2. **Data Inconsistency & Latency:** Human data collection is slow and prone to input errors. Critical data points (like a competitor's sudden drop in price or spike in delivery volume) are often caught weeks after they occur.
3. **Information Siloing:** Qualitative insights (strategic shifting mentioned in an article) and quantitative metrics (revenue figures) are tracked in separate spreadsheets, breaking down unified data analysis.

---

## 🎯 The Core Purpose: Production-Grade Automated Parsing

**MarketSpy AI** solves this problem by architecting an automated, hands-free competitive intelligence pipeline that translates raw, unstructured web text into clean, relational database structures in real time. 

The application is built to demonstrate how modern AI engineering can solve real-world data fragmentation by fulfilling three core purposes:

* **Eliminating Parsing Hallucinations with Rigid Schema Enforcement:** Instead of using LLMs as basic conversational chat interfaces, MarketSpy AI uses programmatic schema guardrails (via Pydantic and Gemini's structured JSON mode) to force generative AI to act as a strict, dependable data ETL (Extract, Transform, Load) pipeline.
* **Guaranteeing System Throughput via Asynchronous Non-Blocking Tasks:** Downloading web data and awaiting LLM reasoning can take anywhere from 2 to 10 seconds per target. By offloading these intensive network calls to asynchronous background tasks, the system keeps API endpoints incredibly responsive under high concurrent traffic.
* **Unifying Strategic Context with Hard Metrics:** The pipeline splits AI parsing results into two parallel relational tables simultaneously—one dedicated to qualitative Markdown intelligence reports and the other tracking numerical performance metrics—enabling deep analytical data processing from a single ingestion point.

--- 

## 🏗️ Architectural Blueprint

The project enforces a strict, decoupled multi-layer software architecture to guarantee maintainability, database atomicity, and high concurrent throughput.

* **API Routing Layer (`app/routers/`):** Lightweight, asynchronous FastAPI endpoints decoupled by resource type (`competitors`, `reports`, `metrics`).
* **Data Serialization Layer (`app/schemas/`):** Robust Pydantic v2 data models ensuring strict data validation for incoming payloads and automated type enforcement for outbound responses.
* **Database Access & Context Layer (`app/session.py`):** High-performance asynchronous context engines processing data pooling workflows concurrently via the modern SQLAlchemy 2.0 standard.
* **Centralized Configuration (`app/config.py`):** Unified, fail-fast settings engine leveraging Pydantic Settings to load, validate, and typecast raw environment variables (`.env`) safely at system boot.
* **AI Service Layer (`app/core/ai_service.py`):** Isolated reasoning engine utilizing the Google GenAI SDK to enforce strict JSON schemas on LLM outputs.

---

## ✅ Phase 1: Foundation (What We Did)

The fundamental database persistence and routing infrastructures are fully built, tested, and passing integration checks:

* **Asynchronous Driver Pipeline:** Built a complete, non-blocking database execution loop utilizing `postgresql+asyncpg`.
* **Relational Database Integrity:** Constructed fully mapped SQLAlchemy entity relationships between Parent profiles (`Competitors`) and Child documents (`Reports`, `Metrics`).
* **Strict Type Safety:** Implemented complete Pydantic schemas, successfully eradicating silent schema drift and validation inconsistencies (e.g., catching case-sensitive `created_at` mapping errors).
* **Interactive Testing Engine:** Verified the entire database lifecycle and API interactions via the fully integrated FastAPI OpenAPI/Swagger documentation dashboard.

---

## ⚙️ Phase 2: The AI Engine (What We Are Doing)

We are actively connecting the routing layer to the intelligence engine to automate data parsing:

* **Centralized Configuration:** Implemented a secure `config.py` state to handle external secrets (`GEMINI_API_KEY`) and database URLs securely.
* **LLM Integration:** Configuring the Google GenAI SDK to use `gemini-1.5-flash` for high-speed, accurate reasoning.
* **Web Scraping:** Utilizing `httpx` to asynchronously fetch raw text from target competitor URLs.
* **Structured Prompt Engineering:** Forcing the LLM to return output strictly bound to our `ExtractedMarketData` Pydantic model to guarantee seamless database insertion.

---

## 🗺️ Phase 3: Automation & Scale (What We Will Achieve)

The final phase will finalize the product for production environments:

* **Background Task Offloading:** Move blocking AI text-generation tasks into FastAPI background workers so the API responds instantly to users while the LLM works in the background.
* **Automated Router Triggers:** Update the `POST /reports/` endpoint to automatically trigger the `ai_service.py` pipeline upon receiving a URL.
* **Advanced Analytics:** Implement endpoints to calculate historical metric trend analytics (e.g., quarter-over-quarter revenue growth).
* **Database Migrations:** Introduce a production-grade migrations manager (Alembic) to handle future schema upgrades safely.

---

## 💻 Installation & Local Setup

### 1. Prerequisites
Ensure your system has the following dependencies installed globally:
* **Python 3.11+**
* **PostgreSQL** (Running locally on default port 5432)
* **Git**

### 2. Clone the Repository
Clone the project workspace to your local environment and change into the backend module directory:
```bash
git clone [https://github.com/yourusername/marketspy-ai.git](https://github.com/yourusername/marketspy-ai.git)
cd "MarketSpy AI/backend"
```

### 3. Initialize an Isolated Virtual Environment
It is highly recommended to install the pipeline within a dedicated environment sandbox to prevent environment pollution:

### Windows (PowerShell):

PowerShell
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Project Packages
With the virtual environment activated, install the required asynchronous production frameworks:
```bash
pip install fastapi sqlalchemy asyncpg pydantic-settings google-genai httpx
```
### 5. Configure Local Environment Variables
Create a .env file inside your project root (backend/.env) to decouple sensitive system secrets from the version control system:

Code snippet
```bash
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/marketspy
GEMINI_API_KEY=your_google_ai_studio_api_key_here
```
### 6. Run the Live Development Server
Boot the FastAPI application runner with automatic system reload tracking enabled:

```bash
fastapi dev app/main.py
```
#### Application Landing Gateway: http://127.0.0.1:8000

#### Interactive OpenAPI/Swagger Documentation: http://127.0.0.1:8000/docs
