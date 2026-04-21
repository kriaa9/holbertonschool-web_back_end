#!/usr/bin/env python3
"""Module that provides a typed function to sum a list of floats."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floating-point numbers as a float."""
    return float(sum(input_list))
