from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion_detector():
    # Retireve the text to analyze from request arguments
    text_to_analyze = request.args.get('phrase')

    # if (text_to_analyze is None):
    #     return ("Not phrase found", 400)
    
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
    else:
        return "For the given statement, the system response is 'anger': {}, "\
            "'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. "\
            "The dominant emotion is {}.".format(anger, disgust, fear, joy, sadness, dominant_emotion )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)