#!/usr/bin/env python3
""" Filtered logger """

from typing import List
import re


def filter_datum(fields: List[str, str], rplc: str, msg: str, sp: str) -> str:
    """ Returns the log message obfuscated """
    for field in fields:
        msg = re.sub(fr'({field}=)[^{sp}]+({re.escape(sp)})', fr'\1{rplc}\2', msg)
    return msg
