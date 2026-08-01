from fastapi import FastAPI

from app.routers.vision import router as vision_router
from app.routers.nlp import router as nlp_router
from app.routers.chatbot import router as chatbot_router

app = FastAPI(
    title="Smart Retail AI",
    version="1.0.0"
)

app.include_router(vision_router)
app.include_router(nlp_router)
app.include_router(chatbot_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Retail AI"
    }