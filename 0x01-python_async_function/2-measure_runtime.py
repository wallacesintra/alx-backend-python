#!/usr/bin/env python3

"""
measure_time function with integers n and max_delay
as arguments that measures the total execution time for wait_n(n, max_delay),
returns total_time / n (float)
"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    measure runtime
    """

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
