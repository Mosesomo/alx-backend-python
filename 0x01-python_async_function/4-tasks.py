#!/usr/bin/env python3
"""Importing modules"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """an async routine called wait_n that
    takes in 2 int arguments (in this order):
    n and max_delay
    spawn wait_random n times with the specified max_delay
    return the list of all the delays (float values)
    """

    wait_times = await asyncio.gather(*(task_wait_random(max_delay)
                                        for _ in range(n)))
    return sorted(wait_times)
