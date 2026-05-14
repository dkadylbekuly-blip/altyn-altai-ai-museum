import json
from pathlib import Path

import numpy as np
import tensorflow as tf
from PIL import Image


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "ml" / "mineral_model.keras"
CLASS_NAMES_PATH = BASE_DIR / "data" / "class_names.json"

IMG_SIZE = 224
CONFIDENCE_THRESHOLD = 55.0

_model = None
_class_names = None


def load_model_once():
    global _model, _class_names

    if _model is None:
        _model = tf.keras.models.load_model(MODEL_PATH)

    if _class_names is None:
        with open(CLASS_NAMES_PATH, "r", encoding="utf-8") as f:
            _class_names = json.load(f)

    return _model, _class_names


def prepare_image(image_path: str):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE))

    arr = np.array(img).astype("float32") / 255.0
    arr = np.expand_dims(arr, axis=0)

    return arr


def predict_image(image_path: str):
    model, class_names = load_model_once()

    arr = prepare_image(image_path)
    predictions = model.predict(arr, verbose=0)[0]

    top_indices = predictions.argsort()[-5:][::-1]

    top5 = []
    for idx in top_indices:
        top5.append({
            "name": class_names[int(idx)],
            "confidence": round(float(predictions[int(idx)] * 100), 2)
        })

    best = top5[0]

    result_name = best["name"]
    if best["confidence"] < CONFIDENCE_THRESHOLD:
        result_name = "unknown"

    return {
        "name": result_name,
        "confidence": best["confidence"],
        "top3": top5[:3],
        "top5": top5,
        "model_status": "production",
    }