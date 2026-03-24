from TTS.api import TTS
import uuid
import os

MODEL_NAME = "tts_models/en/ljspeech/tacotron2-DDC"
OUTPUT_DIR = "output"

tts = None

def load_model():
    global tts
    if tts is None:
        tts = TTS(model_name=MODEL_NAME, progress_bar=False, gpu=False)

def generate_speech(text: str):
    load_model()

    filename = f"{uuid.uuid4()}.wav"
    filepath = os.path.join(OUTPUT_DIR, filename)

    tts.tts_to_file(text=text, file_path=filepath)

    return filepath
