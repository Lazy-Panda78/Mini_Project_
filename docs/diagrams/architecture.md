# System Architecture

```
React Frontend (Vercel)
        |
        | HTTPS REST
        v
FastAPI Backend (AWS EC2 + Docker)
        |             |
        v             v
  PostgreSQL      TensorFlow Model
  (AWS RDS)       loaded from S3
```

TODO: Replace with a proper diagram image (use draw.io or Excalidraw).
