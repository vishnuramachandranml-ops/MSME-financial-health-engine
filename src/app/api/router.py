from fastapi import APIRouter

from app.api.routers.health import router as health_router
from app.api.routers.version import router as version_router
from app.api.routers.assessment import router as assessment_router



api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(version_router)
api_router.include_router(assessment_router)