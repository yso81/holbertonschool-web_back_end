#!/usr/bin/env python3
"""
This module contains a function that returns an asyncio.Task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns a asyncio.Task

    Args:
        max_delay (int): The maximum delay for wait_random

    Returns:
        asyncio.Task: The task object created from the coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
