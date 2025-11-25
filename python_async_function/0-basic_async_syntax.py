#!/usr/bin/env python3
"""
Module avec une coroutine asynchrone
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine asynchrone qui attend un délai aléatoire
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
