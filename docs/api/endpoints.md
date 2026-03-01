# API Reference

## POST /predict
Classify freshness from an uploaded image.

**Request:** `multipart/form-data` with `file` field (JPEG/PNG)

**Response:**
```json
{
  "label": "Fresh",
  "confidence": 0.94,
  "scores": { "Fresh": 0.94, "Moderately Fresh": 0.05, "Spoiled": 0.01 }
}
```

## GET /health
Returns API status and model version.

## GET /history
Returns list of past predictions. Query param: `?limit=20`

## POST /feedback
Submit a correction for a prediction.

## GET /categories
Returns supported food categories.
