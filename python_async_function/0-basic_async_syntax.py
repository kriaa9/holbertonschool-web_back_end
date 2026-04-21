#!/usr/bin/env python3
"""Module that defines a basic asynchronous wait coroutine."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return that delay as a float."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
