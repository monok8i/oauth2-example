from fastapi import FastAPI

from src.routes import router as api_router

app = FastAPI()
app.include_router(api_router)


@app.get("/")
async def index():
    """Root endpoint that returns a greeting message."""
    return {"message": "Hello, World!"}
