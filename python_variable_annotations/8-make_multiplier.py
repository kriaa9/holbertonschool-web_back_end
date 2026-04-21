#!/usr/bin/env python3
"""Module that provides a typed closure factory for multiplication."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""

    def multiply(value: float) -> float:
        """Multiply the provided value by the captured multiplier."""
        return value * multiplier

    return multiply
