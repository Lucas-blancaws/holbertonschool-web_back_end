#!/usr/bin/env python3
"""
Docstring for 1-async_comprehension.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers from
    sync_generator using async comprehension.
    """
    return [num async for num in async_generator()]
