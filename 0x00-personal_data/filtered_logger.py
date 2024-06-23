#!/usr/bin/env python3
""" Filtered logger """

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, messsage: str, separator: str) -> str:
    """ Returns the log message obfuscated """
    return re.sub(f'({"|".join(fields)})=[^{sp}]*', f'\\1={rplc}', msg)
