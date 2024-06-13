#!/usr/bin/env python3
""" Password hashing """

from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """ Takes in a password string and returns bytes """
    if password and type(password) is str:
        salt = gensalt()
        password = password.encode('utf-8')
        return hashpw(password, salt)
