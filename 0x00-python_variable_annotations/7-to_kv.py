#!/usr/bin/env python3
"""
    a function that accepts a str param and float/int param and returns
    a tuple of the values.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        to_kv: returns a tuple of string as first value and sq if int or
        float as second value.

    Args:
        k (str): string parameter
        v (Union[int, float]): integer or float parameter

    Returns:
        Tuple[str, float]: string ad=nd int/float
    """
    return k, v**2
