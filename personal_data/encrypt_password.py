#!/usr/bin/env python3
"""
encrypt_password.py

Provides functions to hash and validate passwords using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password with a salt using bcrypt.

    Args:
        password (str): The plain-text password.

    Returns:
        bytes: The salted, hashed password.
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if a password matches a given hashed password.

    Args:
        hashed_password (bytes): The salted, hashed password.
        password (str): The plain-text password to verify.

    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)
