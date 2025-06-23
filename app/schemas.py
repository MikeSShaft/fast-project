from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class BrandBase(BaseModel):
    name: str
    slug: str
    priority: Optional[int] = 0
    description: Optional[str] = None
    description_en: Optional[str] = None
    trademark: Optional[str] = None
    is_active: Optional[bool] = True
    is_ban: Optional[bool] = False
    has_contact: Optional[bool] = False
    invisible_ws: Optional[bool] = False
    trademark_is_active: Optional[bool] = False

class BrandCreate(BrandBase):
    country_ids: List[int]

class BrandUpdate(BrandBase):
    pass

class Brand(BrandBase):
    id: int
    created_at: datetime
    updated_at: datetime
    countries: List[str]
    local_crosses: List[dict]
    tek_dok_crosses: List[dict]

    class Config:
        orm_mode = True

class CrossBase(BaseModel):
    name: str
    slug: str
    is_copy: Optional[bool] = False
    type: Optional[str] = "Локальный"

class CrossCreate(CrossBase):
    brand_id: int
    country_ids: List[int]

class CrossUpdate(CrossBase):
    pass

class Cross(CrossBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CountryBase(BaseModel):
    name: str

class CountryCreate(CountryBase):
    pass

class Country(CountryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True