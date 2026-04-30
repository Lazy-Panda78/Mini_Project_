# 🍎 FreshVision — Fruit Freshness Classification System

> Full-Stack · AI/ML · Cloud-Deployed · GLA University ML Mini Project 2025–26

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)](https://flask.palletsprojects.com)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?logo=pytorch)](https://pytorch.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)](https://docker.com)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Spaces-FFD21E?logo=huggingface)](https://huggingface.co/spaces/Lazypanda0103/freshvision-app)

---

## 🔗 Live Links

- 🎯 Hugging Face Demo  
  https://huggingface.co/spaces/Lazypanda0103/freshvision-app  

- 🌐 Flask Web App (Render)  
  https://freshness-classifier-qj3t.onrender.com/

---

## 📌 Overview

FreshVision is an AI-powered fruit freshness classification system that predicts whether a fruit is Fresh or Rotten from an image using deep learning.

The system is designed for:
- Real-world reliability  
- Clean deployment  
- User-friendly interaction  

---

## 🎯 Key Features

- 🧠 ResNet18 model (PyTorch)
- 📷 Image-based prediction
- 📊 Confidence score + top predictions
- 🚨 Confidence-based rejection (Unknown detection)
- 🔐 User authentication + history tracking
- 🌐 Hugging Face + Render deployment
- 🐳 Dockerized backend
- ⚙️ CI/CD with GitHub Actions

---

## 🏗️ System Architecture


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
├── High → Prediction
└── Low → Unknown


---

## ⚙️ Tech Stack

| Layer | Technology |
|------|-----------|
| Backend | Flask, Gunicorn |
| Frontend | Jinja2, Bootstrap |
| ML | PyTorch, ResNet18 |
| Database | SQLite |
| Deployment | Render, HuggingFace |
| CI/CD | GitHub Actions |
| Container | Docker |

---

## 📁 Project Structure


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


---

## 🚀 Getting Started

### 1️⃣ Clone

```bash
git clone https://github.com/Lazy-Panda78/Mini_Project_.git
cd Mini_Project_
2️⃣ Install & Run
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py

Open → http://localhost:5000

3️⃣ Docker Run
docker build -t freshvision .
docker run -p 5000:5000 freshvision
🧠 ML Model
Detail	Value
Model	ResNet18 (PyTorch)
Input Size	224 × 224
Output Classes	6 (Fresh/Rotten × Fruits)
Format	.pth
Training	Transfer Learning
Activation	Softmax
Loss	Cross Entropy
🚨 Confidence Handling
if confidence < 0.75:
    return "Unknown"

Prevents incorrect predictions on:

Non-fruit images
Low-quality inputs
Out-of-distribution data
☁️ Cloud Deployment
Component	Service	Status
ML Model	HuggingFace Spaces	✅ Live
Flask App	Render.com	✅ Live
CI/CD	GitHub Actions	✅ Active
🧪 Demo
Upload fruit → prediction
Upload random image → rejection
👨‍💻 Team
Name	Role
Yash Upadhyay	ML & Deployment
Siddhi Singh	Backend
Sanya Singh	Frontend
🧠 Key Learnings
ML deployment challenges
Preprocessing consistency
Handling unknown inputs
CI/CD integration
⭐ Conclusion

FreshVision demonstrates a production-ready AI system combining:

Deep learning
Full-stack development
Cloud deployment

GLA University · ML Mini Project · 2025–26
