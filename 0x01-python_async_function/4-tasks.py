#!/usr/bin/env python3
"""
module for 4-tasks.py
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This method spawns task_wait_random n times with the specified max_delay
    Returns:
    List[float]: A list of float values representing the delays,
    sorted by completion order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results
