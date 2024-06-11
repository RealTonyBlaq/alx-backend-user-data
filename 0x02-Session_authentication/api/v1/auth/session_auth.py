#!/usr/bin/env python3
""" SessionAuth Model """

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Defining the class SessionAuth that authenticates a session """

    def __init__(self) -> None:
        """ Initializes the inherited attributes """
        super().__init__()
