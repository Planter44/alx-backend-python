#!/usr/bin/env python3
"""
module for 3-tasks.py
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task to execute the wait_random coroutine with a given
    max_delay and returns asyncio.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
