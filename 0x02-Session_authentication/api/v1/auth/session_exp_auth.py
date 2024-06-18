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
            self.session_duration = int(getenv('SESSION_DURATION')
        except ValueError:
            self.session_duration = 0
