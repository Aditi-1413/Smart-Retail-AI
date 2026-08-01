import json
import pickle
import random
import numpy as np
import nltk

from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()

# Load chatbot model
model = load_model("app/models/chatbot_model.h5")

# Load words and classes
words = pickle.load(open("app/models/chatbot_words.pkl", "rb"))
classes = pickle.load(open("app/models/chatbot_classes.pkl", "rb"))

# Load intents
with open("data/intents.json") as file:
    intents = json.load(file)


def clean_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [
        lemmatizer.lemmatize(word.lower())
        for word in sentence_words
    ]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_sentence(sentence)

    bag = [0] * len(words)

    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                bag[i] = 1

    return np.array(bag)


def chatbot_reply(message):

    bow = bag_of_words(message)

    prediction = model.predict(
        np.array([bow]),
        verbose=0
    )[0]

    index = np.argmax(prediction)

    tag = classes[index]

    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return {
                "intent": tag,
                "response": random.choice(intent["responses"]),
                "confidence": round(float(prediction[index]), 4)
            }

    return {
        "intent": "unknown",
        "response": "Sorry, I didn't understand.",
        "confidence": 0.0
    }