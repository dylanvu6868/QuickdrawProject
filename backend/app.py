
from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI()
model = tf.keras.models.load_model("quickdraw_model")
categories = ["apple", "banana", "cat", "dog", "car"]

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("L")
    image = image.resize((28,28))
    image = np.array(image).astype(np.float32) / 255.0
    image = np.expand_dims(image, axis=[0, -1])

    predictions = model.predict(image)
    predicted_label = categories[np.argmax(predictions)]

    return {"prediction": predicted_label, "confidence": float(np.max(predictions))}
