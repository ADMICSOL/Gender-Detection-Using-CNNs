# Gender Detection Using Convolutional Neural Networks (CNNs)

This repository contains the code for real-time gender detection using a pre-trained Convolutional Neural Network (CNN) model. The model is implemented using Keras with TensorFlow backend and uses OpenCV for face detection.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project demonstrates how to perform real-time gender detection using a pre-trained CNN model. The model classifies faces detected in video frames as either 'Male' or 'Female'.

## Installation
To set up this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/ADMICSOL/gender-detection-cnn.git
cd gender-detection-cnn
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
It's recommended to use a virtual environment to manage dependencies. You can set up a virtual environment as follows:

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

## Running the Application
To run the gender detection application:

1. Ensure you have a webcam connected to your computer.
2. Run the following command:
```bash
python gender_detection.py
```
3. Press 'q' to quit the application.

