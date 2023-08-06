from fastapi import APIRouter

from . import gitlab

api_router = APIRouter()
api_router.include_router(gitlab.router, prefix="/gitlab", tags=["gitlab"])
