import os
import requests
import json
from google.cloud import translate_v3
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from Models.response_translation_text import Translation, TranslationResponse
from Config.enviroments import project_id, url_dictionary #, key_json
from Models.response_dictionary import ResponseDictionary

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

def get_details_translation(word: str) -> ResponseDictionary:
    """
    Fetches detailed dictionary information for a given word using an external API.

    This function makes a GET request to the dictionary API, decodes the JSON response, 
    and maps it into a `ResponseDictionary` Pydantic model.

    Args:
        word (str): The word to fetch translation and definition details for.

    Returns:
        ResponseDictionary: A structured model containing definitions, phonetics, 
                            synonyms, antonyms, and other metadata for the word.

    Raises:
        HTTPException: If the external API returns an HTTP error.
        Exception: For any other unexpected errors during the request or parsing process.
    """
    try:
        url = f'{url_dictionary}{word}'                
        response = requests.get(url)
        response.raise_for_status()
        
        json_data = json.loads(response.content.decode("utf-8"))
        response_data = json_data[0]
        
        response_dictionary = ResponseDictionary(**response_data)        
        return response_dictionary
        
    except HTTPException as ex:
        raise
    
    except requests.exceptions.HTTPError as ex:
        raise HTTPException(status_code=ex.response.status_code, detail=ex.response.reason)
        
    except Exception as e:
        raise