#!/usr/bin/env python3
""" SessionAuth Model """

from api.v1.auth.auth import Auth
from models.user import User
import uuid
from typing import TypeVar


class SessionAuth(Auth):
    """ Defining the class SessionAuth that authenticates a session """
    user_id_by_session_id = {}

    def __init__(self) -> None:
        """ Initializes the inherited attributes """
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id

        Return:
            - None if user_id is None
            - None if user_id is not a string
        """
        if user_id and type(user_id) is str:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Retrieves the user that matches a session id """
        if session_id and type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves a current user based on the cookie value """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Deletes the user session / logout:

        If the request is equal to None, return False
        If the request doesnt contain the Session ID cookie, return False - you must use self.session_cookie(request)
        If the Session ID of the request is not linked to any User ID, return False - you must use self.user_id_for_session_id(...)
        Otherwise, delete in self.user_id_by_session_id the Session ID (as key of this dictionary) and return True
        """
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                
