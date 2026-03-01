"""Image preprocessing utilities."""
# import numpy as np
# from PIL import Image
# import io

def preprocess_image(image_bytes: bytes):
    """Resize to 224x224 and normalize pixel values to [0,1]."""
    # img = Image.open(io.BytesIO(image_bytes)).convert("RGB").resize((224, 224))
    # return np.expand_dims(np.array(img) / 255.0, axis=0)
    pass
