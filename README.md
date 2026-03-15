#  COVID-19 Detection Using CNN — Web Application

<p align="center">
<img src="https://media.giphy.com/media/l41lI4bYmcsPJX9Go/giphy.gif" width="600">
</p>

<p align="center">
Deep Learning • Medical Imaging • Django Web Application
</p>

---

#  About

This project is a **Django-based web application** that detects the presence of COVID-19 in **Chest X-Ray images** using **Convolutional Neural Networks (CNNs)**.

The deep learning models were trained on a publicly available dataset of approximately **2500 chest X-ray images**, labeled as:

* COVID-19
* Non-COVID

For comparison, three popular CNN architectures were used:

* **Xception**
* **ResNet50**
* **VGG16**

Each model was trained independently and the **trained weights were integrated into the web application** to perform real-time prediction on uploaded X-ray images.

---

#  System Workflow

<p align="center">
<img src="https://miro.medium.com/max/1400/1*XbuW8WuRrAY5p7x4p6pO2g.png" width="700">
</p>

### Pipeline

1. User uploads a **Chest X-Ray image**
2. Image preprocessing and normalization
3. CNN model extracts features
4. Model performs prediction
5. Output classification: **COVID-19 / Non-COVID**

---

#  Demo

<p align="center">
<img src="/Demo/demo.gif" alt="demo gif" width="700">
</p>

The web interface allows users to upload X-ray images and obtain instant predictions from trained CNN models.

---

#  Model Performance

##  ResNet50

### Model Architecture

<p align="center">
<img src="https://user-images.githubusercontent.com/53687927/118810680-c8b25600-b8c9-11eb-9d98-35baa3f3f42e.png">
</p>

### Loss Curves

<p align="center">
<img src="https://user-images.githubusercontent.com/53687927/118811264-6c036b00-b8ca-11eb-8105-c9c8673e3d6c.png">
</p>

### Confusion Matrix

<p align="center">
<img src="https://user-images.githubusercontent.com/53687927/118810998-1cbd3a80-b8ca-11eb-80c7-78a6ecbd2665.png">
</p>

---

##  VGG16

### Model Architecture

<p align="center">
<img src="https://user-images.githubusercontent.com/53687927/118811078-3494be80-b8ca-11eb-9948-7e06064030c3.png">
</p>

### Loss Curves

<p align="center">
<img src="https://user-images.githubusercontent.com/53687927/118811293-74f43c80-b8ca-11eb-9de3-d9380c082aea.png">
</p>

### Confusion Matrix

<p align="center">
<img src="https://user-images.githubusercontent.com/53687927/118811129-42e2da80-b8ca-11eb-9ed3-6c0126180241.png">
</p>

---

##  Xception

### Model Architecture

<p align="center">
<img src="https://user-images.githubusercontent.com/53687927/118811164-4fffc980-b8ca-11eb-8462-6dba7559e9ea.png">
</p>

### Loss Curves

<p align="center">
<img src="https://user-images.githubusercontent.com/53687927/118811317-7d4c7780-b8ca-11eb-87b3-c3d96955522a.png">
</p>

### Confusion Matrix

<p align="center">
<img src="https://user-images.githubusercontent.com/53687927/118811202-5aba5e80-b8ca-11eb-82f5-2f199909453d.png">
</p>

---

#  Dataset

Dataset used in this project:

**SARS-CoV-2 CT-Scan Dataset**

https://www.kaggle.com/plameneduardo/sarscov2-ctscan-dataset

Reference:

Soares, Eduardo, Angelov, Plamen, Biaso, Sarah, Higa Froes, Michele, and Kanda Abe, Daniel.
"SARS-CoV-2 CT-scan dataset: A large dataset of real patients CT scans for SARS-CoV-2 identification."
medRxiv (2020).
https://doi.org/10.1101/2020.04.24.20078584

Angelov, P., & Soares, E. (2020).
"Towards explainable deep neural networks (xDNN)."
Neural Networks, 130, 185-194.

---

#  Tech Stack

* **Python**
* **TensorFlow / Keras**
* **CNN Architectures**

  * ResNet50
  * VGG16
  * Xception
* **Django**
* **NumPy**
* **Pandas**
* **OpenCV**

---

#  Features

* Upload chest X-ray images
* Real-time COVID prediction
* Comparison of multiple CNN architectures
* Web interface built with Django
* Visualization of training metrics

---

#  Disclaimer

This project is intended **for research and educational purposes only** and should not be used as a medical diagnostic tool.

---

#  License

This project follows the **GPL-3.0 License**.

