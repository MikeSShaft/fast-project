from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Enum,
    ForeignKey,
    Table,
    MetaData,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Создаем объект MetaData
metadata = MetaData()

# Базовый класс для моделей
Base = declarative_base(metadata=metadata)

class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    priority = Column(Integer, default=0)
    description = Column(String)
    description_en = Column(String)
    trademark = Column(String(255))
    is_active = Column(Boolean, default=True)
    is_ban = Column(Boolean, default=False)
    has_contact = Column(Boolean, default=False)
    invisible_ws = Column(Boolean, default=False)
    trademark_is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Отношения многие-ко-многим
    countries = relationship("Country", secondary="brand_countries", back_populates="brands")
    crosses = relationship("Cross", back_populates="brand")

class Cross(Base):
    __tablename__ = 'crosses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    is_copy = Column(Boolean, default=False)
    type = Column(Enum('Локальный', 'TekDok', name='cross_type'), default='Локальный')
    brand_id = Column(Integer, ForeignKey('brands.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Отношения
    brand = relationship("Brand", back_populates="crosses")
    countries = relationship("Country", secondary="cross_countries", back_populates="crosses")

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Отношения многие-ко-многим
    brands = relationship("Brand", secondary="brand_countries", back_populates="countries")
    crosses = relationship("Cross", secondary="cross_countries", back_populates="countries")

# Таблицы для отношений многие-ко-многим
brand_countries = Table(
    'brand_countries',
    Base.metadata,
    Column('brand_id', Integer, ForeignKey('brands.id')),
    Column('country_id', Integer, ForeignKey('countries.id'))
)

cross_countries = Table(
    'cross_countries',
    Base.metadata,
    Column('cross_id', Integer, ForeignKey('crosses.id')),
    Column('country_id', Integer, ForeignKey('countries.id'))
)