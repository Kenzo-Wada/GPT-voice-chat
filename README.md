# GPT-voice-chat

## How-to

### .env

- create `.env`file and add your openAI API key

```
OPENAI_API_KEY=your-api-key
```

### Docker

- `docker compose up --build`
- plz be shure that you have mounted your audio device correctly to docker container

### local(mac)

- `brew install portaudio libsndfile`
- `pip install -r requirements.txt`
- `python src/main.py`
