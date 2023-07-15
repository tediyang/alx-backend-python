#!/usr/bin/env python3
"""
    a function that returns the sunm of a mixed list
"""
from typing import List, Union
from functools import reduce


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        sum_mixed_list

        Args:
            mxd_lst (List[int  |  float]): List with int and float

        Returns:
            float: sum in float
    """
    return reduce(lambda a, b: a + b, mxd_lst)
