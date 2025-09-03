#!/usr/bin/env python3
"""
encrypt_password.py

Provides a function to hash passwords using bcrypt.
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
