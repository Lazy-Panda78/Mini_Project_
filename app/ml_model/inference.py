import torch
import torch.nn as nn
from torchvision.models import resnet18, ResNet18_Weights
from torchvision import transforms
from PIL import Image
import torch.nn.functional as F
import os

# ===== CONFIG =====
CONF_THRESHOLD = 0.75  # adjust if needed

# ===== DEVICE =====
device = torch.device("cpu")

# ===== CLASSES =====
classes = [
    'freshapples', 'freshbanana', 'freshoranges',
    'rottenapples', 'rottenbanana', 'rottenoranges'
]

# ===== MODEL (Lazy Loading) =====
model = None

def _load_model():
    """Load model lazily on first prediction to save startup memory."""
    global model
    if model is None:
        model = resnet18(weights=ResNet18_Weights.DEFAULT)
        model.fc = nn.Linear(model.fc.in_features, 6)
        
        # Get absolute path to the model file
        model_path = os.path.join(os.path.dirname(__file__), 'best_model.pth')
        model.load_state_dict(torch.load(model_path, map_location=device))
        model.eval()
    return model

# ===== TRANSFORM =====
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# ===== PREDICTION FUNCTION =====
def predict_image(image: Image.Image):
    model = _load_model()
    image = image.convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image)
        probs = F.softmax(outputs, dim=1)[0]

    best_idx = torch.argmax(probs).item()
    confidence = probs[best_idx].item()
    label = classes[best_idx]

    # 🚨 UNKNOWN DETECTION (MAIN FIX)
    if confidence < CONF_THRESHOLD:
        return {
            "fruit": "Unknown",
            "condition": "Uncertain",
            "confidence": round(confidence * 100, 2)
        }

    # ✅ NORMAL CASE
    condition = "Fresh" if "fresh" in label else "Rotten"
    fruit = label.replace("fresh", "").replace("rotten", "")

    return {
        "fruit": fruit.capitalize(),
        "condition": condition,
        "confidence": round(confidence * 100, 2)
    }