#!/usr/bin/env python3
"""Module that provides a typed function for sequence-length pairing."""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return each sequence from the iterable paired with its length."""
    return [(i, len(i)) for i in lst]
