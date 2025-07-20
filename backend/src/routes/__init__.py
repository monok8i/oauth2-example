from fastapi import APIRouter

from .auth import google_router

router = APIRouter(prefix="/auth")

router.include_router(google_router)
