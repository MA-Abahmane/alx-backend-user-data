#!/usr/bin/env python3

"""
Sessions in database
DocDocDocDocDoc
"""

from models.user_session import UserSession
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """ SessionExpAuth class
    """

    def create_session(self, user_id=None):
        """ create_session
        """
        sessionID = super().create_session(user_id)
        if not sessionID:
            return None

        session_dictionary = {'user_id': user_id, 'session_id': sessionID}
        user = UserSession(**session_dictionary)
        user.save()

        return sessionID

    def user_id_for_session_id(self, session_id=None):
        """ user_id_for_session_id
        """
        userID = UserSession.search({'session_id': session_id})
        if not userID:
            return None
        return userID

    def destroy_session(self, request=None):
        """ destroy_session
        """
        l = request
        return False
