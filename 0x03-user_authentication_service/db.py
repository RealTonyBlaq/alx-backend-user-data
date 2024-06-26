#!/usr/bin/env python3
""" DB Module """

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Saves a new User to the database """
        new_user = User()
        new_user.email = email
        new_user.hashed_password = hashed_password
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Finds and returns a user object from the database """
        if kwargs:
            for key in kwargs.keys():
                if key not in ['email', 'id', 'session_id', 'reset_token']:
                    raise InvalidRequestError('Invalid key in kwargs')
            user = self._session.query(User).filter_by(**kwargs).first()
            if user:
                return user
            raise NoResultFound('No result found with the parameters')
        raise InvalidRequestError('Invalid parameter type. Use keyword args')

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Updates a user object in the database """
        if user_id and kwargs and type(user_id) is int:
            try:
                user = self.find_user_by(id=user_id)
            except NoResultFound:
                return None

            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError(f'User has no attribute named {key}')
            self._session.add(user)
            self._session.commit()

        return None
