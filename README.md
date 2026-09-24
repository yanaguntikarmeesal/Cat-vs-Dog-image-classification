# 🐱🐶 Cat vs Dog Image Classification

A **Deep Learning Image Classification** project that classifies images as either **Cat 🐱 or Dog 🐶** using **VGG16 Transfer Learning**, **TensorFlow**, and **Streamlit**.

## 🚀 Project Demo

The project provides an interactive Streamlit web application where users can upload an image and receive:

* 🐱 Cat / 🐶 Dog prediction
* 📊 Prediction confidence
* 📈 Cat and Dog probabilities
* 🖼️ Uploaded image preview
* 📋 Image format and dimensions
* 🧠 Model architecture details

---

## 📌 Project Overview

The application uses a pretrained **VGG16** convolutional neural network with **ImageNet transfer learning**.

The uploaded image is:

```text
Uploaded Image
      ↓
Convert to RGB
      ↓
Resize to 224 × 224
      ↓
NumPy Array
      ↓
VGG16 Model
      ↓
Binary Classification
      ↓
Cat 🐱 / Dog 🐶
```

---

## 🧠 Model Architecture

```text
VGG16
   ↓
Flatten
   ↓
Dense(256, ReLU)
   ↓
Dense(1, Sigmoid)
   ↓
Cat / Dog
```

### Model Configuration

| Parameter         | Value               |
| ----------------- | ------------------- |
| Model             | VGG16               |
| Transfer Learning | ImageNet            |
| Input Size        | 224 × 224 × 3       |
| Classification    | Binary              |
| Optimizer         | Adam                |
| Loss              | Binary Crossentropy |
| Classes           | Cat, Dog            |
| Epochs            | 5                   |

---

## ✨ Features

* 🐱 Cat classification
* 🐶 Dog classification
* 🧠 VGG16 transfer learning
* ⚡ TensorFlow/Keras
* 🖼️ Image upload
* 📊 Confidence score
* 📈 Class probabilities
* 🎨 Custom CSS interface
* 🌈 Project banner
* 📋 Image information
* 📚 Model architecture information
* 📱 Wide Streamlit layout

---

## 🛠️ Technologies

* Python
* TensorFlow
* Keras
* VGG16
* NumPy
* Pillow
* Streamlit

---

## 📁 Repository Structure

```text
Cat-Vs-Dog-Image-Classification/
│
├── app.py
├── catvsdog.h5
├── requirements.txt
├── README.md
└── screenshots/
    └── cat-vs-dog.png
```

### Files

**`app.py`**
Main Streamlit application.

**`catvsdog.h5`**
Trained TensorFlow/Keras model.

**`requirements.txt`**
Required Python packages.

**`README.md`**
Project documentation.

---

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Cat-Vs-Dog-Image-Classification.git
```

### 2. Open the project

```bash
cd Cat-Vs-Dog-Image-Classification
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 requirements.txt

```text
streamlit
tensorflow
numpy
pillow
```

---

## ▶️ Run the Application

Run the following command:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 🖼️ Supported Images

The application supports:

```text
.jpg
.jpeg
.png
.bmp
.webp
```

---

## 📊 Prediction

The model produces a binary probability.

```python
if prediction >= 0.5:
    predicted_class = "Dog"
    confidence = prediction
else:
    predicted_class = "Cat"
    confidence = 1 - prediction
```

### Example

```text
Prediction: 🐱 Cat
Confidence: 98.25%

Cat: 98.25%
Dog: 1.75%
```

or:

```text
Prediction: 🐶 Dog
Confidence: 96.80%

Cat: 3.20%
Dog: 96.80%
```

The actual prediction depends on the uploaded image and trained model.

---

## 🖼️ Image Preprocessing

Each uploaded image is converted to RGB and resized:

```python
image = image.convert("RGB")

image = image.resize((224, 224))

image_array = np.array(
    image,
    dtype=np.float32
)

image_array = np.expand_dims(
    image_array,
    axis=0
)
```

The final input shape is:

```text
1 × 224 × 224 × 3
```

---

## 🎨 Streamlit Interface

The application contains:

### 🐾 Sidebar

Displays:

* Project information
* Model information
* Dataset classes
* Input dimensions
* Optimizer
* Loss function

### 📤 Upload Section

Users can upload a Cat or Dog image.

### 🖼️ Image Information

Displays:

* Image format
* Image width
* Image height

### 🔍 Prediction

Displays:

* Predicted class
* Confidence
* Raw probability

### 📈 Class Probabilities

Displays:

```text
🐱 Cat
🐶 Dog
```

with progress indicators.

### 🧠 Model Architecture

Shows the VGG16 transfer-learning structure.

---

## 🎯 Learning Objectives

This project demonstrates:

* Convolutional Neural Networks
* Image Classification
* Transfer Learning
* VGG16
* TensorFlow/Keras
* Binary Classification
* Image Preprocessing
* Model Prediction
* Streamlit
* Machine Learning Web Applications

---

## 🔮 Future Improvements

* 📷 Webcam classification
* 📁 Multiple-image prediction
* 📊 Training accuracy/loss visualization
* 📈 Confusion matrix
* 🔄 Model comparison
* 🐾 More animal classes
* ☁️ Streamlit Cloud deployment
* 🤗 Hugging Face model deployment

---

## ⚠️ Model File

The application expects:

```text
catvsdog.h5
```

in the same directory as:

```text
app.py
```

If the file is missing, the application will display:

```text
Model file catvsdog.h5 was not found.
```

For a large `.h5` file, Git LFS or external model hosting can be used.

---

## 👨‍💻 Author

**Yanaguntikar**

### 🐱🐶 Cat vs Dog Image Classification

Built using:

```text
Python
TensorFlow
VGG16
NumPy
Pillow
Streamlit
```

---

## ⭐ GitHub

If you find this project useful for learning **Deep Learning, Computer Vision, VGG16, TensorFlow, and Streamlit**, consider giving the repository a ⭐.
