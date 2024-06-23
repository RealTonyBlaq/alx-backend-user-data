#!/usr/bin/env python3
""" Filtered logger """

from typing import List
import re


def filter_datum(fields: List[str], rplc: str, msg: str, sp: str) -> str:
    """ Returns the log message obfuscated """
    return re.sub(f'({"|".join(fields)})=[^;]*', f'\\1={rplc}', message)

