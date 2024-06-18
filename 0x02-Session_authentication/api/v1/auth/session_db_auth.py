#!/usr/bin/env python3
""" SessionDBAuth Module """

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    Defining the new SessionSBAuth system that stores
    session_ids to the database.
    """

    def create_session(self, user_id=None) -> str:
        """ Creates and stores a session_id """
        sess_id = super().create_session(user_id)
        user_session = UserSession(user_id=user_id, session_id=sess_id)
        