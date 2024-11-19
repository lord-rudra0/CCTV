from flask import Flask, request, jsonify , render_template , redirect , url_for , flash, Response
import cv2 

app = Flask(__name__)

camera = cv2.VideoCapture(0)
import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not found!")
else:
    print("Camera found!")


def cctv_feed():
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

@app.route('/https://cctv-integration-system.onrender.com/video')
def video():
    return Response(cctv_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)