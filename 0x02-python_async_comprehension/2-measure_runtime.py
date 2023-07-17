#!/usr/bin/env python3
"""
    a function that measures the total time of an async comprehension
"""
import asyncio
import time

comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        measure_runtime: returns the total time taken for async to complete.

        Returns:
            float: this return value will be between 10 and 10.2. This is due
            to the fact that the generator waited 1 second after yield and the
            yielded 10 times.
    """
    start = time.perf_counter()
    await asyncio.gather(comp(), comp(), comp(), comp())
    end = time.perf_counter()
    return end - start
