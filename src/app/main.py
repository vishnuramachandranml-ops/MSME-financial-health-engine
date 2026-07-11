from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.core.logger import configure_logging
from app.core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    yield


app = FastAPI(
    title="AI Underwriter Copilot API",
    description="""
AI-powered MSME Financial Health Assessment Engine.

Features:
- Explainable Financial Health Score
- Component-wise Risk Assessment
- AI Executive Summary (Gemini)
- Credit Recommendation
- Alternate Data Evaluation
- Explainable Metric Breakdown
""",
    version="1.0.0",
    contact={
        "name": "Team AI Underwriter",
        "email": "team@example.com",
    },
)

app.include_router(api_router)