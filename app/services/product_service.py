import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

MODEL_PATH = "app/models/product_classifier.h5"

model = load_model(MODEL_PATH)

CLASS_NAMES = [
    "T-shirt/Top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle Boot"
]

def predict_product(img_path):

    img = image.load_img(
        img_path,
        color_mode="grayscale",
        target_size=(28, 28)
    )

    img = image.img_to_array(img)      # Shape: (28, 28, 1)

    img = img.astype("float32") / 255.0

    img = np.expand_dims(img, axis=0)  # Shape: (1, 28, 28, 1)

    prediction = model.predict(img, verbose=0)

    predicted_class = np.argmax(prediction)

    confidence = float(np.max(prediction))

    return {
        "product": CLASS_NAMES[predicted_class],
        "confidence": round(confidence, 4)
    }