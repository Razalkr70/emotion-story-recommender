import cv2
import numpy as np
from keras.models import load_model

# Load pre-trained emotion model
model = load_model("emotion_model/emotion_model.h5")

# Emotion labels
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

def detect_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi_gray, (48, 48)) / 255.0
        roi = roi.reshape(1, 48, 48, 1)
        prediction = model.predict(roi, verbose=0)
        emotion = emotion_labels[np.argmax(prediction)]
        return emotion

    # If no face is detected
    return "neutral"
