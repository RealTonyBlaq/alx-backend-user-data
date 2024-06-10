#!/usr/bin/env python3
""" Auth Module """

from flask import request
from typing import List, TypeVar


class Auth:
    """ Defining the class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Requires authentication for the path """
        if path and excluded_paths and excluded_paths != []:
            if path[-1] != '/'
            if path in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves auth from the Header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates a User """
        return None
