from tasks import add
import asyncio

def sum(a, b):
    res = a + b
    return res

async def main():
  print('main')
  add.delay(4, 4)
  # await asyncio.sleep(1)
  print('called')

asyncio.run(main())