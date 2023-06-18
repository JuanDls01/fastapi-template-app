from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..settings.db_setup import async_get_db
from .crud import get_device_models, create_device_model
from .schemas import DeviceModel, DeviceModelCreate

router = APIRouter()


@router.get("/models", response_model=List[DeviceModel])
async def read_device_models(db: Session = Depends(async_get_db)):
    device_models = await get_device_models(db=db)
    return device_models


@router.post("/models", response_model=str)
async def crete_device_model(
    device_model: DeviceModelCreate, db: Session = Depends(async_get_db)
):
    device_model_created = await create_device_model(
        db=db, device_model=device_model
    )
    return device_model_created.id
