#!/usr/bin/env python3
""" SessionAuth Model """

from api.v1.auth.auth import Auth
import uuid


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
        """ Retrieves the user that """
