#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """This class manages storage of hbnb models in the database"""
    __engine = None
    __session = None

    def __init__(self):
        """Public instance methods to create the engine using env variable"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}{}/{}'.format(user, password, host, database), pool_pre_ping=True)

        if(getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session all objects depending of the class name (argument cls)"""
        if cls is None:
            cls_dict = self.__session.query(State).all()
            cls_dict.extend(self.__session.query(City).all())
            cls_dict.extend(self.__session.query(User).all())
            cls_dict.extend(self.__session.query(Place).all())
            cls_dict.extend(self.__session.query(Review).all())
            cls_dict.extend(self.__session.query(Amenity).all())
        else:
            cls_dict = {}
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                cls_dict[key] = obj
            return cls_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session obj if not none"""
        if(obj):
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Creates all tables in the database and initializes the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the working SQLAlchemy session."""
        self.__session.close()
    