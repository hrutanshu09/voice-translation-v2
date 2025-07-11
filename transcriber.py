# transcriber.py

import whisper
from crypto_utils import encrypt_4digit_numbers
import tempfile

# Load model once at the top
model = whisper.load_model("base")

def transcribe_audio_bytes(audio_bytes: bytes) -> dict:
    # Save audio to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    # Transcribe the audio using Whisper
    result = model.transcribe(
        temp_audio_path,
        task="transcribe",
        language="hi"
    )

    raw_text = result.get("text", "").strip()
    sanitized_text = encrypt_4digit_numbers(raw_text)
    
    return {
        "transcript": raw_text,
        "sanitized": sanitized_text
    }
