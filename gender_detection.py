import cv2
import numpy as np
from keras.models import load_model

# Load the trained gender model
gender_model = load_model("gender_model0286.h5")

# Define the categories of gender
gender_labels = ['Male', 'Female']

# Load the face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face ROI
        face_roi = frame[y:y + h, x:x + w]

        # Preprocess the face ROI for gender prediction
        face_array_gender = cv2.resize(face_roi, (224, 224))
        face_array_gender = np.expand_dims(face_array_gender, axis=0) / 255.0

        # Predict gender
        gender_preds = gender_model.predict(face_array_gender)
        predicted_gender = gender_labels[int(round(gender_preds[0][0]))]

        # Display the gender prediction
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, f"Gender: {predicted_gender}",
                    (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('Gender Detection', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
