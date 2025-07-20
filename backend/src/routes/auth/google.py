from fastapi import APIRouter

router = APIRouter(prefix="/google")


@router.get("/")
async def google_auth(code: str):
    """Endpoint for Google authentication."""
    return {"message": "Google authentication endpoint", "code": code}
