from fastapi import FastAPI
from pydantic import BaseModel

# deine Logik aus dem Notebook
def translate_emojis(text: str) -> str:
    mapping = {
        "😊": "smile",
        "😂": "laugh",
        "❤️": "heart",
        "🔥": "fire",
        "👍": "thumbs up",
        "😢": "cry",
        "😎": "cool",
        "💡": "idea",
    }
    for emoji, word in mapping.items():
        text = text.replace(emoji, word)
    return text

# FastAPI-App
app = FastAPI(title="Emoji Translator API")

# Request- und Response-Struktur
class TextIn(BaseModel):
    text: str

class TextOut(BaseModel):
    translated: str

# Endpoint definieren
@app.post("/translate", response_model=TextOut)
def translate(incoming: TextIn):
    return TextOut(translated=translate_emojis(incoming.text))
