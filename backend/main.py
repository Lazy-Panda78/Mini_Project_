"""
Freshness Classifier – FastAPI Backend  |  Entry Point
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Food Freshness Classification API",
    description="Multimodal AI system for classifying food freshness across fruits, vegetables, meat and dairy.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # TODO: restrict to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok", "version": "1.0.0"}

# TODO: uncomment once routes are implemented
# from routes import predict, history, feedback
# app.include_router(predict.router)
# app.include_router(history.router)
# app.include_router(feedback.router)
