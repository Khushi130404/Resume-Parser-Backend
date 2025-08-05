from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="Resume Parser API",
    description="Upload a resume and extract key information.",
    version="1.0.0"
)

app.include_router(router)
