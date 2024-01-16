#!/usr/bin/env python3

"""
    Basic auth
    DocDocDocDoc
"""

import base64
from typing import TypeVar
from models.user import User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """ returns the Base64 part of the Authorization header
        """
        if authorization_header is None or\
            type(authorization_header) != str or\
                authorization_header.split(' ')[0] != 'Basic':
            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """ returns the decoded value of a given Base64 string
        """
        try:
            value = base64.b64decode(base64_authorization_header,
                                     validate=True)
            return value.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None or\
            type(decoded_base64_authorization_header) != str or\
                ':' not in decoded_base64_authorization_header:
            return None, None

        values = decoded_base64_authorization_header.split(':')
        return values[0], values[1]

    def user_object_from_credentials(self, user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """  returns the User instance based on his email and password
        """
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        if len(users) <= 0:
            return None

        if users[0].is_valid_password(user_pwd):
            return users[0]
        return None
