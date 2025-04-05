from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Config.enviroments import CONFIG_APP
from Routes.test_router import router as test_router
from Routes.translation_route import router as translation_router

# Initialize FastAPI app with configuration
app = FastAPI(
    title=CONFIG_APP['title'],
    description=CONFIG_APP['description'],
    version=CONFIG_APP['version'],
    contact=CONFIG_APP['contact'],
    openapi_tags=CONFIG_APP['openapi_tags'],
    docs_url=CONFIG_APP['docs_url'],
    redoc_url=CONFIG_APP['redoc_url'],
    openapi_url=CONFIG_APP['openapi_url'],
    debug=CONFIG_APP['debug']
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CONFIG_APP['middleware']['cors']['allow_origins'],
    allow_credentials=CONFIG_APP['middleware']['cors']['allow_credentials'],
    allow_methods=CONFIG_APP['middleware']['cors']['allow_methods'],
    allow_headers=CONFIG_APP['middleware']['cors']['allow_headers']
)

# Include routers
app.include_router(test_router)
app.include_router(translation_router)
