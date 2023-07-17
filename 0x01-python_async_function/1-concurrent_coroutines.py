#!/usr/bin/env python3
"""
    a function that executes several coroutines at the same time.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        wait_n: runs the wait_random function n times

        Args:
            n (int): the number of times the wait_random func will be called
            max_delay (int): the maximum time a func can be delayed

        Returns:
            List[float]: a list of all the delay times.
    """
    data = []
    i = 0
    while i < n:
        call = wait_random(max_delay)
        # add the called function into a list
        data.append(call)
        i += 1

    # return a list of the function: in order of completion
    return [await task for task in asyncio.as_completed(data)]
