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
git clone https://github.com/your-username/gender-detection-cnn.git
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

## Model Training
If you want to train your own model:

1. Prepare your dataset in the required format.
2. Modify the `train_model.py` script to fit your needs.
3. Run the training script:
```bash
python train_model.py
```

## Contributing
Contributions to this project are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
