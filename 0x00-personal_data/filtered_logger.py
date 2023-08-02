#!/usr/bin/env python3
"""Filtered Logger Module"""
import re


def filter_datum(fields, redaction, message, seprator):
    """Obfuscates message from logger"""
    for field in fields:
        message = re.sub(r'{}=.*?{}'.format(field, seprator),
                         '{}={}{}'.format(field, redaction, seprator), message)
    return message
