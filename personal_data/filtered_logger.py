#!/usr/bin/env python3
"""
filtered_logger.py

A module for filtering and formatting log messages containing
sensitive data (PII).
"""

import logging
import os
import re
from typing import List

import mysql.connector
from mysql.connector import MySQLConnection


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates the values of specified fields in a log message.

    Args:
        fields (List[str]): List of field names to redact.
        redaction (str): String to replace sensitive values with.
        message (str): The log message containing data.
        separator (str): Separator used between fields in the log message.

    Returns:
        str: The log message with sensitive fields redacted.
    """
    pattern = f"({'|'.join(fields)})=.*?{re.escape(separator)}"
    return re.sub(
        pattern,
        lambda m: f"{m.group(1)}={redaction}{separator}",
        message
    )


class RedactingFormatter(logging.Formatter):
    """
    Formatter class for logging messages with sensitive information redacted.
    """

    REDACTION = "***"
    FORMAT = (
        "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    )
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter.

        Args:
            fields (List[str]): List of field names to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format a log record, redacting sensitive fields.

        Args:
            record (logging.LogRecord): Log record to format.

        Returns:
            str: Formatted log message with sensitive fields redacted.
        """
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message,
                            self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    Create and configure a logger for user data.

    Returns:
        logging.Logger: Configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Connect to the MySQL database using environment variables.

    Environment variables:
        PERSONAL_DATA_DB_USERNAME: Database username
        PERSONAL_DATA_DB_PASSWORD: Database password
        PERSONAL_DATA_DB_HOST: Database host
        PERSONAL_DATA_DB_NAME: Database name

    Returns:
        mysql.connector.MySQLConnection: Connection object to the MySQL database.
        The caller should call `close()` on the connection when finished.
    """
    user = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.environ.get("PERSONAL_DATA_DB_NAME")

    conn = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )
    return conn
