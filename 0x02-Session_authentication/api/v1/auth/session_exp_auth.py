#!/usr/bin/env python3
""" SesionExpAuth Module """

from os import getenv
from session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """ Defining the SessionExpAuth model """

    def __init__(self) -> None:
        """ Initializing the attributes """
        super().__init__()
        self.session_duration = getenv()
