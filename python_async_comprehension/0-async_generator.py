#!/usr/bin/env python3
"""
Module contenant un générateur asynchrone
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Générateur asynchrone qui yield 10 nombres aléatoires

    Boucle 10 fois, attend 1 seconde à chaque itération,
    puis yield un nombre aléatoire entre 0 et 10

    Yields:
        Un nombre flottant aléatoire entre 0 et 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
