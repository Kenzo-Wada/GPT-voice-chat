import openai


# OpenAI APIによる回答の生成
class OpenAIAPI:
    def __init__(self, api_key, engine, max_tokens, temperature):
        openai.api_key = api_key
        self.engine = engine
        self.max_tokens = max_tokens
        self.temperature = temperature
        
    def generate_answer(self, text):
        try:
            response = openai.Completion.create(engine=self.engine, prompt=text, max_tokens=self.max_tokens, n=1, stop=None, temperature=self.temperature)
            answer = response.choices[0].text
        except openai.error.APIError as e:
           
