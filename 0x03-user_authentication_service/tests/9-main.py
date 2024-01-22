#!/usr/bin/env python3
"""
Main file
"""
from auth import _generate_uuid

ident = _generate_uuid()

print(ident)
print(_generate_uuid())
