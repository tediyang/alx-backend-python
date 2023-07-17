#!/usr/bin/env python3
"""
    a function that returns an asyncio.Task
"""
import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_depth: int) -> Coroutine:
    """
        task_wait_random: return an asyncio.Task generated from wait_random

        Args:
            max_depth (int): the maximum number the async function will sleep

        Returns:
            IO: an asyncio.Task
    """
    return asyncio.create_task(wait_random(max_depth))
