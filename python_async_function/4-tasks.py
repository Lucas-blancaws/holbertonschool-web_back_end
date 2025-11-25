#!/usr/bin/env python3
"""
Module pour exécuter plusieurs tasks concurrentes
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n (n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n fois avec max_delay spécifi
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
 
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays
