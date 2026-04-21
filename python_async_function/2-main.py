#!/usr/bin/env python3
"""Manual test script for measuring average coroutine runtime."""

measure_time = __import__("2-measure_runtime").measure_time


def main() -> None:
    """Run measure_time and print the average elapsed time per coroutine."""
    print(measure_time(5, 9))


if __name__ == "__main__":
    main()
