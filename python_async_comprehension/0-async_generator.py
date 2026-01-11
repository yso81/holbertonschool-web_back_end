#!/usr/bin/env python3
"""
This module defines an asynchronous generator coroutine
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times. In each iteration, it waits asynchronously for 1 second,
    then yields a random number between 0 and 10

    Returns:
        Generator[float, None, None]: An async generator yielding floats
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
