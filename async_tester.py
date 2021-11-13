import asyncio


async def naming():
    print("Devin")
    await foo("text")
    
    
async def foo(text):
    print(text)
    await asyncio.sleep(1)
    
    
asyncio.run(naming())
# await naming()