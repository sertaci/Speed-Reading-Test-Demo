import os
import azure.cognitiveservices.speech as speechsdk


def from_mic():
    speech_config = speechsdk.SpeechConfig(subscription="API_KEY_HERE", region="eastus")
    speech_config.speech_recognition_language="tr-TR"

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    
    result = speech_recognizer.recognize_once_async().get()

    return result
