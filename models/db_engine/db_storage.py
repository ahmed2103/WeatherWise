#!/usr/bin/python3
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
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = session_factory()
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()

    def new(self, obj):
        self.__session.add(obj)

    def get(self, cls, id):
        if cls and id:
            return self.__session.query(cls).get(id)

    def delete(self, obj):
        if obj:
            self.__session.delete(obj)

    def save(self):
        self.__session.commit()


    def user_locations(self, user_id):
        """Get all locations for a user"""
        from models.location import Location
        locations = self.__session.query(Location).filter_by(user_id=user_id).all()
        if locations:
            return (location.city_name for location in locations)