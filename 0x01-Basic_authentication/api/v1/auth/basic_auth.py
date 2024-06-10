#!/usr/bin/env python3
""" Basic Authentication Model """

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Defining an empty BasicAuth class. """

    def __init__(self) -> None:
        """ Inintializes the parent class Auth """
        super().__init__()
