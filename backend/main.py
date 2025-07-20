from fastapi import FastAPI

from src.routes import router

app = FastAPI()
app.include_router(router)


@app.get("/")
async def index():
    """Root endpoint that returns a greeting message."""
    return {"message": "Hello, World!"}
