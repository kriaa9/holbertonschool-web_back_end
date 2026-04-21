#!/usr/bin/env python3
"""Manual test script for creating an asyncio task."""

import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def main() -> None:
    """Create a task, print its class, and await its completion."""
    task = task_wait_random(5)
    print(task.__class__)
    print(await task)


if __name__ == "__main__":
    asyncio.run(main())
