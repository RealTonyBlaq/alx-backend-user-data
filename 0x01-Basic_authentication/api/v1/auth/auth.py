#!/usr/bin/env python3
""" Auth Module """

from flask import request
from typing import List


class Auth:
    """ Defining the class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Requires authentication for the path """
        pass

    def authorization_header(self, request=None) -> str:
        """ Retrieves auth from the Header """
        return None
