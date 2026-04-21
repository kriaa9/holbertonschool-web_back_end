#!/usr/bin/env python3
"""Module that provides typed retrieval from mappings with a fallback."""

from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Optional[T] = None
) -> Union[Any, T]:
    """Return dct[key] when present, otherwise return default."""
    if key in dct:
        return dct[key]
    return default
