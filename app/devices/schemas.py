from pydantic import BaseModel


class DeviceBase(BaseModel):
    serial_number: str


class DeviceCreate(DeviceBase):
    pass


class Device(DeviceBase):
    """
    Models that will be used when reading data, when returning it from the API
    """

    id: int
    device_model_id: int
    is_active: bool

    class Config:
        orm_mode = True


class DeviceModelBase(BaseModel):
    technical_name: str


class DeviceModelCreate(DeviceModelBase):
    no_readeable_attribute: str


class DeviceModel(DeviceModelBase):
    """
    Models that will be used when reading data, when returning it from the API
    """

    id: int
    is_active: bool
    devices: list[Device] = []

    class Config:
        """
        Will tell the Pydantic model to read the data even if it is not a dict,
        but an ORM model
        """

        orm_mode = True
