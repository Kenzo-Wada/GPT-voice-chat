import os
from gtts import gTTS
from playsound import playsound

def text_to_speech(text, language="ja"):
    tts = gTTS(text, lang=language)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")
