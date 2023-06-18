from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..settings.db_setup import async_get_db

router = APIRouter()


@router.get("/")
async def get_devices(db: Session = Depends(async_get_db)):
    devices = db.query(devices.Device).all()
    return devices
