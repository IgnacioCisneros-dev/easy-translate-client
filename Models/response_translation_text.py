from pydantic import BaseModel
from typing import List

class Translation(BaseModel):
    translated_text: str
    source_language: str
    target_language: str

class TranslationResponse(BaseModel):
    translations: List[Translation]
