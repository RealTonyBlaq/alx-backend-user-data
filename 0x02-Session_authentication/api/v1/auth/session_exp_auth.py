#!/usr/bin/env python3
""" SesionExpAuth Module """

from os import getenv
from session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """ Defining the SessionExpAuth model """

    def __init__(self) -> None:
        """ Initializing the attributes """
        super().__init__()
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Creates a session, returns a session ID """
        session_id = super().create_session(user_id)
        if session_id
