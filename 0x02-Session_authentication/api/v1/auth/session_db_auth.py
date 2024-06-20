#!/usr/bin/env python3
""" SessionDBAuth Module """

from os import getenv
from api.v1.auth.session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
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
        user_session.save()
        return sess_id

    def user_id_for_session_id(self, session_id=None) -> str:
        """ Returns the user_id that matches a session_id """
        if session_id:
            users = UserSession.search({'session_id': session_id})
            if users is None or users == []:
                return None

            user = users[0]
            duration = getenv('SESSION_DURATION')
            current_time = datetime.now()

            if duration is None or duration <= 0:
                return user.user_id
            if current_time > user.created_at + timedelta(seconds=duration):
                return None
            return user.user_id

    def destroy_session(self, request=None) -> None:
        """ Deletes a user session """
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                users = UserSession.search({'session_id': session_id})
                if users:
                    for user in users:
                        user.remove()
        return None
