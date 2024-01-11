#!/usr/bin/env python3

"""
A function named filter_datum that returns the log message obfuscated
"""

import re


def filter_datum(fields, redaction, message, separator):
    """ A function that returns the log message obfuscated """
    for field in fields:
        fltrd_message = re.sub(f'{field}=.*?{separator}',
                                f'{field}={redaction}{separator}', message)
    return fltrd_message
