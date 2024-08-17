#!/usr/bin/python3

import asyncio

async def say(message, delay):
    await asyncio.sleep(delay)
    print(message)

async def main():
    task1 = asyncio.create_task(say("wallace", 10))
    task2 = asyncio.create_task(say("sinatra", 5))

    await task1
    await task2

asyncio.run(main())
