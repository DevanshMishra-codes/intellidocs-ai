from fastapi import APIRouter

from app.api.v1.endpoints import auth, users

from app.api.v1.endpoints import documents

from app.api.v1.endpoints import chat

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(documents.router)
api_router.include_router(chat.router)