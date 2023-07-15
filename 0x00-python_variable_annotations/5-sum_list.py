#!/usr/bin/env python3
"""
    a function that sums the value in a list.
"""
from functools import reduce


def sum_list(input_list: list[float]) -> float:
    """
        sum_list: return the sum of the list in float.

        Args:
            input_list (list[float]): list with only float as parameters

        Returns:
            float: the sum of the list in float
    """
    return reduce(lambda a, b: a + b, input_list)
