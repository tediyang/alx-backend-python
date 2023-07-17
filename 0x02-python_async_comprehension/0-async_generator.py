#!/usr/bin/env python3
"""
    a function that creates an async generator
"""
import asyncio
from random import uniform
from typing import Generator
# from typing import AsyncGenerator


async def async_generator() -> Generator[float, None, None]:
    """
        async_generator: yields a randomly generated float.

    Returns:
        float: randomly generated float
    """
    for _ in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
