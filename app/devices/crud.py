from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession

# from sqlalchemy.future import select

from .models import DeviceModel, Device
from .schemas import DeviceModelCreate, DeviceCreate


async def get_device_model(db: AsyncSession, device_model_id: int):
    query = DeviceModel.__table__.select(DeviceModel.id == device_model_id)
    # select(DeviceModel).where(DeviceModel.id == device_model_id)
    # result = await db.execute(query)4
    result = await db.fetch_all(query)
    # result.scalar_one_or_none()
    return result.scalars()


async def get_device_models(db: AsyncSession):
    # query = select(DeviceModel)
    query = DeviceModel.__table__.select()
    result = await db.fetch_all(query)
    return result.scalars().all()


async def create_device_model(
    db: AsyncSession, device_model: DeviceModelCreate
):
    db_device_model = DeviceModel(
        technical_name=device_model.technical_name,
        no_readeable_attribute=device_model.no_readeable_attribute,
    )
    db.add(db_device_model)
    await db.commit()
    db.refresh(db_device_model)
    return db_device_model


from databases import Database


async def create_device(db: Database, device: DeviceCreate):
    # db_device = Device(
    #     serial_number=device.serial_number,
    #     device_model_id=device.device_model_id,
    # )
    async with db.transaction():
        query = Device.__table__.insert()

        values = {
            "serial_number": device.serial_number,
            "device_model_id": device.device_model_id,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        }
        result = await db.execute(query=query, values=values)
    # serial_number = Column(String, unique=True, index=True)
    # is_active = Column(Boolean, default=True)
    # device_model_id = Column(Integer, ForeignKey("device_models.id"))
    print("device", result)
    return result
