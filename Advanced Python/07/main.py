import asyncio
import time
import sys
import aiohttp


async def fetch(name, session, queue):
    while True:
        url = await queue.get()
        try:
            async with session.get(url) as resp:
                await resp.read()
                print(name)
        finally:
            queue.task_done()


async def get_urls(urls, queue):
    counter = 0
    with open(urls, encoding='utf-8') as file:
        for url in file:
            await queue.put(url)
            if counter % 10 == 0:
                await asyncio.sleep(0.1)
            counter += 1
    print("-----------------------All-----------------------")


async def crawl(urls, threads=5):
    queue = asyncio.Queue()
    task = asyncio.create_task(get_urls(urls, queue))
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(fetch(f"coro_{i}", session, queue))
            for i in range(threads)
        ]
        await task
        await queue.join()

    for val in tasks:
        val.cancel()

if __name__ == "__main__":
    args = sys.argv
    thrs = int(args[1]) if args[1].isdigit() else int(args[2])
    us = args[1] if not args[1].isdigit() else args[2]
    print(thrs, us)
    start = time.time()
    asyncio.get_event_loop().run_until_complete(crawl(us, thrs))
    end = time.time()
    print(end - start)
