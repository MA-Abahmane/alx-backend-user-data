#!/usr/bin/env python3

"""
    class to manage the API authentication
"""

import fnmatch
from flask import request
from typing import List, TypeVar


class Auth:
    """ class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ authentication require
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        if path[-1] != '/':
            path += '/'

        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ authorization header
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user
        """
        return None
