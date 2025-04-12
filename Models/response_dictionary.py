from pydantic import BaseModel
from typing import Optional, List


class License(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None


class Phonetics(BaseModel):
    text: Optional[str] = None
    audio: Optional[str] = None
    sourceUrl: Optional[str] = None
    license: Optional[License] = None


class Definition(BaseModel):
    definition: Optional[str] = None
    synonyms: Optional[List[str]] = None
    antonyms: Optional[List[str]] = None
    example: Optional[str] = None


class Meaning(BaseModel):
    partOfSpeech: Optional[str] = None
    definitions: List[Definition] = []
    synonyms: Optional[List[str]] = None
    antonyms: Optional[List[str]] = None


class ResponseDictionary(BaseModel):
    word: Optional[str] = None
    phonetics: Optional[List[Phonetics]] = None
    meanings: Optional[List[Meaning]] = None
    license: Optional[License] = None
    sourceUrls: Optional[List[str]] = None
