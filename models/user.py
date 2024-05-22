#!/usr/bin/python3
"""user model for the ORM"""
import models
from models.Base_model import BaseModel
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship, backref
from datetime import datetime

class User(BaseModel):
    """User model for the ORM"""
    __tablename__ = 'users'

    prefered_units = Column(String(2), default='C')
    last_active = Column(DateTime, default=lambda:datetime.now(),
                         onupdate=lambda:datetime.now())
    locations = relationship('Location',
                             backref=backref('user', cascade='all, delete'),
                             cascade='all, delete, delete-orphan')

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        self.prefered_units = kwargs.get('prefered_units', 'C')