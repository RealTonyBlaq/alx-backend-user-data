#!/usr/bin/env python3
""" SessionAuth Model """

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Defining the class SessionAuth that authenticates a session """
    user_id_by_session_id = {}

    def __init__(self) -> None:
        """ Initializes the inherited attributes """
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id

        Return: None if user_id is None
        Return None if user_id is not a string
        """
        
