#!/usr/bin/env python3

"""
A function named filter_datum that returns the log message obfuscated
"""

import re


def filter_datum(fields, redaction, message, separator):
    """ A function that returns the log message obfuscated
        Arguments:
            fields: a list of strings representing all fields to obfuscate
            redaction: a string representing by what the field will be
              obfuscated
            message: a string representing the log line
            separator: a string representing by which character is separating
              all fields in the log line (message)
        The function should use a regex to replace occurrences of certain
          field values.
    """
    for field in fields:
        fltrd_message = re.sub(f'{field}=.*?{separator}',
                                f'{field}={redaction}{separator}', message)

    return fltrd_message
