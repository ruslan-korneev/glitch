from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.config.const import API_V1_STR, BACKEND_CORS_ORIGINS, PROJECT_NAME

from .routers import api_router

application = FastAPI(title=PROJECT_NAME, openapi_url=f"{API_V1_STR}openapi.json")

# Set all CORS enabled origins
if BACKEND_CORS_ORIGINS:
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

application.include_router(api_router, prefix=API_V1_STR)
