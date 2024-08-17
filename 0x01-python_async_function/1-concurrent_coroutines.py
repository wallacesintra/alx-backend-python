#!/usr/bin/env python3

"""
wait_n that takes in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    wait = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(wait)
