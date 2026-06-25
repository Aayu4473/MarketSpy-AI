from fastapi import FastAPI
from app.routers import competitor, report, metrics

app = FastAPI(title="MarketSpy AI Backend",
              description="Production-grade asynchronous competitive intelligence pipeline",
              version="1.0.0"
              )

# Plug in the Drive-Thru Window!
app.include_router(competitor.router)
app.include_router(report.router)
app.include_router(metrics.router)

@app.get("/")
async def root():
    return {"message": "Welcome to MarketSpy AI API"}