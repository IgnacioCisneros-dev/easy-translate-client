import os
from dotenv import dotenv_values

config_env = {
     **dotenv_values(".env"),  
    **os.environ, 
}


try:
    CONFIG_APP = {
        'title': "API Translation Client",
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
    
    GOOGLE_APPLICATION_CREDENTIALS = config_env['GOOGLE_APPLICATION_CREDENTIALS']
    
except Exception as ex:
    raise Exception(f"Error loading configuration: {str(ex)}")