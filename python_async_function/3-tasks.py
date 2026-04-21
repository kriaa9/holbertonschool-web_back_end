#!/usr/bin/env python3
"""Module that wraps a coroutine in an asyncio Task."""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return a task that runs wait_random with max_delay."""
    return asyncio.create_task(wait_random(max_delay))
