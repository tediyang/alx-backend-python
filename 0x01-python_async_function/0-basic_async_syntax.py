#!/usr/bin/env python3
"""
    an async function that awaits a random function.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
        wait_random: this returns a randiom float value after waiting for it.

        Args:
            max_delay (int): maximum delay

        Returns:
            int: the generated value
    """
    random.seed(444)  # whenever this code runs it returns the same values
    value = random.uniform(0, max_delay + 1)
    await asyncio.sleep(value)
    return value
