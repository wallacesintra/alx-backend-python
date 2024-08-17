# Async

## Async and await

`async` - used to declare a function as asynchronous.

`await` - (can be used in a async function) pauses the execution of async function until the awaited coroutine is complete.

installing:

```bash
pip install --upgrade pip aiohttp aiofiles
```

```python

import asyncio

async def say_hello():
    print("hello")
    await asyncio.sleep(1)
    print("world")

asyncio.run(say_hello())

```

## running concurrent coroutines

use `asyncio.gather()`

```python
async def task1():
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```

## creating asyncio Tasks

Tasks wrap coroutines and allow them to run concurrently.

use `asyncio.create_task()`

```python
async def say(message, delay):
    await asyncio.sleep(delay)
    print(message)

async def main():
    task1 = asyncio.create_task(say("hello", 2))
    task2 = asyncio.create_task(say("world", 3))

    await task1
    await task2

asyncio.run(main())
```

## random module

random module provides functions to generate random numbers, select random elements, shuffle sequences...

```python
import random

print(random.random()) # random float between 0 and 1
print(random.randint(1, 10)) # random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry'])) # random select from the list
```
