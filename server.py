""" Runs Flask server. """

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion_detector():
    """ Retireve the text to analyze from request arguments """
    text_to_analyze = request.args.get('phrase')

    # Pass the text to the emotion_detector funciton and store the response
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return ("Invalid text! Please try again!.", 400)
    return f"For the given statement, the system response is 'anger': {anger}, "\
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "\
            f"The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """ Renders index page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
