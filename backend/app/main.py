from fastapi import FastAPI
from app.routers import competitor

app = FastAPI(title="MarketSpy AI Backend")

# Plug in the Drive-Thru Window!
app.include_router(competitor.router)

@app.get("/")
async def root():
    return {"message": "Welcome to MarketSpy AI API"}