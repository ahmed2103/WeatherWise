import models
from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, func
from datetime import datetime


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(String(60), primary_key=True, default=lambda: str(uuid4()))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __init__(self, *args, **kwargs):
        """Base model constructor"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts the model to a dictionary"""
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        """formal representation of the model"""
        return f"<{self.__class__.__name__} {self.to_dict()}>"

    def __str__(self):
        """ingormal representation of the model"""
        return f"{self.to_dict()}"

    def save(self):
        """Saves the model to the database"""
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Deletes the model from the database"""
        models.storage.delete(self)
        models.storage.save()