#!/usr/bin/env python3
"""Module that provides a safe first-element accessor using duck typing."""

from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a sequence or None when it is empty."""
    if lst:
        return lst[0]
    return None
