import httpx
import asyncio
import time

URL = "https://httpbin.org/get"
N = 20

def sync_test():
    with httpx.Client() as client:
        for _ in range(N):
            client.get(URL)

async def async_test():
    async with httpx.AsyncClient() as client:
        tasks = [client.get(URL) for _ in range(N)]
        await asyncio.gather(*tasks)

def main():
    start = time.time()
    sync_test()
    print("Sync time:", time.time() - start, "seconds")

    start = time.time()
    asyncio.run(async_test())
    print("Async time:", time.time() - start, "seconds")

if __name__ == "__main__":
    main()
