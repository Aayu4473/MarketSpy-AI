import os
from typing import AsyncGenerator
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# 1. Load system secrets from our decoupled backend/.env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("CRITICAL SYSTEM ERROR: DATABASE_URL environment variable is not configured.")

# 2. Instantiate our high-performance Asynchronous DB Engine
# echo=True prints raw SQL logs to your terminal so you can audit database transactions visually
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# 3. Form our decoupled Session Factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,  # Prevents lazy-loading errors after committing database records
    autocommit=False,
    autoflush=False,
)

# 4. Create our Dependency Injection Gateway
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI Database Dependency Injection Generator.
    Yields an active asynchronous connection session pool per HTTP request lifecycle,
    and guarantees a strict cleanup close operation when the route returns.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()