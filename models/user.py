#!/usr/bin/python3
"""user model for the ORM"""
import models
from models.Base_model import BaseModel, Base
from sqlalchemy import Column, String, backref
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User model for the ORM"""
    __tablename__ = 'users'

    prefered_units = Column(String(2), default='C')
    locations = relationship('Location',
                             backref=backref('user', cascade='all, delete'),
                             cascade='all, delete, delete-orphan')


    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        self.prefered_units = kwargs.get('prefered_units', 'C')
