from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.schemas import TextRequest
from app.tts_engine import generate_speech

app = FastAPI(title="Open Source TTS API")

@app.get("/")
def home():
    return {"message": "TTS API Running"}

@app.post("/tts")
def text_to_speech(request: TextRequest):
    filepath = generate_speech(request.text)
    return FileResponse(filepath, media_type="audio/wav", filename="speech.wav")
