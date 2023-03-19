from audio_recognition import get_audio_input, transcribe_audio
from gpt4 import generate_gpt4_response
from tts import text_to_speech

def main():
    audio_data = get_audio_input()
    transcribed_text = transcribe_audio(audio_data)

    if transcribed_text:
        print(f"Input: {transcribed_text}")
        gpt4_response = generate_gpt4_response(transcribed_text)
        print(f"Output: {gpt4_response}")
        text_to_speech(gpt4_response)

if __name__ == "__main__":
    main()
