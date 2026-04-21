#!/usr/bin/env python3
"""Manual test script for running concurrent wait_random coroutines."""

import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


async def main() -> None:
    """Run wait_n and print delays returned in completion order."""
    print(await wait_n(5, 5))


if __name__ == "__main__":
    asyncio.run(main())
