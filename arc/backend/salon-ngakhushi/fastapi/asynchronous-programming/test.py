import asyncio

async def main1():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# asyncio.run allows running the code without awaiting
asyncio.run(main1())

async def fetch_data(delay):
    print("\nFetching data...")
    await asyncio.sleep(delay)
    print("Data Fetched")
    return {"data": ["Data1", "Data2"]}

async def main2():
    print("\nStarting main coroutine")
    task= fetch_data(2) # initiates fetch_data method
    print("End of main coroutine")    
    result =  await task # starts the executing of fetch_data method
    print(f"Received result: {result}")
    
asyncio.run(main2())
