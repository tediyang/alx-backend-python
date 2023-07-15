#!/usr/bin/env python3
"""
    a function that returns None or the first value of a list.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        safe_first_element: returns the first element of the list or None.

    Args:
        lst (Sequence[Any]): a sequence of any datatype.

    Returns:
        Union[Any, None]: returns the first element of any datatype or None.
    """
    if lst:
        return lst[0]
    else:
        return None
