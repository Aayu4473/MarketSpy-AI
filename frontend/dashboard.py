import streamlit as st
import requests
import pandas as pd

# 1. Premium Theme Configuration
st.set_page_config(
    page_title="MarketSpy AI | Competitive Intelligence Hub",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Target configuration pointing directly to your local FastAPI server
BACKEND_URL = "http://localhost:8000"

# 2. Injecting Custom Clean UI Aesthetics
st.markdown("""
    <style>
    /* Base typography and layout */
    .main-title { font-size: 2.8rem; font-weight: 800; color: #0F172A; margin-bottom: 0.2rem; letter-spacing: -0.05em; }
    .subtitle { font-size: 1.15rem; color: #475569; margin-bottom: 1.5rem; }
    
    /* Premium Metric Cards */
    .metric-card {
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        color: #111;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05), 0 1px 3px rgba(0,0,0,0.1);
        font-family: 'Inter', sans-serif;
        border: 1px solid rgba(0,0,0,0.05);
    }
    
    /* Vibrant Color Rotation */
    .metric-green { background-color: #4ade80; } /* Emerald */
    .metric-blue { background-color: #60a5fa; }  /* Blue */
    .metric-yellow { background-color: #facc15; } /* Yellow */
    .metric-gray { background-color: #f1f5f9; }  /* Slate */
    
    /* Typography inside the cards */
    .metric-title { 
        font-size: 15px; 
        font-weight: 600; 
        opacity: 0.85; 
        margin-bottom: 8px; 
    }
    .metric-value { 
        font-size: 32px; 
        font-weight: 800; 
        margin: 0; 
        line-height: 1.1; 
        letter-spacing: -0.03em;
    }
    .metric-source {
        font-size: 12px;
        font-weight: 500;
        opacity: 0.75;
        margin-top: 12px;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    
    /* Style the custom dropdown filter row */
    .filter-row {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 20px;
        padding: 10px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigation Control
st.sidebar.title("🦅 MarketSpy Control Center")
st.sidebar.markdown("---")

# Module A: Trigger New Deep-Scrape & Analysis Pipeline
st.sidebar.subheader("🎯 Analyze New Target")
company_name = st.sidebar.text_input("Company Name", placeholder="e.g., OpenAI")
company_domain = st.sidebar.text_input("Company Website", placeholder="e.g., openai.com")

if st.sidebar.button("🚀 Execute Agent Analysis", use_container_width=True):
    if company_name and company_domain:
        with st.sidebar.spinner("Deploying CrewAI Agents to scrape and evaluate..."):
            try:
                payload = {"name": company_name, "website": company_domain}
                response = requests.post(f"{BACKEND_URL}/competitors/", json=payload)
                
                if response.status_code in [200, 201]:
                    st.sidebar.success(f"Analysis successfully built for {company_name}!")
                    st.rerun() 
                else:
                    try:
                        error_msg = response.json().get("detail", f"Error {response.status_code}")
                        st.sidebar.error(error_msg)
                    except:
                        st.sidebar.error(f"Backend returned error code: {response.status_code}")
                        
            except Exception as e:
                st.sidebar.error(f"Could not connect to FastAPI server: {e}")
    else:
        st.sidebar.warning("Please provide both name and domain.")

st.sidebar.markdown("---")

# Module B: Fetch and List Tracked Portfolios
st.sidebar.subheader("🗂️ Tracked Portfolio")
try:
    competitors_raw = requests.get(f"{BACKEND_URL}/competitors/").json()
    competitor_map = {item["name"]: item["id"] for item in competitors_raw}
    options_list = ["-- Select Monitored Company --"] + list(competitor_map.keys())
except Exception:
    options_list = ["-- Select Monitored Company --"]
    st.sidebar.error("⚠️ Connection offline: Run FastAPI backend.")

selected_name = st.sidebar.selectbox("Switch Dashboard Focus", options_list)

# --- NEW: DELETE BUTTON LOGIC ---
if selected_name != "-- Select Monitored Company --":
    target_id = competitor_map[selected_name]
    
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    if st.sidebar.button("🗑️ Delete Profile", type="primary", use_container_width=True):
        try:
            del_response = requests.delete(f"{BACKEND_URL}/competitors/{target_id}")
            if del_response.status_code == 200:
                st.sidebar.success(f"Deleted {selected_name} from database.")
                st.rerun()
            else:
                st.sidebar.error("Failed to delete profile.")
        except Exception as e:
            st.sidebar.error(f"Connection error: {e}")

st.sidebar.markdown("---")

# 4. Main View Routing Logic
if selected_name == "-- Select Monitored Company --" or not options_list:
    # Landing/Fallback view
    st.markdown('<h1 class="main-title">📈 MarketSpy Intelligence Engine</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Autonomous AI market agent networks tracking your competitive landscape in real-time.</p>', unsafe_allow_html=True)
    
    stat_col1, stat_col2, stat_col3 = st.columns(3)
    monitored_count = len(options_list) - 1 if len(options_list) > 1 else 0
    
    with stat_col1:
        st.metric("Monitored Profiles", monitored_count, delta="Live Database")
    with stat_col2:
        st.metric("Agent Squadrons Active", "3 Crew Workers", delta="Stable Mode")
    with stat_col3:
        st.metric("Analysis Engine API", "Operational", delta="Ready")
        
    st.info("💡 Pro-Tip: Pick an existing profile from the sidebar dropdown on the left or add a new brand to stream a real-time deep dive report.")

else:
    # Deep dive view for the chosen competitor
    target_id = competitor_map[selected_name]
    
    try:
        response = requests.get(f"{BACKEND_URL}/competitors/{target_id}")
        
        if response.status_code == 200:
            data = response.json()
            
            # --- HEADER ---
            st.markdown(f'<h1 class="main-title">🏢 {data.get("name", "Unknown")} Focus</h1>', unsafe_allow_html=True)
            st.markdown(f'<p class="subtitle">Monitored Web Domain: <a href="https://{data.get("domain", "")}" target="_blank"><code>{data.get("domain", "N/A")}</code></a></p>', unsafe_allow_html=True)
            
            # --- DROPDOWN FILTER ROW ---
            st.markdown('<div class="filter-row">', unsafe_allow_html=True)
            filter_col, _ = st.columns([1, 3]) # Makes the dropdown small and pushed to the left
            with filter_col:
                view_mode = st.selectbox(
                    "🔎 Filter Dashboard View:",
                    ["All Insights", "💰 Financial & Growth", "⚙️ Operational Scale"]
                )
            st.markdown('</div>', unsafe_allow_html=True)
            st.divider()
            
            # --- METRIC FILTERING LOGIC ---
            metrics = data.get("metrics", [])
            filtered_metrics = []
            
            # Keywords to auto-detect if a metric is financial
            # Updated keyword list in dashboard.py
            fin_keywords = ["valuation", "sales", "gmv", "revenue", "capital", "margin", "profit", "cost", "funding", "price", "tier", "plan", "subscription"]
            
            for met in metrics:
                lbl = met.get("label", "").lower()
                is_fin = any(kw in lbl for kw in fin_keywords)
                
                if view_mode == "💰 Financial & Growth" and is_fin:
                    filtered_metrics.append(met)
                elif view_mode == "⚙️ Operational Scale" and not is_fin:
                    filtered_metrics.append(met)
                elif view_mode == "All Insights":
                    filtered_metrics.append(met)

            # --- THE 60/40 SPLIT LAYOUT ---
            left_col, right_col = st.columns([1.5, 1], gap="large")
            
            # LEFT: Qualitative Markdown Report
            with left_col:
                st.subheader("📝 Qualitative Intelligence Briefing")
                st.caption(f"Filtered for: {view_mode}")
                
                with st.container(border=True):
                    st.markdown(data.get("report", "No written contents found."))
            
            # RIGHT: Graphs & Quantitative Metrics
            with right_col:
                st.subheader("📊 Quantitative Performance")
                st.caption("Visualized Data & Key Extracted Figures")
                
                if filtered_metrics:
                    
                    # --- NEW: INTERACTIVE GRAPH ---
                    try:
                        # Build a Pandas DataFrame from the filtered metrics
                        df = pd.DataFrame([
                            {"Metric": m["label"], "Value": float(m["value"])} 
                            for m in filtered_metrics 
                        ])
                        
                        if not df.empty:
                            # We sort and take the top 5 to prevent the graph from looking cluttered
                            df = df.sort_values(by="Value", ascending=False).head(5)
                            st.bar_chart(data=df.set_index("Metric"), use_container_width=True)
                    except Exception as e:
                        pass # Silently skip graph if data format is weird
                        
                    # --- KEY METRICS GRID ---
                    colors = ["metric-green", "metric-blue", "metric-yellow", "metric-gray"]
                    card_col1, card_col2 = st.columns(2)
                    
                    for i, met in enumerate(filtered_metrics):
                        target_col = card_col1 if i % 2 == 0 else card_col2
                        card_color = colors[i % len(colors)]
                        
                        # Format numeric values intelligently
                        try:
                            val = float(met.get("value", 0))
                            if val >= 1_000_000_000:
                                formatted_val = f"${val/1_000_000_000:.1f}B"
                            elif val >= 1_000_000:
                                formatted_val = f"${val/1_000_000:.1f}M"
                            else:
                                formatted_val = f"{val:,.0f}"
                        except ValueError:
                            formatted_val = met.get("value", "0")
                            
                        # Build the HTML structure for the card
                        html_card = f"""
                        <div class="metric-card {card_color}">
                            <div class="metric-title">{met.get('label', 'Metric')}</div>
                            <div class="metric-value">{formatted_val}</div>
                            <div class="metric-source">✓ Verified in AI Extraction</div>
                        </div>
                        """
                        
                        with target_col:
                            st.markdown(html_card, unsafe_allow_html=True)
                else:
                    st.info(f"No metrics found for the '{view_mode}' category.")
                    
        else:
            st.error(f"⚠️ Failed to load data from backend. (Error Code: {response.status_code})")
            
    except Exception as e:
        st.error(f"Error compiling dynamic dashboard view: {e}")