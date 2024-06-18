#!/usr/bin/env python3
""" SesionExpAuth Module """

from datetime import datetime, timedelta
from os import getenv
from session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """ Defining the SessionExpAuth model """

    def __init__(self) -> None:
        """ Initializing the attributes """
        super().__init__()
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None) -> str:
        """ Creates a session, returns a session ID """
        session_id = super().create_session(user_id)
        if session_id:
            self.user_id_by_session_id[session_id] = {'user_id': user_id, 'created_at': datetime.now()}
            return session_id
        return None

    def user_id_for_session_id(self, session_id=None) -> str:
        """ Returns the user_id that matches a session_id """
        if session_id:
            user_session = self.user_id_by_session_id.get(session_id)
            if user_session:
                if self.session_duration <= 0:
                    return user_session.get('user_id')
                if user_session.get('created_at'):
                    expire_in = timedelta()
        return None

