#!/usr/bin/env python3
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def use_await():
    await say_after(3, 'world')
    await say_after(2, 'hello')
    print(f'use_await finished at t={time.time() - start} seconds')


async def use_tasks():
    task_a = asyncio.create_task(say_after(3, 'world'))
    task_b = asyncio.create_task(say_after(2, 'hello'))
    await task_a
    await task_b
    print(f'use_tasks finished at t={time.time() - start} seconds')


start = time.time()
asyncio.run(use_await()) #call async code from sync code
asyncio.run(use_tasks())
