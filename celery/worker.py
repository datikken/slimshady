import asyncio
from tasks import add

async def main():
  print('main')
  add.delay(4, 4)
  print('called')

asyncio.run(main())
