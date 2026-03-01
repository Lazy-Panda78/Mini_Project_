from fastapi import APIRouter
router = APIRouter(prefix="/history", tags=["History"])

@router.get("/")
def get_history(limit: int = 20):
    # TODO: query PostgreSQL for prediction records
    return {"predictions": [], "total": 0}
