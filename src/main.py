import pyaudio
import speech_recognition as sr
import openai
import pyttsx3
import os

# Text to speechエンジンの初期化
engine = pyttsx3.init()

# 環境変数からAPIキーを取得
openai.api_key = os.environ.get('OPENAI_API_KEY')

# 音声入力用の設定
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# 音声入力用のオブジェクトの生成
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, input_device_index=2)

# 音声入力からテキストへの変換用のオブジェクトの生成
r = sr.Recognizer()

while True:
    # 音声入力の取得
    data = stream.read(CHUNK)
    
    # 音声入力からテキストへの変換
    try:
        text = r.recognize_google(data)
        print("Input:", text)
    except sr.UnknownValueError:
        text = ""
    except sr.RequestError:
        text = ""
    
    # GPT-4による回答の生成
    try:
        response = openai.Completion.create(engine="text-davinci-002", prompt=text, max_tokens=1024, n=1, stop=None, temperature=0.5)
        answer = response.choices[0].text
        print("Response:", answer)
    except openai.error.APIError as e:
        print("Error: ", e)
        answer = "Sorry, I could not generate a response."
    
    # 回答の読み上げ
    try:
        engine.say(answer)
        engine.runAndWait()
    except pyttsx3.exceptions.EngineError as e:
        print("Error: ", e)
