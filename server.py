"""
This file is the Flask server running the web application.
"""
import json
from flask import Flask, render_template, request
import EmotionDetection

app = Flask(__name__)

@app.route('/')
def home():
    """
    This method implements the default route the application.
    """
    return render_template("index.html")

@app.route('/emotionDetector')
def emotion_detector():
    """
    This method implements the route the application that is used to call the emotion detector.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = json.loads(EmotionDetection.emotion_detection.emotion_detector(text_to_analyze))
    if result["dominant_emotion"] is None:
        return "<b>Invalid text! Please try again!.</b>"

    return f'''For the given statement, the system response is 'anger': {result['anger']} ,
    'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} 
    and 'sadness': {result['sadness']}. The dominant emotion is <b>{result['dominant_emotion']}</b>.'''