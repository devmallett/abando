import asyncio
from fin_scraper import FinViz

# new_ = FinViz()
# odl = FinViz()

# new_.pattern_one()
# odl.pattern_three()



async def naming():
    await foo("text")
    print("Devin")
    
    
    
async def foo(text):
    # print(text)
    await asyncio.sleep(1)
    print(text)
    
    
asyncio.run(naming())
# await naming()