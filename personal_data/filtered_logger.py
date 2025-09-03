#!/usr/bin/env python3
"""
Module for filtering sensitive data from log messages
"""
import re
from typing import List

def filter_datum(fields: List[str], redaction: str,
    message: str, separator: str) -> str:
    """
    Obfuscates the values of specified fields in a log message.
    """
    pattern = f"({'|'.join(fields)})=.*?{re.escape(separator)}"
    return re.sub(pattern,
        lambda m: f"{m.group(1)}={redaction}{separator}",
        message)

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))




