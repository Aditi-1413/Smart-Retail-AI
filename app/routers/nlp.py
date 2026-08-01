from fastapi import APIRouter

from pydantic import BaseModel

from app.services.sentiment_service import predict_sentiment

router = APIRouter()


class Review(BaseModel):
    text: str


@router.post("/predict-sentiment")
def sentiment(review: Review):

    return predict_sentiment(review.text)