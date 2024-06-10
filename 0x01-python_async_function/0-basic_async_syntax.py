#!/usr/bin/env python3
"""
module 0-basic_async_syntax.py 
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function asynchronously waits for a random time between 0 and
    max_delay seconds and eventually returns it
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
