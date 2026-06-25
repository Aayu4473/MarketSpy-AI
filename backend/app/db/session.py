import os
from typing import AsyncGenerator
# 1. Import your new central configuration object instead of load_dotenv
from app.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# 2. Instantiate our high-performance Asynchronous DB Engine 
# We now grab the validated URL straight from settings.DATABASE_URL
engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

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