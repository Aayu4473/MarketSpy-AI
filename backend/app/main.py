from fastapi import FastAPI
from app.routers import competitor, report, metrics

app = FastAPI(title="MarketSpy AI Backend")

# Plug in the Drive-Thru Window!
app.include_router(competitor.router)

@app.get("/")
async def root():
    return {"message": "Welcome to MarketSpy AI API"}

app.include_router(competitor.router)
app.include_router(report.router)
app.include_router(metrics.router)