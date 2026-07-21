from crewai.tools import tool
import httpx

@tool("Fetch Competitor Financial Metrics")
def fetch_competitor_metrics_tool(competitor_id: int) -> str:
    """
    Useful when you need to retrieve structured financial metrics, 
    such as Total Revenue, Net Income, or R&D expenses for a specific competitor ID.
    Input must be an integer representing the competitor ID.
    """
    # Point directly to the live GET endpoint we built and tested in Phase 2
    url = f"http://127.0.0.1:8000/reports/metrics/{competitor_id}"
    
    try:
        # Use httpx to make a clean, synchronous call to the API
        response = httpx.get(url, timeout=10.0)
        
        if response.status_code == 200:
            return str(response.json())
        else:
            return f"Failed to retrieve metrics. Server responded with status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred while connecting to the metrics API: {str(e)}"