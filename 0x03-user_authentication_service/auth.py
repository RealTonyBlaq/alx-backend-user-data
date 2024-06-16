#!/usr/bin/env python3
""" Password hashing """

from bcrypt import checkpw, hashpw, gensalt
from db import DB
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """ Takes in a password string and returns bytes """
    if password and type(password) is str:
        salt = gensalt()
        password = password.encode('utf-8')
        return hashpw(password, salt)


class Auth:
    """
    Auth class to interact with the authentication database
    """

    def __init__(self):
        """ Initializes the _db attribute """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user if the email doesn't exist in the db. """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            password = _hash_password(password)
            return self._db.add_user(email, password)
        except InvalidRequestError:
            raise ValueError('Invalid request type')

    def valid_login(self, email: str, password: str) -> bool:
        """ Validates the login password of the user """
        if email and password:
            try:
                user = self._db.find_user_by(email=email)
