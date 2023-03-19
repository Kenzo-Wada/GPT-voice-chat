import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_gpt4_response(prompt):
    prompt = f"日本語で答えてください: {prompt}"
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    
    answer = response.choices[0].text.strip()
    
    # Remove unnecessary parts
    answer = answer.replace("ください", "").replace("。", "").strip()
    
    return answer
