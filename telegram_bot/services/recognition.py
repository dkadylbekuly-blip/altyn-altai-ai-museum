import json
from pathlib import Path

import torch
from PIL import Image
from torchvision import models, transforms

from bot_config import MODEL_PATH, CLASS_NAMES_PATH


_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_model = None
_class_names = None


def _load_class_names():
    global _class_names

    if _class_names is None:
        with open(CLASS_NAMES_PATH, "r", encoding="utf-8") as f:
            _class_names = json.load(f)

    return _class_names


def _load_model():
    global _model

    if _model is not None:
        return _model

    class_names = _load_class_names()
    num_classes = len(class_names)

    model = models.resnet18(weights=None)
    model.fc = torch.nn.Linear(model.fc.in_features, num_classes)

    state = torch.load(MODEL_PATH, map_location=_device)
    model.load_state_dict(state)

    model.to(_device)
    model.eval()

    _model = model
    return _model


_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225],
    ),
])


def recognize_image(image_path: str):
    model = _load_model()
    class_names = _load_class_names()

    image = Image.open(image_path).convert("RGB")
    tensor = _transform(image).unsqueeze(0).to(_device)

    with torch.no_grad():
        outputs = model(tensor)
        probabilities = torch.softmax(outputs, dim=1)[0]
        top_probs, top_indices = torch.topk(probabilities, k=3)

    top3 = []
    for prob, idx in zip(top_probs, top_indices):
        name = class_names[int(idx)]
        confidence = float(prob.item()) * 100
        top3.append({
            "name": name,
            "confidence": confidence,
        })

    return {
        "name": top3[0]["name"],
        "confidence": top3[0]["confidence"],
        "top3": top3,
    }