from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter(prefix="/feedback", tags=["Feedback"])

class FeedbackRequest(BaseModel):
    prediction_id: str
    correct_label: str  # "Fresh" | "Moderately Fresh" | "Spoiled"

@router.post("/")
def submit_feedback(body: FeedbackRequest):
    # TODO: store to DB for future retraining
    return {"status": "received"}
