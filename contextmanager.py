#!/usr/bin/env python3
from contextlib import contextmanager
import time


class Timer:
    """
    Timer class
    """

    def __init__(self):
        self._start = None
        self.elapsed = 0.0

    def __enter__(self):
        if self._start is not None:
            raise RuntimeError('Time already started')
        self._start = time.perf_counter()
        return self

    def __exit__(self, *args):
        if self._start is None:
            raise RuntimeError('Time not started')
        end = time.perf_counter()
        self.elapsed += end - self._start
        self._start = None


@contextmanager
def timed():
    start = time.time()
    print(f"start at {start}")
    try:
        yield  # yield to body of `with` statement
    finally:
        end = time.time()
        print(f"End at {end}, {end - start} elapsed")


if __name__ == '__main__':
    with Timer() as t:
        time.sleep(4)
    print(t.elapsed)

    # method 2: use decorator
    with timed():
        time.sleep((3))
