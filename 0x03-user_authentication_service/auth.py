#!/usr/bin/env python3

"""
Auth Class
    &
Helping Functions
"""

import uuid
import bcrypt
import logging
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import User
from db import DB

logging.disable(logging.WARNING)


def _hash_password(password: str) -> bytes:
    """ returns a salted hash of the input password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('UTF-8'), salt)


def _generate_uuid() -> str:
    """ return a string representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """ Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Constructor
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register user
        """
        # Check is user account exists, if not; create one
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')

        except NoResultFound:
            pass
        hash_pass = _hash_password(password).decode('UTF-8')

        return self._db.add_user(email, hash_pass)

    def valid_login(self, email: str, password: str) -> bool:
        """ Validate User account
        """
        # find user by email
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                # Check if the provided password matches the hashed password
                pswd = password.encode('UTF-8')
                hashed_pswd = user.hashed_password.encode('UTF-8')
                if bcrypt.checkpw(pswd, hashed_pswd):
                    return True
        except (NoResultFound, InvalidRequestError):
            return False
        return False

    def create_session(self, email: str) -> str:
        """ create a user session and return the session ID as a string
        """
        try:
            user = self._db.find_user_by(email=email)
        except (NoResultFound, InvalidRequestError):
            return None

        if user:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)

            return user.session_id

        return False
