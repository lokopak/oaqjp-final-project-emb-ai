import json

import requests


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    obj = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, json = obj, headers = headers)

        if response.status_code == 200:
            emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
        
            emotions["dominant_emotion"] = max(emotions, key=emotions.get)

            return emotions
        else:
            return ({
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            })

    except Exception as err:
        return ("Unexpected error {}".format(err), 500)