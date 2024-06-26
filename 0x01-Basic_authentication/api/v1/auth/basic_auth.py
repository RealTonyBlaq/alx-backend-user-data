#!/usr/bin/env python3
""" Basic Authentication Model """

from api.v1.auth.auth import Auth
from base64 import b64decode
import binascii
from models.user import User
from typing import TypeVar


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

    def decode_base64_authorization_header(
          self, base64_authorization_header: str) -> str:
        """
        Return None if base64_authorization_header is None
        Return None if base64_authorization_header is not a string
        Return None if base64_authorization_header is not a valid Base64
        """
        if base64_authorization_header and type(
              base64_authorization_header) is str:
            try:
                decoded = b64decode(base64_authorization_header)
                return decoded.decode('utf-8')
            except binascii.Error:
                pass
        return None

    def extract_user_credentials(
          self, decoded_base64_authorization_header: str) -> (str, str):
        """
        This method returns 2 values:

        Return None, None if decoded_base64_authorization_header is None
        Return None, None if decoded_base64_authorization_header
            is not a string
        Return None, None if decoded_base64_authorization_header
            doesn't contain ':'

        Otherwise, return the user email and the user password
        """
        if decoded_base64_authorization_header and type(
              decoded_base64_authorization_header) is str:
            if ':' in decoded_base64_authorization_header:
                user, password = decoded_base64_authorization_header.split(
                    ':', 1)
                return (user, password)
        return (None, None)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Return None if user_email is None or not a string
        Return None if user_pwd is None or not a string
        Return None if your database (file) doesnt contain any User
            instance with email equal to user_email - you should use
            the class method search of the User to lookup the list of
            users based on their email. Don't forget to test all cases:
            “what if there is no user in DB?”, etc.
        Return None if user_pwd is not the password of the User instance found-
            use the method is_valid_password of User

        Otherwise, return the User instance
        """
        if all([user_email, type(user_email) is str, user_pwd,
                type(user_pwd) is str]):
            try:
                users = User.search({"email": user_email})
                for user in users:
                    if user.is_valid_password(user_pwd):
                        return user
            except Exception:
                pass
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Overloads Auth and retrieves the User instance for a request
        """
        header = self.authorization_header(request)
        auth_header = self.extract_base64_authorization_header(header)
        decoded_header = self.decode_base64_authorization_header(auth_header)
        user_email, pwd = self.extract_user_credentials(decoded_header)
        user_instance = self.user_object_from_credentials(user_email, pwd)

        return user_instance
