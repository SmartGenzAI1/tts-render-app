# Open Source TTS API

Text to Speech API using Coqui TTS and FastAPI.
Deployable on Render Free Tier.

## API Endpoint
POST /tts

Body:
{
  "text": "Hello world"
}

Returns WAV audio file.
