# Asynchronous operations
# Python offers several options for managing long running operations asynchronously.
# asyncio is the core library for supporting asynchronous operations, including async/await.
#
# https://docs.python.org/3/library/asyncio.html
# https://docs.python.org/3/reference/compound_stmts.html#async-def
# https://docs.python.org/3/reference/expressions.html#await

from timeit import default_timer
import aiohttp
import asyncio

# could be called with:  result = await load_data(session, 4)
async def load_data(task_id, session, delay):
    start_time = default_timer()
    print(f"[{task_id}] starting {delay}s timer ...")
    async with session.get(f"http://httpbin.org/delay/{delay}") as resp:
        text = await resp.text()
        elapsed_time = default_timer() - start_time
        print(f"[{task_id}] completed {delay}s timer in {elapsed_time}s with {text}")
        return text


# async allows for function to be await'd on, as well as, contain
async def main():
    # Start the timer
    start_time = default_timer()

    # Creating a single session
    async with aiohttp.ClientSession() as session:
        # Setup our tasks and get them running
        two_task = asyncio.create_task(load_data("A", session, 2))
        three_task = asyncio.create_task(load_data("B", session, 3))

        # Simulate other processing
        await asyncio.sleep(1)
        print("Doing other work")

        # Let's go get our values
        # await logically pauses the code, blocking execution until response comes back,
        # but the process is free to do other tasks.
        # await can only be used within an async construct
        two_result = await two_task
        print(f"two_result: {two_result}")
        three_result = await three_task
        print(f"three_result: {three_result}")

        # Print our results
        elapsed_time = default_timer() - start_time
        print(f"The operation took {elapsed_time:.2} seconds")


asyncio.run(main())
