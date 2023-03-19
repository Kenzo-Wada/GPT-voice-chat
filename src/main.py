import os
from speech_recognizer import SpeechRecognizer
from openai_api import OpenAIAPI
from text_to_speech import TextToSpeech


# 環境変数からAPIキーを取得
openai_api_key = os.environ.get('OPENAI_API_KEY')

# 音声認識の設定
recognizer = SpeechRecognizer()

# OpenAI APIの設定
openai_api = OpenAIAPI(api_key=openai_api_key, engine="text-davinci-002", max_tokens=1024, temperature=0.5)

# Text-to-Speechの設定
tts = TextToSpeech()

# 音声入力から回答までの処理
def process_input():
    # 音声入力の取得
    data = recognizer.get_audio_input()
    
    # 音声入力からテキストへの変換
    text = recognizer.recognize_google(data)
    print("Input:", text)
    
    # OpenAI APIによる回答の生成
    answer = openai_api.generate_answer(text)
    print("Response:", answer)
    
    # 回答の読み上げ
    tts.speak(answer)


# メイン関数
if __name__ == '__main__':
    while True:
        process_input()
