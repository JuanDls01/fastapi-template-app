from fastapi import APIRouter
from .devices.endpoints import router as devices_router

api_router = APIRouter()

api_router.include_router(devices_router, prefix="/devices", tags=["devices"])
