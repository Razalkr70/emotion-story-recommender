from flask import Flask, render_template, Response, jsonify
import cv2
from camera import detect_emotion
from utils import get_story_by_emotion

app = Flask(__name__)
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_emotion_story')
def get_emotion_story():
    try:
        success, frame = camera.read()
        if not success or frame is None:
            return jsonify({"emotion": "None", "story": "Failed to capture image from camera."})

        emotion = detect_emotion(frame)
        story = get_story_by_emotion(emotion)

        return jsonify({"emotion": emotion, "story": story})

    except Exception as e:
        return jsonify({"emotion": "Error", "story": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
