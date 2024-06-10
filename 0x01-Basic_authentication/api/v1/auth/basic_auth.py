#!/usr/bin/env python3
""" Basic Authentication Model """

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Defining an empty BasicAuth class. """

    def __init__(self) -> None:
        """ Inintializes the parent class Auth """
        super().__init__()

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
