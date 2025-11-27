#!/usr/bin/env python3
"""
Module contenant une coroutine avec async comprehension
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    