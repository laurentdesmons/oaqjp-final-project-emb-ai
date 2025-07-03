from flask import Flask, render_template, request
import EmotionDetection
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/emotionDetector')
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    result = json.loads(EmotionDetection.emotion_detection.emotion_detector(text_to_analyze))
    return f'''For the given statement, the system response is 'anger': {result['anger']} , 
    'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} 
    and 'sadness': {result['sadness']}. The dominant emotion is <b>{result['dominant_emotion']}</b>.'''