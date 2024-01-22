#!/usr/bin/env python3

""" DB module
"""

import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


logging.disable(logging.WARNING)


class DB:
    """ DB class
    """

    def __init__(self) -> None:
        """ Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """ Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ save the user to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """ returns the first row found in the users table
             as filtered by the method’s input arguments
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound('No results are found')
        except InvalidRequestError:
            raise InvalidRequestError('Wrong query arguments are passed')

    def update_user(self, user_id: int, **kwargs) -> None:
        """ update the user’s attributes
        """
        # Search user to update
        user = self.find_user_by(id=user_id)

        # Check if any passed argument doesn't correspond to a user attribute
        invalid_args = set(kwargs.keys()) - set(User.__table__.columns.keys())
        if invalid_args:
            raise ValueError("Passed argument that doesn't correspond to user")

        # Update user's attributes
        for key, val in kwargs.items():
            setattr(user, key, val)

        # Commit changes to the database
        self._session.commit()
