#!/usr/bin/env python3
""" Basic Authentication Model """

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Defining an empty BasicAuth class. """

    def __init__(self) -> None:
        """ Inintializes the parent class Auth """
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization
        header for a Basic Authentication

        Return None if authorization_header is None
        Return None if authorization_header is not a string
        Return None if authorization_header doesn't start by Basic
            (with a space at the end)
        Otherwise, return the value after Basic (after the space)
        """
        if authorization_header and type(authorization_header) is str:
            b64 = authorization_header.split(' ')
            if b64[0] == 'Basic':
                return b64[1]
        return None

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Return None if base64_authorization_header is None
        Return None if base64_authorization_header is not a string
        Return None if base64_authorization_header is not a valid Base64
        """
        if base64_authorization_header and type(base64_authorization_header) is str:
            try:
                decoded = base64.b64decode()
