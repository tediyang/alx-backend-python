#!/usr/bin/env python3
"""
    measure the runtime of the async function
"""
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> int:
    """
        measure_time: returns the average time taken to finish the process.

        Args:
            n (int): the number of times the function will run
            max_delay (int): the maximum time the function will sleep

        Returns:
            int: returns the average time.
    """
    start = time.perf_counter()
    wait_n(n, max_delay)
    end = time.perf_counter()
    return (end - start) / n    
