#!/usr/bin/env python3
""" Main file """

import requests


def register_user(email: str, password: str) -> None:
    """ Tests POST /users endpoint """
    r = requests.post('127.0.0.1:5000/users', params={'email': email, 'password':})
log_in_wrong_password(email: str, password: str) -> None
log_in(email: str, password: str) -> str
profile_unlogged() -> None
profile_logged(session_id: str) -> None
log_out(session_id: str) -> None
reset_password_token(email: str) -> str
update_password(email: str, reset_token: str, new_password: str) -> None
