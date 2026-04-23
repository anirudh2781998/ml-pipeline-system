# 🚀 End-to-End ML Pipeline System (MLflow + FastAPI)

A production-style machine learning pipeline that demonstrates model training, experiment tracking, and deployment using modern MLOps tools. This project showcases how to build scalable ML systems from training to real-time inference.

---

## 🔍 Overview

This project implements a complete ML workflow:

* Data loading and preprocessing
* Model training and evaluation
* Experiment tracking using MLflow
* Model inference via REST API (FastAPI)

It simulates a real-world ML pipeline used in production systems.

---

## ⚙️ System Architecture

1. **Training Pipeline**

   * Loads dataset (Iris dataset)
   * Trains a classification model (Logistic Regression)
   * Logs parameters and metrics using MLflow

2. **Experiment Tracking (MLflow)**

   * Tracks model performance
   * Stores metrics and parameters
   * Enables reproducibility

3. **Inference Layer (FastAPI)**

   * Exposes trained model via REST API
   * Supports real-time predictions

---

## 🧠 Features

* 🔹 End-to-end ML workflow
* 🔹 Experiment tracking with MLflow
* 🔹 REST API for real-time predictions
* 🔹 Modular and extensible architecture
* 🔹 Designed with MLOps principles

---

## 🏗️ Tech Stack

* **Language:** Python
* **ML Library:** scikit-learn
* **MLOps:** MLflow
* **API:** FastAPI
* **Server:** Uvicorn

---

## 📂 Project Structure

```id="y4vbvd"
ml-pipeline-system/
│── train.py        # Model training + MLflow logging
│── predict.py      # Batch prediction script
│── app.py          # FastAPI inference server
│── requirements.txt
│── README.md
```

---

## ▶️ Getting Started

### 1. Clone the repository

```bash id="r4xkxp"
git clone https://github.com/anirudh2781998/ml-pipeline-system.git
cd ml-pipeline-system
```

---

### 2. Install dependencies

```bash id="9sqwxt"
pip install -r requirements.txt
```

---

### 3. Run training pipeline

```bash id="u2s0hv"
python train.py
```

👉 Logs will be tracked in MLflow

---

### 4. Start MLflow UI (optional)

```bash id="vgyk62"
mlflow ui
```

Open:

```id="74tfdz"
http://127.0.0.1:5000
```

---

### 5. Run inference API

```bash id="a1pf6y"
uvicorn app:app --reload
```

API runs at:

```id="rq9f1v"
http://127.0.0.1:8000
```

---

## 📡 API Usage

### Endpoint:

```id="s7rgx3"
GET /predict
```

### Example:

```id="p3n3n1"
http://localhost:8000/predict
```

### Sample Response:

```json id="q2a1cv"
{
  "prediction": 0
}
```

---

## ⚡ Performance Highlights

* Efficient training with minimal compute
* Real-time inference via REST API
* Experiment tracking for reproducibility
* Clean modular pipeline

---

## 🔒 Future Improvements

* Airflow DAG integration for pipeline orchestration
* Model versioning and registry (MLflow Registry)
* Docker-based deployment
* CI/CD integration
* Advanced models (XGBoost, Deep Learning)
* Feature store integration

---

## 👨‍💻 Author

**Anirudh Pandey**

* GitHub: https://github.com/anirudh2781998

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
