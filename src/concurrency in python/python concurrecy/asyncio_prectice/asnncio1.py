import asyncio

async def sayHello():
    print("Hello async world")
    await asyncio.sleep(1)
    print("world")

async def otherFunc():
    print("Hello async other function")
    await asyncio.sleep(1)
    print("world")

loop = asyncio.get_event_loop()

loop.run_until_complete(otherFunc())

loop.run_until_complete(sayHello())
print("I am sync code")
loop.close()