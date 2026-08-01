import joblib

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load trained model
model = load_model("app/models/sentiment_model.h5")

# Load IMDB word index
word_index = joblib.load("app/models/imdb_word_index.pkl")

MAX_LENGTH = 200


def preprocess_review(review):

    review = review.lower().split()

    encoded = []

    for word in review:

        if word in word_index:
            encoded.append(word_index[word] + 3)

        else:
            encoded.append(2)

    sequence = pad_sequences(
        [encoded],
        maxlen=MAX_LENGTH
    )

    return sequence


def predict_sentiment(review):

    sequence = preprocess_review(review)

    prediction = model.predict(
        sequence,
        verbose=0
    )[0][0]

    sentiment = "Positive"

    if prediction < 0.5:
        sentiment = "Negative"

    return {
        "sentiment": sentiment,
        "confidence": round(float(prediction), 4)
    }