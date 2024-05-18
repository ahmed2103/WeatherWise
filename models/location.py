#!/usr/bin/python3
"""locatiom model for the ORM"""

import models
from models.Base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, ForeignKey


class Location(BaseModel, Base):
    __tablename__ = 'locations'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    city_name = Column(String(60), nullable=False)
    country_code = Column(String(5), nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
