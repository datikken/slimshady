import asyncio
from tgbot.bot import send_to_channel

def sum(a, b):
    res = a + b
    return res

async def main():
  # print('main')
  # add.delay(4, 4)
  await send_to_channel(-1001510060014, 'done')
  
  print('called')

asyncio.run(main())