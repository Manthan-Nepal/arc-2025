import asyncio

async def fetch_data(id, delay):
    print(f"ID {id} Starting to fetch...")
    await asyncio.sleep(delay)
    return {"ID": id, "data": f"Data from ID {id}"}
    

async def main1():
    task1= asyncio.create_task(fetch_data(1, 3))
    task2= asyncio.create_task(fetch_data(2, 2))
    task3= asyncio.create_task(fetch_data(3, 4))
    
    output1= await task1
    output2= await task2
    output3= await task3
    print(output1, output2, output3)
    
async def main2():
    # no error handling with gather
    outputs= await asyncio.gather(fetch_data(1, 3), fetch_data(2, 2), fetch_data(3, 4))
    
    for output in outputs:
        print(f"\nData received: {output}")

async def main3():
    # error handling with TaskGroup
    tasks= []
    async with asyncio.TaskGroup() as tg:
        for i, delay in enumerate([3, 2, 4], start=1):
            task= tg.create_task(fetch_data(i, delay))
            tasks.append(task)
    
    outputs= [task.result() for task in tasks]
    
    for output in outputs:
        print(f"\nData received: {output}")
    
    
# asyncio.run(main1())
# asyncio.run(main2())
asyncio.run(main3())