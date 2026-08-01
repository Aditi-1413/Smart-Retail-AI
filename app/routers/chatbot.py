from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chatbot_service import chatbot_reply

router = APIRouter()


class Message(BaseModel):
    text: str


@router.post("/chat")
def chat(message: Message):
    return chatbot_reply(message.text)