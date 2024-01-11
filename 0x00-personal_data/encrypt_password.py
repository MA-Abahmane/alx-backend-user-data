#!/usr/bin/env python3

"""
Encrypting passwords
User passwords should NEVER be stored in plain text in a database.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ takes in password and returns a hashed password """
    # Hash a password for the first time, with a randomly-generated salt
    hashed_pwd = bcrypt.hashpw((password.encode('UTF-8')),
                               bcrypt.gensalt())
    return hashed_pwd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ validate that the provided password matches the hashed password """
    # Check that an unhashed password matches one that has previously been
    # hashed
    return bcrypt.checkpw(password.encode('UTF-8'), hashed_password)
