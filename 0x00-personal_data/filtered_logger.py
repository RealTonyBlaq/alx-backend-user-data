#!/usr/bin/env python3
""" Filtered logger """

from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str):
