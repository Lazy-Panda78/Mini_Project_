<<<<<<< HEAD
<div align="center">

# 🥦 Unified Food Freshness Classification System

**A Full-Stack · AI/ML · Cloud-Deployed solution for automated food freshness detection**

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?logo=fastapi)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13-FF6F00?logo=tensorflow)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![AWS](https://img.shields.io/badge/AWS-EC2+S3-FF9900?logo=amazonaws)
![License](https://img.shields.io/badge/License-MIT-green)

[Live Demo](#) · [API Docs](#api-documentation) · [Report Issue](#)

</div>

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [ML Model](#ml-model)
- [Cloud Deployment](#cloud-deployment)
- [Team](#team)

---

## Overview

This project implements a **unified AI-based food freshness classification system** capable of assessing the freshness of fruits, vegetables, meat, and dairy products using:

- 🖼️ **Computer Vision** — MobileNetV2-based CNN trained on freshness image datasets
- 📡 **Sensor Fusion** — Integration of temperature, humidity, CO₂, and pH sensor readings
- ⚡ **Real-time Prediction** — Sub-200ms inference via a REST API
- ☁️ **Cloud-Hosted** — Backend on AWS EC2, model artifacts on S3, frontend on Vercel

**Freshness Classes:** `Fresh` · `Moderately Fresh` · `Spoiled`

---

## Features

- 📷 Drag-and-drop image upload for instant freshness analysis
- 🌡️ Optional sensor data input (temperature, humidity, CO₂, pH)
- 📊 Confidence scores for each freshness class
- 📁 Prediction history with analytics dashboard
- 🔄 Feedback loop for model improvement
- 🐳 Fully Dockerized for consistent deployment

---

## System Architecture

```
┌─────────────────┐        ┌──────────────────────┐        ┌─────────────────┐
│   React Frontend│  HTTP  │  FastAPI Backend      │  Load  │  ML Model       │
│   (Vercel)      │◄──────►│  (AWS EC2 + Docker)   │◄──────►│  (TensorFlow)   │
└─────────────────┘        └──────────────────────┘        └─────────────────┘
                                      │                              │
                              ┌───────▼──────┐              ┌───────▼──────┐
                              │  PostgreSQL  │              │   AWS S3     │
                              │  (AWS RDS)   │              │ Model Store  │
                              └──────────────┘              └──────────────┘
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 18, Tailwind CSS, Recharts |
| Backend | FastAPI (Python 3.10), Uvicorn |
| ML / AI | TensorFlow 2.13, MobileNetV2, scikit-learn |
| Database | PostgreSQL (AWS RDS) |
| Cloud | AWS EC2, S3, RDS |
| Frontend Hosting | Vercel |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |

---

## Project Structure

```
freshness-classifier/
├── frontend/                   # React.js application
│   ├── src/
│   │   ├── components/         # Reusable UI components
│   │   ├── pages/              # Route-level pages
│   │   ├── utils/              # API helpers, formatters
│   │   └── assets/             # Images, icons
│   └── package.json
│
├── backend/                    # FastAPI application
│   ├── main.py                 # App entry point
│   ├── routes/                 # API route handlers
│   ├── models/                 # DB models (SQLAlchemy)
│   ├── utils/                  # Preprocessing, inference helpers
│   ├── tests/                  # Unit & integration tests
│   └── requirements.txt
│
├── ml/                         # Machine Learning
│   ├── notebooks/              # Jupyter notebooks (EDA, training)
│   ├── scripts/                # train.py, evaluate.py, preprocess.py
│   ├── models/                 # Saved model files (.h5)
│   └── data/                   # raw/ and processed/ datasets
│
├── cloud/                      # Infrastructure & deployment
│   ├── aws/                    # AWS configs (EC2 setup, S3 policy)
│   ├── docker/                 # Dockerfiles
│   └── .github/workflows/      # CI/CD pipelines
│
├── docs/                       # Documentation
│   ├── diagrams/               # Architecture diagrams
│   └── api/                    # API reference docs
│
├── docker-compose.yml          # Local dev orchestration
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- Docker & Docker Compose
- Git

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/freshness-classifier.git
cd freshness-classifier
```

### 2. Run with Docker (Recommended)

```bash
docker-compose up --build
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### 3. Run Manually

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

---

## API Documentation

Interactive docs available at `/docs` (Swagger UI) when the backend is running.

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/predict` | Classify food freshness from image |
| `GET` | `/health` | API health check |
| `POST` | `/feedback` | Submit correction for a prediction |
| `GET` | `/history` | Retrieve past predictions |
| `GET` | `/categories` | List supported food categories |

**Example request:**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@apple.jpg"
```

**Example response:**
```json
{
  "label": "Fresh",
  "confidence": 0.94,
  "scores": {
    "Fresh": 0.94,
    "Moderately Fresh": 0.05,
    "Spoiled": 0.01
  }
}
```

---

## ML Model

- **Base Model:** MobileNetV2 pretrained on ImageNet
- **Fine-tuned on:** Fruits & Vegetables Freshness Dataset (Kaggle)
- **Input:** 224×224 RGB image + optional 4-sensor vector
- **Output:** 3-class softmax (Fresh / Moderately Fresh / Spoiled)
- **Accuracy:** ~XX% (update after training)

Training details in `ml/notebooks/training.ipynb`

---

## Cloud Deployment

| Component | Service | Status |
|---|---|---|
| Backend API | AWS EC2 (t2.medium) | 🟡 In Progress |
| Model Storage | AWS S3 | 🟡 In Progress |
| Database | AWS RDS (PostgreSQL) | 🟡 In Progress |
| Frontend | Vercel | 🟡 In Progress |
| CI/CD | GitHub Actions | 🟡 In Progress |

---

## Team

| Name | Role |
|---|---|
| [Your Name] | ML Engineer / Full-Stack |
| [Team Member 2] | Backend Developer |
| [Team Member 3] | Frontend Developer |

---

<div align="center">
Made for Machine Learning Mini Project · 3 Academic Credits
</div>
=======
# Mini_Project_
## _**FreshVision: AI-Based Food Quality Classifier**_ -
Unified Comprehensive Freshness Classification System for Diverse Food Categories
>>>>>>> 601763a664d023a2f4596efa3ba16279d004bce1
