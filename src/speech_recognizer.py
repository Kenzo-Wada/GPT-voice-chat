import pyaudio
import speech_recognition as sr


# 音声認識用のオブジェクトの生成
class SpeechRecognizer:
    def __init__(self, chunk=1024, format=pyaudio.paInt16, channels=1, rate=44100, input_device_index=2):
        self.chunk = chunk
        self.format = format
        self.channels = channels
        self.rate = rate
        self.input_device_index = input_device_index
        
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.format, channels=self.channels, rate=self.rate, input=True, frames_per_buffer=self.chunk, input_device_index=self.input_device_index)
        
        self.r = sr.Recognizer()
        
    def get_audio_input(self):
        # 音声入力の取得
        data = self.stream.read(self.chunk)
        return data
    
    def recognize_google(self, data):
        # 音声入力からテキストへの変換
        text = self.r.recognize_google(data)
        return text
