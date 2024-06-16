#!/usr/bin/env python3
""" Password hashing """

from bcrypt import checkpw, hashpw, gensalt
from db import DB
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import User
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """ Takes in a password string and returns bytes """
    if password and type(password) is str:
        salt = gensalt()
        password = password.encode('utf-8')
        return hashpw(password, salt)


def _generate_uuid() -> str:
    """ Returns a string representation of a new UUID """
    return str(uuid4())


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
                return checkpw(password.encode('utf-8'), user.hashed_password)
            except (InvalidRequestError, NoResultFound):
                return False

    def create_session(self, email: str) -> str:
        """
        Returns the session ID as a string and stores it to
        the database to the User.session_id attribute
        """
        if email and type(email) is str:
            try:
                user = self._db.find_user_by(email=email)
                self._db.update_user(user.id, session_id=_generate_uuid())
                return user.session_id
            except (InvalidRequestError, NoResultFound):
                return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Retrieves a User by their session_id """
        if session_id and type(session_id) is str:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except (NoResultFound, InvalidRequestError):
                pass
        return None

    def destroy_session(self, user_id: int):
        """ Destroys a session attached to a user """
        if user_id and type(user_id) is int:
            try:
                user = self._db.find_user_by(id=user_id)
                self._db.update_user(user.id, session_id=None)
            except (NoResultFound, InvalidRequestError):
                pass
        return None

    def get_reset_password_token(self, email: str) -> str:
        """ Sets the reset_token attribute for a user and returns it """
        if email and type(email) is str:
            try:
                user = self._db.find_user_by(email=email)
                token = _generate_uuid()
                self._db.update_user(user.id, reset_token=token)
                return token
            except (NoResultFound, InvalidRequestError):
                pass
        raise ValueError('Invalid request / User {} doesnt exist'
                         .format(email))

    def update_password(self, reset_token: str, password: str):
        """ Updates a User password if it exists """
        if reset_token and password:
            user = self._db.find_user_by()
