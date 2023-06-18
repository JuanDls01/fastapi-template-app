from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import DeviceModel
from .schemas import DeviceModelCreate


async def get_device_model(db: AsyncSession, device_model_id: int):
    query = select(DeviceModel).where(DeviceModel.id == device_model_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_device_models(db: AsyncSession):
    query = select(DeviceModel)
    result = await db.execute(query)
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
