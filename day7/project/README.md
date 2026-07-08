<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=SMS%20Spam%20Detection%20Pipeline&fontSize=40&fontColor=fff&animation=twinkling&fontAlignY=35&desc=An%20End-to-End%20NLP%20Classifier%20for%20Spam%20vs%20Ham&descAlignY=55&descSize=18)

![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&lines=%F0%9F%93%A9+Classifying+SMS+as+Spam+or+Ham;%F0%9F%A7%A0+CountVectorizer+%2B+Naive+Bayes;%E2%9A%A1+98.57%25+Accuracy+Achieved%21)

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![HuggingFace](https://img.shields.io/badge/🤗%20Datasets-HuggingFace-FFD21E?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

![Stars](https://img.shields.io/github/stars/your-username/sms-spam-detector?style=social)
![Forks](https://img.shields.io/github/forks/your-username/sms-spam-detector?style=social)

</div>

---

## 📑 Table of Contents

- [🎯 Objective](#-objective)
- [🛠️ Tech Stack](#️-tech-stack--libraries)
- [🔄 How It Works](#-how-it-works)
- [🧠 Key Concepts](#-key-concepts-implemented)
- [📊 Model Performance](#-model-performance)
- [📂 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [🤝 Connect](#-connect-with-me)

---

## 🎯 Objective

This project is an end-to-end **Natural Language Processing (NLP)** pipeline that classifies SMS messages as either:

| Label | Meaning |
|:---:|:---|
| 🚫 **Spam** | Fraudulent / promotional messages |
| ✅ **Ham** | Normal, legitimate messages |

---

## 🛠️ Tech Stack & Libraries

<div align="center">

| Purpose | Tool |
|:---|:---|
| 🐍 Language | `Python` |
| 🐼 Data Manipulation | `pandas` |
| 🤖 Machine Learning | `scikit-learn` (CountVectorizer, MultinomialNB) |
| 📦 Data Sourcing | `datasets` (Hugging Face) |

</div>

---

## 🔄 How It Works

```mermaid
graph LR
    A[📥 Load Dataset<br/>Hugging Face] --> B[🧹 Preprocess & Save<br/>spam.csv]
    B --> C[✂️ Train-Test Split<br/>80% / 20%]
    C --> D[🔢 CountVectorizer<br/>Bag of Words]
    D --> E[🤖 Train MultinomialNB]
    E --> F[📊 Evaluate<br/>Accuracy · Precision · Recall]
    F --> G{✅ Prediction}
    G --> H[🚫 Spam]
    G --> I[✅ Ham]

    style A fill:#6C63FF,color:#fff
    style E fill:#F7931E,color:#fff
    style H fill:#FF4D4D,color:#fff
    style I fill:#00C48C,color:#fff
```

---

## 🧠 Key Concepts Implemented

1. **📥 Data Ingestion** — Fetched modern SMS spam data from Hugging Face and processed it into a `.csv` file.
2. **✂️ Train-Test Split** — Divided the dataset (80% training, 20% testing) for unbiased evaluation.
3. **🔢 Text Vectorization** — Used `CountVectorizer` to convert text messages into numerical token counts (Bag of Words).
4. **🤖 Model Training** — Trained a `MultinomialNB` (Naive Bayes) classifier, efficient for text classification based on word probabilities.
5. **📊 Evaluation Metrics** — Analyzed the model using Accuracy, Precision, and Recall.

---

## 📊 Model Performance

<div align="center">

![Accuracy](https://img.shields.io/badge/Accuracy-98.57%25-brightgreen?style=for-the-badge)
![Precision](https://img.shields.io/badge/Precision-97%25-blue?style=for-the-badge)
![Recall](https://img.shields.io/badge/Recall-93%25-orange?style=for-the-badge)

| Metric | Score | Notes |
|:---|:---:|:---|
| ✅ Accuracy | **98.57%** | Overall correctness of the model |
| 🎯 Precision (Spam) | **97%** | Prioritized to prevent normal messages landing in spam |
| 📥 Recall (Spam) | **93%** | Ability to catch actual spam messages |

</div>

---

## 📂 Project Structure

```text
├── spam.csv        # Dataset downloaded and parsed from Hugging Face
├── pipeline.py      # Main Python script for vectorization, training, and testing
└── README.md        # Project documentation
```

---

## 🚀 Getting Started

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/sms-spam-detector.git
cd sms-spam-detector

# 2️⃣ Install dependencies
pip install pandas scikit-learn datasets

# 3️⃣ Run the pipeline
python pipeline.py
```

---

## 🤝 Connect with Me

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-profile)
[![Fiverr](https://img.shields.io/badge/Fiverr-1DBF73?style=for-the-badge&logo=fiverr&logoColor=white)](https://fiverr.com/your-profile)
[![Upwork](https://img.shields.io/badge/Upwork-14A800?style=for-the-badge&logo=upwork&logoColor=white)](https://upwork.com/freelancers/your-profile)

</div>

![footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer)

