#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
import models
from models.Base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from os import getenv


user = getenv('MYSQL_USER')
passwd = getenv('MYSQL_PASSWD')


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{passwd}'
                                      f'@localhost/WeatherWise', pool_pre_ping=True)

    def reload(self):
        """Create all tables in the database and start a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.close()

    def new(self, obj):
        """Add an object to the database session"""
        self.__session.add(obj)

    def get(self, cls, id):
        """Get an object from the database by its class and id"""
        if cls and id:
            return self.__session.query(cls).get(id)

    def delete(self, obj):
        """Delete an object from the database"""
        if obj:
            self.__session.delete(obj)

    def save(self):
        """Commit all changes to the database"""
        self.__session.commit()

    def user_locations(self, user_id):
        """Get all locations for a user"""
        from models.location import Location
        locations = self.__session.query(Location).filter_by(user_id=user_id).all()
        if locations:
            return ((location.city_name, location.country_code) for location in locations)
