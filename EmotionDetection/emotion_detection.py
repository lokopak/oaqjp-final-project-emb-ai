import json

import requests


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = obj, headers = headers)
    emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
    
    emotions["dominant_emotion"] = max(emotions, key=emotions.get)

    return emotions