from audio_recognition import get_audio_input, transcribe_audio
from gpt4 import generate_gpt4_response
from tts import text_to_speech

def main():
    while True:
        audio_data = get_audio_input()
        text = transcribe_audio(audio_data)

        if text is not None:
            print(f"Input: {text}")

            if text == "終了":
                print("プログラムを終了します。")
                break

            response = generate_gpt4_response(text)
            print(f"Output: {response}")
            text_to_speech(response)
        else:
            print("Error: ")

if __name__ == "__main__":
    main()
