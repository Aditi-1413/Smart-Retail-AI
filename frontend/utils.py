import requests

API = "http://127.0.0.1:8000"


# ==========================================
# PRODUCT CLASSIFICATION
# ==========================================

def predict_product(uploaded_file):

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    try:

        response = requests.post(
            API + "/predict-product",
            files=files
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


# ==========================================
# FACE RECOGNITION
# ==========================================

def recognize_face(uploaded_file):

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    try:

        response = requests.post(
            API + "/recognize-face",
            files=files
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


# ==========================================
# SENTIMENT ANALYSIS
# ==========================================

def predict_sentiment(review):

    try:

        response = requests.post(
            API + "/predict-sentiment",
            json={
                "text": review
            }
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


# ==========================================
# CHATBOT
# ==========================================

def chatbot(message):

    try:

        response = requests.post(
            API + "/chat",
            json={
                "text": message
            }
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


# ==========================================
# SERVER STATUS
# ==========================================

def check_server():

    try:

        response = requests.get(API)

        if response.status_code == 200:

            return True

        return False

    except:

        return False