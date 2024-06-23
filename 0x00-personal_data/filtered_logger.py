#!/usr/bin/env python3
""" Filtered logger """

from typing import List
import re


def filter_datum(fields: List[str], rpn: str, message: str, separator: str):
    """ Returns the log message obfuscated """
    for field in fields:
        message = re.sub(fr'({field}=)[^{separator}]+({separator})', fr'\1{redaction}\2', message)
    return message
