#!/usr/bin/env python3
"""Manual test script for running concurrent asyncio tasks."""

import asyncio

task_wait_n = __import__("4-tasks").task_wait_n


async def main() -> None:
    """Run task_wait_n and print delays in completion order."""
    print(await task_wait_n(5, 5))


if __name__ == "__main__":
    asyncio.run(main())
