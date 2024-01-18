#!/usr/bin/env python3

"""
    Session Authentication mechanism
"""

import uuid
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session Authentication class
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        sess_id = uuid.uuid4()
        self.user_id_by_session_id[str(sess_id)] = user_id

        return str(sess_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ returns a User instance based on a cookie value
        """
        sess_cookie = self.session_cookie(request)

        user_id = self.user_id_for_session_id(sess_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None) -> bool:
        """ deletes the user session / logout:
        """
        if request is None:
            return False

        sess_cookie = self.session_cookie(request)
        if sess_cookie is None:
            return False

        user_id = self.user_id_for_session_id(sess_cookie)
        if user_id is None:
            return False

        del self.user_id_by_session_id[sess_cookie]
        return True
