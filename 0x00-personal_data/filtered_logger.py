#!/usr/bin/env python3
""" Filtered logger """

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, sp: str) -> str:
    """ Returns the log message obfuscated """
    for field in fields:
        message = re.sub(fr'({field}=)[^{sp}]+({sp})', fr'\1{redaction}\2', message)
    return message
