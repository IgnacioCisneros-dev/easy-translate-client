from fastapi import APIRouter
from Services.translate_services import (
    translate_text_to_target_language,
    get_details_translation
) 

router = APIRouter(
    prefix="/api",
    tags=["Translation"]
)

@router.post(
    "/translate",
    summary="Translate text endpoint",
    description="Translates text from English to the specified target language",
    response_description="Translation result",
    responses={
        200: {
            "description": "Successful translation",
            "content": {
                "application/json": {
                    "example": {
                        "translated_text": "Bonjour le monde",
                        "source_language": "en-US",
                        "target_language": "fr"
                    }
                }
            }
        },
        400: {
            "description": "Bad request",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid request parameters"}
                }
            }
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/json": {
                    "example": {"detail": "Translation failed: error message"}
                }
            }
        }
    }
)
async def translate_text(text: str, target_language: str):
    try:
        response = translate_text_to_target_language(text=text, language_code=target_language)
        return response       
    except Exception as e:
        raise
    


@router.get("/translate/details",
            summary='Endpoint for retreive details about the word in the input',
            description="Translates text from English to the specified target language with details and more examples.",
            response_description="Translation result",
            responses={
            200: {
                "description": "Successful translation",
                "content": {
                    "application/json": {
                        "example": {
                            "translated_text": "Bonjour le monde",
                            "source_language": "en-US",
                            "target_language": "fr"
                        }
                    }
                }
            },
            400: {
                "description": "Bad request",
                "content": {
                    "application/json": {
                        "example": {"detail": "Invalid request parameters"}
                    }
                }
            },
            500: {
                "description": "Internal server error",
                "content": {
                    "application/json": {
                        "example": {"detail": "Translation failed: error message"}
                    }
                }
            }
        }
)
async def get_dictonary_details(word: str):
    try:        
        response = get_details_translation(word)
        return response        
    except Exception as e:
        print(e)
        raise
    
    
    