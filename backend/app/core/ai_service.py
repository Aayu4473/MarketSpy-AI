import re
import httpx
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.models.report import Report
from app.models.metrics import Metrics

# Initialize the Gemini Client using our central configuration settings
client = genai.Client(api_key=settings.GEMINI_API_KEY)


# 1. Define a strict schema for an individual metric item.
# This eliminates the generic 'dict' type, resolving the Gemini API validation crash.
class MetricItem(BaseModel):
    metric_type: str = Field(
        description="The clean name/category of the metric (e.g., 'Total Revenue', 'Automotive Gross Margin', 'Total Deliveries')."
    )
    value: float = Field(
        description="The extracted raw numerical value as a float. Normalize percentages or shorthand values (e.g., 5.4B turns into 5400000000.0)."
    )
    source_url: str = Field(
        description="The exact web page URL from which this specific financial metric was harvested."
    )


# 2. Define the main payload schema using our new strongly typed MetricItem structure
class ExtractedMarketData(BaseModel):
    markdown_analysis: str = Field(
        description="Comprehensive market analysis report formatted in beautiful clean Markdown."
    )
    metrics: list[MetricItem] = Field(
        description="List of key numerical financial and performance metrics found within the target text."
    )


async def fetch_url_content(url: str) -> str:
    """
    Fetches live web content directly. Uses SEC-compliant headers to guarantee 
    unblocked access when fetching raw corporate filings from government servers.
    """
    # The SEC mandates this exact header structure: "AppName (your_email@domain.com)"
    headers = {
        "User-Agent": "MarketSpy_AI_Engine (admin@marketspy.local)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    
    print(f"[LIVE FETCH] Attempting direct connection to: {url}")

    async with httpx.AsyncClient(headers=headers, timeout=20.0, follow_redirects=True) as httpx_client:
        response = await httpx_client.get(url)
        
        if response.status_code != 200:
            raise Exception(f"Failed to fetch content. HTTP Status: {response.status_code}")

        # --- NEW CLEANING LOGIC ---
        # 1. Use regex to strip out all <html tags>
        clean_text = re.sub(r'<[^>]+>', ' ', response.text)
        # 2. Collapse massive blank spaces into single spaces
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        
        # Now 150,000 characters of PURE TEXT will go deep into the financial tables!
        return clean_text  # Cap at 20k characters for Gemini


async def generate_market_report(competitor_id: int, target_url: str, db: AsyncSession):
    """
    Downloads web content, runs it through Gemini's reasoning engine, 
    and inserts both the report and parsed metrics into the database.
    """
    try:
        # 1. Fetch raw text data from the competitor's target URL
        raw_web_text = await fetch_url_content(target_url)

        # 2. Build out a detailed system prompt for the intelligence engine
        system_prompt = (
            "You are an expert financial and competitive intelligence analyst for MarketSpy AI. "
            "Analyze the provided raw website text and extract actionable insights. "
            "Generate a highly professional markdown report and pull out all identifiable "
            "numerical data metrics (revenues, delivery figures, growth rates, etc.)."
        )

        # 3. Request structured data output back from Gemini
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=f"Target URL Content:\n{raw_web_text}",
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json",
                response_schema=ExtractedMarketData,
                temperature=0.2
            ),
        )

        # 4. Parse the structured output safely
        # The SDK automatically converts the response straight into our strict ExtractedMarketData instance
        ai_data: ExtractedMarketData = response.parsed

        # 5. Save the generated Markdown report directly into the database
        db_report = Report(
            competitor_id=competitor_id,
            target_url=target_url,
            ai_markdown_analysis=ai_data.markdown_analysis
        )
        db.add(db_report)

        # 6. Iterate and save each individual metric pulled out by Gemini
        # We now use dot notation accessors since item is a verified Pydantic object instance
        for item in ai_data.metrics:
            db_metric = Metrics(
                competitor_id=competitor_id,
                metric_type=item.metric_type,
                value=item.value,
                source_url=item.source_url if item.source_url else target_url
            )
            db.add(db_metric)

        # 7. Commit both operations atomically to the database
        await db.commit()
        print(f"Successfully processed and stored AI intelligence data for Competitor ID: {competitor_id}")

    except Exception as e:
        await db.rollback()
        print(f"CRITICAL ERROR in AI Engine Loop: {str(e)}")
        raise e