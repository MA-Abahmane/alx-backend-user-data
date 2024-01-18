#!/usr/bin/env python3

"""
SET Expiration date to a Session ID
DocDocDocDocDoc
"""

import datetime
from os import getenv
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """ SessionExpAuth class
    """

    def __init__(self):
        """ Constructor
        """
        try:
            value = int(getenv('SESSION_DURATION'))
        except Exception:
            value = 0
        self.session_duration = value

    def create_session(self, user_id=None):
        """ session creation
        """
        sessionID = super().create_session(user_id)
        if sessionID is None:
            return None

        session_dictionary = {'user_id': user_id, 'created_at': datetime.now()}
        self.user_id_by_session_id[sessionID] = session_dictionary

        return sessionID

    def user_id_for_session_id(self, session_id=None):
        """ user id for session id
        """
        user_info = self.user_id_by_session_id.get(session_id)
        if session_id is None or user_info is None:
            return None

        if self.session_duration <= 0:
            return user_info.get('user_id')

        if 'created_at' not in user_info.keys():
            return None

        create_date = user_info.get('created_at')
        allowedWIN = create_date + datetime.timedelta(
            seconds=self.session_duration)
        if allowedWIN < datetime.now():
            return None
        return user_info.get('user_id')
