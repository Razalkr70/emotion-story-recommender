# 🎭 Emotion-Based Story Recommender

A Flask-based web application that captures real-time video from your webcam, detects facial emotion using computer vision, and displays a short story based on the detected emotion. This tool aims to provide personalized content through emotion recognition.

---

## 📸 Overview

This project combines **Flask**, **OpenCV**, and **emotion detection** techniques to analyze the user's facial expressions and recommend a story matching their current emotional state. It's an innovative way to integrate AI with real-time video input for a personalized user experience.

---

## 🧠 Features

- Real-time webcam video feed using OpenCV
- Emotion detection using a custom model
- Story recommendation based on the detected emotion
- Simple and interactive web interface using Flask
- JSON response containing emotion and story

---

## 🛠️ Tech Stack

- **Python** – Core language  
- **Flask** – Web framework  
- **OpenCV** – Real-time video capture and image handling  
- **Custom Emotion Detection Model** – Integrated via `detect_emotion()`  
- **Utility Functions** – Story mapping via `get_story_by_emotion()`  
- **HTML/CSS (Jinja2)** – Frontend templates  

---

## 🗂️ Folder Structure
``
project-root/
├── app.py # Main Flask application
├── camera.py # Contains detect_emotion() function
├── utils.py # Maps emotion to story
├── templates/
│ └── index.html # Frontend UI
├── static/ # (Optional) Static assets (CSS, JS, etc.)
└── requirements.txt # Python dependencies
``


---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Razalkr70/emotion-story-recommender.git
cd emotion-story-recommender
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3.Run the App
```
python app.py
```

