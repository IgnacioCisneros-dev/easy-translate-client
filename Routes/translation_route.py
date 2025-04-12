from fastapi import APIRouter
from Services.translate_services import translate_text_to_target_language

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