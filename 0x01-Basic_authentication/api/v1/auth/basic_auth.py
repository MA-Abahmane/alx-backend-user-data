#!/usr/bin/env python3

"""
    Basic auth
    DocDocDocDoc
"""

import base64
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
