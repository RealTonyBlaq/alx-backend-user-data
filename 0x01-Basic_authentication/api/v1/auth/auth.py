#!/usr/bin/env python3
""" Auth Module """

from flask import request
from typing import List, TypeVar


class Auth:
    """ Defining the class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Requires authentication for the path

        Returns True if path is None
        Returns True if excluded_paths is None or empty
        Returns False if path is in excluded_paths
        """
        if path and excluded_paths and excluded_paths != []:
            if path[-1] != '/':
                path = path + '/'
            if path in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves auth from the Header """
        if request:
            header = request.headers.get('Authorization')
            return header
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates a User """
        return None


class BasicAuth(Auth):
    """ Defining an empty BasicAuth class """
    pass
