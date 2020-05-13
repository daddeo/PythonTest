# https://docs.python.org/3/library/asyncio-task.html

from timeit import default_timer
import asyncio


async def factorial(name, number):
    start_time = default_timer()
    f = 1
    for i in range(2, number + 1):
        print(f"[{name}] compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    elapsed_time = default_timer() - start_time
    print(f"[{name}] factorial({number}) = {f} in {elapsed_time}s")


async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 5), factorial("B", 10), factorial("C", 15),
    )


asyncio.run(main())
