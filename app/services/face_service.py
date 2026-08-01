import cv2
import joblib

# Load trained LBPH model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("app/models/face_recognizer.yml")

# Load label map
label_map = joblib.load("app/models/face_labels.pkl")


def recognize_face(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return {
            "error": "Could not read image."
        }

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize to training size (width=47, height=62)
    gray = cv2.resize(gray, (47, 62))

    label, confidence = recognizer.predict(gray)

    person = label_map.get(label, "Unknown")

    return {
        "person": person,
        "distance": round(float(confidence), 2)
    }