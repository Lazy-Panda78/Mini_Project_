from fastapi import APIRouter, UploadFile, File
router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("/")
async def predict(file: UploadFile = File(...)):
    # TODO: preprocess image, run model, return result
    return {"label": "TODO", "confidence": 0.0, "scores": {}}
