from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import documents, health, rag
from app.core.exception_handler import register_exception_handlers

app = FastAPI(
    title="VidyAI Backend",
    version="1.0.0",
    description="AI-powered Academic Intelligence Platform",
)

# Local frontend development origin. Configure the deployment origin here
# (or replace this with an environment-driven allow-list) before production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

register_exception_handlers(app)
app.include_router(health.router)
app.include_router(documents.router)
app.include_router(rag.router)


@app.get("/")
async def root():
    return {"project": "VidyAI", "status": "running"}
