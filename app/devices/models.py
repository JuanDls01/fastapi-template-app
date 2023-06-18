from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from ..settings.db_setup import Base
from ..settings.mixins import Timestamp


class DeviceModel(Timestamp, Base):
    __tablename__ = "device_models"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    technical_name = Column(String, unique=True, index=True)
    no_readeable_attribute = Column(String)

    devices = relationship(
        "Device", back_populates="device_model", uselist=False
    )


class Device(Timestamp, Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    serial_number = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    device_model_id = Column(Integer, ForeignKey("device_models.id"))

    device_model = relationship("DeviceModel", back_populates="devices")

    __table_args__ = (UniqueConstraint("serial_number", "device_model_id"),)
