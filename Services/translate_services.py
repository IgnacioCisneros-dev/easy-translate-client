# Imports the Google Cloud Translation library
import os
from google.cloud import translate_v3
from Config.enviroments import key_json,project_id

client = translate_v3.TranslationServiceClient()



# Initialize Translation client
def translate_text_to_target_language(
    text: str = "YOUR_TEXT_TO_TRANSLATE",
    language_code: str = "en",
) -> translate_v3.TranslationServiceClient:
    """Translating Text from English.
    Args:
        text: The content to translate.
        language_code: The language code for the translation.
            E.g. "fr" for French, "es" for Spanish, etc.
            Available languages: https://cloud.google.com/translate/docs/languages#neural_machine_translation_model
    """

    
    parent = f"projects/{project_id}/locations/global"
    # Translate text from English to chosen language
    # Supported mime types: # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        contents=[text],
        target_language_code=language_code,
        parent=parent,
        mime_type="text/plain",
        source_language_code="en-US",
    )

    # Display the translation for each input text provided
    for translation in response.translations:
        print(f"Translated text: {translation.translated_text}")
    # Example response:
    # Translated text: Bonjour comment vas-tu aujourd'hui?

    return response
