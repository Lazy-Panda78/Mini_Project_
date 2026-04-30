# 🍎 FreshVision — Fruit Freshness Classification System

> **Full-Stack · AI/ML · Cloud-Deployed · GLA University ML Mini Project 2025–26**

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)](https://flask.palletsprojects.com)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?logo=pytorch)](https://pytorch.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)](https://docker.com)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Spaces-FFD21E?logo=huggingface)](https://huggingface.co/spaces/Lazypanda0103/freshvision-app)

---

## 🔗 Live Links

| Platform | URL |
|---|---|
| 🎯 Hugging Face Demo | [freshvision-app](https://huggingface.co/spaces/Lazypanda0103/freshvision-app) |
| 🌐 Flask Web App (Render) | [freshness-classifier-qj3t.onrender.com](https://freshness-classifier-qj3t.onrender.com/) |

---

## 📌 Overview

**FreshVision** is an AI-powered fruit freshness classification system that predicts whether a fruit is **Fresh** or **Rotten** from an image using deep learning.

The system is designed for:
- ✅ Real-world reliability
- ✅ Clean, scalable deployment
- ✅ User-friendly interaction

---

## 🎯 Key Features

| Feature | Description |
|---|---|
| 🧠 ResNet18 Model | PyTorch-based transfer learning |
| 📷 Image-based Prediction | Upload any fruit image for instant classification |
| 📊 Confidence Scoring | Top predictions with probability scores |
| 🚨 Unknown Detection | Confidence-based rejection for out-of-distribution inputs |
| 🔐 Auth & History | User authentication with prediction history tracking |
| 🌐 Dual Deployment | Hosted on Hugging Face Spaces + Render |
| 🐳 Dockerized | Fully containerized backend |
| ⚙️ CI/CD | Automated pipeline via GitHub Actions |

---

## 🏗️ System Architecture

```
User Input (Image)
        │
        ▼
Flask Web App (Render)
        │
        ▼
Preprocessing (Resize + Normalize)
        │
        ▼
ResNet18 Model (PyTorch)
        │
        ▼
Softmax Probabilities
        │
        ▼
Confidence Thresholding
    ├── High Confidence  →  Prediction Returned
    └── Low Confidence   →  "Unknown" Returned
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Flask, Gunicorn |
| Frontend | Jinja2, Bootstrap |
| ML Framework | PyTorch, ResNet18 |
| Database | SQLite |
| Deployment | Render, Hugging Face Spaces |
| CI/CD | GitHub Actions |
| Containerization | Docker |

---

## 📁 Project Structure

```
Mini_Project_/
│
├── run.py
├── requirements.txt
├── Dockerfile
│
├── app/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── predict.py
│   │   └── history.py
│   │
│   ├── models/
│   │   └── database.py
│   │
│   ├── utils/
│   │   ├── inference.py
│   │   └── preprocess.py
│   │
│   ├── templates/
│   └── static/
│
├── tests/
├── model.py
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Lazy-Panda78/Mini_Project_.git
cd Mini_Project_
```

### 2️⃣ Install Dependencies & Run

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the app
python run.py
```

Open your browser at → **http://localhost:5000**

### 3️⃣ Run with Docker

```bash
docker build -t freshvision .
docker run -p 5000:5000 freshvision
```

---

## 🧠 ML Model Details

| Property | Value |
|---|---|
| Model Architecture | ResNet18 (PyTorch) |
| Input Size | 224 × 224 px |
| Output Classes | 6 (Fresh / Rotten × 3 Fruits) |
| Model Format | `.pth` |
| Training Strategy | Transfer Learning |
| Output Activation | Softmax |
| Loss Function | Cross Entropy |

---

## 🚨 Confidence-Based Rejection

To prevent incorrect predictions on non-fruit or low-quality images, a confidence threshold is applied:

```python
if confidence < 0.75:
    return "Unknown"
```

This guards against:
- 🖼️ Non-fruit images
- 📉 Low-quality or blurry inputs
- 🔀 Out-of-distribution data

---

## ☁️ Cloud Deployment

| Component | Service | Status |
|---|---|---|
| ML Model | Hugging Face Spaces | ✅ Live |
| Flask App | Render.com | ✅ Live |
| CI/CD Pipeline | GitHub Actions | ✅ Active |

---

## 🧪 Demo Scenarios

| Input | Expected Output |
|---|---|
| 🍎 Fresh apple image | `Fresh Apple — 94% confidence` |
| 🍌 Rotten banana image | `Rotten Banana — 88% confidence` |
| 🖼️ Random non-fruit image | `Unknown — confidence too low` |

---

## 👨‍💻 Team

| Name | Role |
|---|---|
| Yash Upadhyay | ML Engineering & Deployment |
| Siddhi Singh | Backend Development |
| Sanya Singh | Frontend Development |

---

## 🧠 Key Learnings

- Challenges of deploying ML models in production
- Importance of preprocessing consistency across training and inference
- Handling unknown / out-of-distribution inputs gracefully
- Integrating CI/CD pipelines for automated testing and deployment

---

## ⭐ Conclusion

**FreshVision** demonstrates a production-ready AI system that combines:

- 🤖 Deep learning with transfer learning (ResNet18)
- 🏗️ Full-stack web development (Flask + Bootstrap)
- ☁️ Cloud deployment on Render & Hugging Face
- 🔁 Automated CI/CD with Docker & GitHub Actions

---

<div align="center">

**GLA University · ML Mini Project · 2025–26**

Made with ❤️ by Team FreshVision

</div>
