#!/usr/bin/env python3
"""Manual test script for the wait_random coroutine."""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def main() -> None:
    """Run wait_random three times and print each returned delay."""
    print(await wait_random())
    print(await wait_random())
    print(await wait_random())


if __name__ == "__main__":
    asyncio.run(main())
