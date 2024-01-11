#!/usr/bin/env python3

"""
A function named filter_datum that returns the log message obfuscated
"""

import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ A function that returns the log message obfuscated """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """Create and configure a logger for user_data.

    Returns:
        logging.Logger: Configured logger object.
    """
    # Create a logger named "user_data"
    logger = logging.getLogger("user_data")

    # Set the logging level to INFO
    logger.setLevel(logging.INFO)

    # Create a list of PII_FIELDS for the formatter
    formatter = list(PII_FIELDS)

    # Create a StreamHandler to handle log records and set its formatter
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)
    stream_handler.setFormatter(RedactingFormatter(formatter))

    # Avoid propagating log messages to other loggers
    logger.propagate = False

    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.flds = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log records using filter_datum """
        record.msg = filter_datum(self.flds, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
