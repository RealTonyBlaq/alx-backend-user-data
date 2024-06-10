#!/usr/bin/env python3
""" Auth Module """

from flask import request
from typing


class Auth:
    """ Defining the class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
