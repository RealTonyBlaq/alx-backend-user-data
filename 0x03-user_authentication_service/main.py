#!/usr/bin/env python3
""" Main file """

import requests


def register_user(email: str, password: str) -> None:
    """ Tests POST /users endpoint """
    r = requests.post('http://127.0.0.1:5000/users',
                      data={'email': email, 'password': password})
    assert r.json() == {"email": email, "message": "user created"}
    assert r.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """ Tests POST /sessions with wrong login details """
    r = requests.post('http://127.0.0.1:5000/sessions',
                      data={'email': email, 'password': password})
    assert r.status_code == 401


def log_in(email: str, password: str) -> str:
    """ Tests POST /sessions with the correct login details """
    r = requests.post('http://127.0.0.1:5000/sessions',
                      data={'email': email, 'password': password})
    assert r.json() == {"email": email, "message": "logged in"}
    assert r.status_code == 200


def profile_unlogged() -> None:
    """ Tests GET /profile without a session_id """
    r = requests.get('http://127.0.0.1:5000/profile')
    assert r.status_code == 403


def profile_logged(session_id: str) -> None:
    """ Tests GET /profile with a session_id """
    r = requests.get('http://127.0.0.1:5000/profile',
                     cookies={'session_id': session_id})
    assert r.status_code == 200


def log_out(session_id: str) -> None:
    """ Tests DELETE /sessions """
    r = requests.delete('http://127.0.0.1:5000/sessions',
                        cookies={'session_id': session_id}, allow_redirects=True)
    assert r.json() == {"message": "Bienvenue"}
    assert r.status_code == 200
reset_password_token(email: str) -> str
update_password(email: str, reset_token: str, new_password: str) -> None


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
