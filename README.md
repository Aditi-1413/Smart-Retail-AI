# 🛍 Smart Retail AI Platform

## Overview

Smart Retail AI is an AI-powered retail assistant that integrates multiple machine learning and deep learning models into a single platform. It provides product classification, face recognition, sentiment analysis, and an AI chatbot through a FastAPI backend and a Streamlit frontend.

---

## Features

### 👕 Product Classification
- CNN Model
- Fashion-MNIST Dataset
- Predicts 10 clothing categories

### 🙂 Face Recognition
- OpenCV LBPH Face Recognizer
- LFW Dataset
- Identifies known individuals

### ⭐ Sentiment Analysis
- LSTM Neural Network
- IMDB Movie Reviews Dataset
- Predicts Positive/Negative sentiment

### 🤖 AI Chatbot
- Intent Classification
- TensorFlow Model
- Retail support assistant

### 📈 Analytics Dashboard
- Model accuracy comparison
- Dataset statistics
- System status
- Performance metrics

---

## Technologies Used

- Python
- TensorFlow
- OpenCV
- Scikit-learn
- FastAPI
- Streamlit
- Plotly
- NumPy
- Pandas

---

## Project Structure

```
smart-retail-ai/
│
├── app/
├── frontend/
├── notebooks/
├── models/
├── uploads/
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone <repository-url>

cd smart-retail-ai

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Run Backend

```bash
python -m uvicorn app.main:app --reload
```

Run Frontend

```bash
cd frontend

streamlit run app.py
```

---

## API

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Developed By

Aditi Mishra