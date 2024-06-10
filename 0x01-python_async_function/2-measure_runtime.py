#!/usr/bin/env python3
"""
module for 2-measure_runtime.py
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function measures the total execution time of wait_n divided by n to
    find the average time
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))  # Execute the asynchronous function
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
