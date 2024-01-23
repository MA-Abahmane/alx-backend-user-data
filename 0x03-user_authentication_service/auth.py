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
        # find user by email
        try:
            user = self._db.find_user_by(email=email)
        except (NoResultFound, InvalidRequestError):
            return None

        if user:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)

            return user.session_id

        return False

    def get_user_from_session_id(self, session_id: str) -> User:
        """ returns the corresponding User or None
        """
        if session_id is None:
            return None
        # find user by session_id
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except (NoResultFound, InvalidRequestError):
            return None

    def destroy_session(self, user_id: int) -> None:
        """ updates the corresponding user’s session ID to None
        """
        # find user by id
        try:
            user = self._db.find_user_by(user_id=user_id)

        except (NoResultFound, InvalidRequestError):
            return None

        # update user session_id
        self._db.update_user(user.id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Find the user corresponding to the email and
            reset Users token
        """
        # find user by email
        try:
            user = self._db.find_user_by(email=email)

        except (NoResultFound, InvalidRequestError):
            raise ValueError('User not found')

        # update user session token
        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)

        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """ Uses the reset_token to find the corresponding user.
            If it does not exist, raise a ValueError exception
        """
        # find user by reset_token
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except (NoResultFound, InvalidRequestError):
            raise ValueError('User not found')

        # hash password and update users
        hash_pass = _hash_password(password)
        self._db.update_user(user.id,
                             hashed_password=hash_pass,
                             reset_token=None)
