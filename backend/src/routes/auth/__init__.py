from fastapi import APIRouter

from .google import router as google_router

router = APIRouter(prefix="/auth")
router.include_router(google_router)

__all__ = ["router"]
