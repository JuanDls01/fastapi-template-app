from typing import List

from databases import Database

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..settings.db_setup import async_get_db, get_db_async_connection
from .crud import (
    get_device_model,
    get_device_models,
    create_device_model,
    create_device,
)
from .schemas import DeviceModel, DeviceModelCreate, DeviceCreate

router = APIRouter()

from .models import DeviceModel, Device


@router.get("/models")
async def read_device_models(db: Database = Depends(get_db_async_connection)):
    query = DeviceModel.__table__.select()
    result = await db.fetch_all(query)
    # device_models = await get_device_models(db=db)
    return result


@router.get("/models/{device_model_id}")
async def read_device_model(
    device_model_id: int, db: Database = Depends(get_db_async_connection)
):
    query = DeviceModel.__table__.select().where(
        DeviceModel.id == device_model_id
    )
    result = await db.fetch_all(query)
    return result[0]


@router.post("/models", response_model=str)
async def create_device_models(
    device_model: DeviceModelCreate, db: Session = Depends(async_get_db)
):
    device_model_created = await create_device_model(
        db=db, device_model=device_model
    )
    return device_model_created.id


@router.get("")
async def read_devices(db: Database = Depends(get_db_async_connection)):
    query = Device.__table__.select()
    result = await db.fetch_all(query)
    # device_models = await get_device_models(db=db)
    return result


@router.post("")
async def create_devices(
    device: DeviceCreate, db: Database = Depends(get_db_async_connection)
):
    device_created = await create_device(db=db, device=device)
    print("device_created", device_created)
    return device_created
