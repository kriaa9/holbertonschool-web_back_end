#!/usr/bin/env python3
"""Module that provides a typed key/value conversion function."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing the key and the squared value as a float."""
    return (k, float(v * v))
