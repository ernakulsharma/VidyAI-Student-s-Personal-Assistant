from fastapi import FastAPI

from app.api.routes import documents, health, rag
from app.core.exception_handler import (
    register_exception_handlers,
)

app = FastAPI(
    title="VidyAI Backend",
    version="1.0.0",
    description="AI-powered Academic Intelligence Platform"
)

register_exception_handlers(app)
app.include_router(health.router)
app.include_router(documents.router)
app.include_router(rag.router)

@app.get("/")
async def root():
    return {
        "project": "VidyAI",
        "status": "running"
    }