#!/usr/bin/env python3
"""
    a function that returns a value if a dictionary key is in the dictionary
    or return None.
"""
from typing import Mapping, TypeVar, Union, Any


# This is used to notify that any datatype that is sent as the parameter
# must be returned datatype. 
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
        safely_get_value: get the key if present or return None.

        Args:
            dct (Mapping[Any, Any]): any datatype as key and value
            key (Any): any datatype
            default (Union[T, None], optional): Defaults to None.

        Returns:
            Union[Any, T]: _description_
    """
    if key in dct:
        return dct[key]
    else:
        return default
