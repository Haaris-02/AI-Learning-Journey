<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:58A6FF,50:BC8CFF,100:3FB950&height=220&section=header&text=Handwritten%20Digit%20Classifier&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=A%20Deep%20Neural%20Network%20built%20with%20TensorFlow%20%26%20Keras&descAlignY=58&descSize=16" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=600&size=20&duration=2800&pause=900&color=58A6FF&center=true&vCenter=true&width=650&lines=Recognizing+handwritten+digits+0-9+with+97%25%2B+accuracy;Trained+on+60%2C000+MNIST+images;From+raw+pixels+to+real-time+prediction" alt="typing animation"/>

<br/>

![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-000000?style=for-the-badge&logo=python&logoColor=white)

![Accuracy](https://img.shields.io/badge/Test%20Accuracy-97.65%25-3fb950?style=flat-square)
![Dataset](https://img.shields.io/badge/Dataset-MNIST-58a6ff?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-bc8cff?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-8b949e?style=flat-square)

</div>

<br/>

## 📖 Table of Contents

- [Project Overview](#-project-overview)
- [Key Concepts Learned](#-key-concepts-learned)
- [Model Architecture](#️-model-architecture)
- [Dataset & Preprocessing](#-dataset--preprocessing)
- [How to Run Locally](#️-how-to-run-locally)
- [Sample Result & Output](#-sample-result--output)
- [Future Enhancements](#-future-enhancements)

<br/>

## 📌 Project Overview

This repository demonstrates a **Deep Neural Network (DNN)** built to recognize and classify handwritten digits (**0–9**) using the benchmark **MNIST dataset**.

Beyond standard dataset testing, this project includes a **real-time custom image inference pipeline** — draw a digit in MS Paint, scan it from paper, or drop in any grayscale image, and the model will predict what number it is.

<div align="center">

| 🎯 Goal | 📦 Input | 🧠 Model | ✅ Output |
|:---:|:---:|:---:|:---:|
| Classify digits 0–9 | 28×28 grayscale image | 3-layer Dense DNN | Predicted digit + confidence |

</div>

<br/>

## ⚡ Key Concepts Learned

<details open>
<summary><b>🤖 What is Deep Learning?</b></summary>
<br/>

**Deep Learning** is an advanced subset of Artificial Intelligence (AI) inspired by the human brain. Unlike traditional Machine Learning — which requires manual feature engineering — Deep Learning automatically learns hierarchical features directly from raw data using layered network architectures.

</details>

<details>
<summary><b>🧠 What is a Neural Network (ANN / DNN)?</b></summary>
<br/>

A **Neural Network** is a computational model made of interconnected nodes (artificial neurons), organized into layers:

- **Input Layer** — receives raw features (e.g. image pixels)
- **Hidden Layers** — perform mathematical transformations using **Weights (W)** and **Biases (b)**, passed through **Activation Functions** like ReLU
- **Output Layer** — generates final class probabilities using **Softmax**

> A network with more than one hidden layer is classified as a **Deep Neural Network (DNN)**.

</details>

<details>
<summary><b>⚙️ What is TensorFlow & Keras?</b></summary>
<br/>

- **TensorFlow** — Google's open-source, high-performance low-level framework for numerical computation and large-scale Machine Learning
- **Keras** (`tf.keras`) — a user-friendly, high-level Neural Network API built into TensorFlow, used here for rapid prototyping and model building

</details>

<br/>

## 🏗️ Model Architecture

<div align="center">
<img src="assets/architecture.svg" width="100%" alt="DNN architecture diagram — input, two hidden layers, output"/>
</div>

<br/>

| Layer | Type | Output Shape | Params | Activation |
|:---|:---|:---:|:---:|:---:|
| 1 | Flatten | 784 | 0 | — |
| 2 | Dense | 128 | 100,480 | ReLU |
| 3 | Dense | 64 | 8,256 | ReLU |
| 4 | Dense (Output) | 10 | 650 | Softmax |

```text
  [ Input Image ]  ──▶  28 × 28 Grayscale Image
         │
         ▼
  [ Flatten Layer ]  ──▶  Converts 2D matrix (28×28) into a 1D array of 784 pixels
         │
         ▼
  [ Dense Layer 1 ]  ──▶  128 Neurons | Activation: ReLU
         │
         ▼
  [ Dense Layer 2 ]  ──▶  64 Neurons  | Activation: ReLU
         │
         ▼
  [ Output Layer ]   ──▶  10 Neurons  | Activation: Softmax (probability for 0–9)
```

<br/>

## 📊 Dataset & Preprocessing

<div align="center">

| Metric | Details |
|:---|:---|
| 📚 Dataset | MNIST Handwritten Digits |
| 🏋️ Train Samples | 60,000 images |
| 🧪 Test Samples | 10,000 images |
| 🖼️ Image Resolution | 28 × 28 grayscale pixels |
| ⚖️ Normalization | Pixel values rescaled from `[0, 255]` → `[0.0, 1.0]` |

</div>

<br/>

## 🛠️ How to Run Locally

**1. Install dependencies**

```bash
pip install tensorflow pillow numpy matplotlib
```

**2. Run training & custom digit prediction**

Place your custom handwritten digit image (e.g. `digit.png`) in the project directory, then run:

```bash
python test_custom_image.py
```

<br/>

## 🎯 Sample Result & Output

```text
Training Model...
Epoch 1/3 - loss: 0.2541 - accuracy: 0.9258
Epoch 2/3 - loss: 0.1082 - accuracy: 0.9672
Epoch 3/3 - loss: 0.0754 - accuracy: 0.9765
---------------------------------
📷 Image Path: digit.png
🎯 Neural Network Prediction: NUMBER 8
🔥 Confidence: 59.50%
---------------------------------
```

> 💡 Lower confidence on custom hand-drawn digits is expected from a Dense network — this is exactly the gap the CNN upgrade below is designed to close.

<br/>

## 🚀 Future Enhancements

- [ ] Upgrade architecture from Dense Neural Network (DNN) to **Convolutional Neural Network (CNN)** for >99% prediction confidence
- [ ] Add a **Web GUI** using Streamlit / Flask to draw digits on screen in real time
- [ ] Add a confusion matrix + per-digit accuracy breakdown
- [ ] Deploy as a live demo (Streamlit Cloud / Hugging Face Spaces)

<br/>

<div align="center">

### 👤 Author

**Mohamad Alharis**
Freelance Django Developer & AI Voice Agent Builder · Building AI/ML skills one project at a time

[![GitHub](https://img.shields.io/badge/GitHub-Haaris--02-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Haaris-02)

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:3FB950,50:BC8CFF,100:58A6FF&height=100&section=footer" width="100%"/>

</div>