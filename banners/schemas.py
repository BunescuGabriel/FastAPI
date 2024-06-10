from pydantic import BaseModel


class BannerSchema(BaseModel):
    id: int
    name: str
    image_url: str

    class Config:
        orm_mode = True

class BannerUpdateSchema(BaseModel):
    name: str = None
    image_url: str = None
