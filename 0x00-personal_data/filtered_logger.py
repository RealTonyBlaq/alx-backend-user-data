#!/usr/bin/env python3
""" Filtered logger """

from typing import List
import re


def filter_datum(fields: List[str], rplc: str, msg: str, sp: str) -> str:
    """ Returns the log message obfuscated """
    sp = re.escape(sp)
    return re.sub(f'({"|".join(fields)})=[^{sp}]*', f'\\1={rplc}', msg)
