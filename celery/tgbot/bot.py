from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot('5255444441:AAFX2xVwHC5yG4TB9fGEN7bn2H6Fi8YDoO8')


async def send_to_channel(channelId, msg):
    await bot.send_message(channelId, msg)
    await bot.close_session()
