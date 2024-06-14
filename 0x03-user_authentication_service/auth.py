#!/usr/bin/env python3
""" Password hashing """

from bcrypt import hashpw, gensalt
from db import DB
from sqlalchemy.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """ Takes in a password string and returns bytes """
    if password and type(password) is str:
        salt = gensalt()
        password = password.encode('utf-8')
        return hashpw(password, salt)


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initializes the _db attribute """
        self._db = DB()

    def register_user(self, email: str, pwd: str) -> User:
        """ Registers a user if the email doesn't exist in the db """
        if all([email, pwd, type(email) is str, type(pwd) is str]):
            try:
                user = self._db.find_user_by(email=email)
                raise ValueError
            except NoResultFound:
                
