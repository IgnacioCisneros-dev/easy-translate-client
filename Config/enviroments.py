import os
from dotenv import dotenv_values

config_env = {
     **dotenv_values(".env"),  
    **os.environ, 
}


try:
    CONFIG_APP = {
        'title': "Translation Client API",
        'description': 'API Client that provides seamless integration with Google Cloud Translation services, enabling fast and accurate text translation across multiple languages',
        'version': "1.0.0",
        'contact': {
            'name': "",
            'email': "icisneros1012@gmail.com",
            'url': "https://pending.com"
        },
        'openapi_tags': [
            {
                'name': "Health",
                'description': "Health check endpoints"
            }
        ],
        'docs_url': "/docs",
        'redoc_url': "/redoc",
        'openapi_url': "/openapi.json",
        'debug': False,
        'middleware': {
            'cors': {
                'allow_origins': ["*"],
                'allow_credentials': True,
                'allow_methods': ["*"],
                'allow_headers': ["*"]
            },
            'trusted_hosts': {
                'allowed_hosts': ["*"]
            }
        },
        'default_response_class': {
            'media_type': "application/json"
        }
    }
    
    #key_json = config_env['KEY_JSON']
    project_id = config_env['PROJECT_ID']
    url_dictionary = config_env['URL_DICTIONARY_API']
    
except Exception as ex:
    raise Exception(f"Error loading configuration: {str(ex)}")