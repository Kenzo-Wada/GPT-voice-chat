import speech_recognition as sr

def get_audio_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio_data = recognizer.listen(source)
    return audio_data

def transcribe_audio(audio_data, language="ja-JP"):
    recognizer = sr.Recognizer()
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data, language=language)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        text = None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        text = None
    return text
