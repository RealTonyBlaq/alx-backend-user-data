#!/usr/bin/env python3
""" Filtered logger """

from typing import List
import re


def filter_datum(fields: List[str], rplc: str, msg: str, separator: str):
    """ Returns the log message obfuscated """
    for field in fields:
        message = re.sub(fr'({field}=)[^{separator}]+({separator})', fr'\1{rplc}\2', message)
    return message
