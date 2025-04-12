import os
from google.cloud import translate_v3
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from Models.response_translation_text import Translation, TranslationResponse
from Config.enviroments import project_id #, key_json

client = translate_v3.TranslationServiceClient()
#client = translate_v3.TranslationServiceClient.from_service_account_json(key_json)
parent = f"projects/{project_id}/locations/global"



# Initialize Translation client
def translate_text_to_target_language(text: str, language_code: str,) -> translate_v3.TranslationServiceClient:
    """
        Translating Text from English to a specific languages
    Args:
        text: The content to translate.
        language_code: The language code for the translation.
        E.g. "fr" for French, "es" for Spanish, etc.
        Available languages: https://cloud.google.com/translate/docs/languages#neural_machine_translation_model
    """
    
    try:        
        
        response = client.translate_text(
        contents=[text],
        target_language_code=language_code,
        parent=parent,
        mime_type="text/plain",
        source_language_code="en-US")
        
        
        if response is None:
            raise HTTPException(status.HTTP_409_CONFLICT, 'There was a problem retrieving the translation.')
        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=TranslationResponse(
                translations=[
                    Translation(
                        translated_text=response.translations[0].translated_text,
                        source_language="en-US",
                        target_language=language_code
                    )
                ]
            ).model_dump(),
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST",
                "Access-Control-Allow-Headers": "Content-Type"
            }
        )
        
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, f'There was a problem, error: {e} Please try again.')
