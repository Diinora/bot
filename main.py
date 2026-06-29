import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("API")
bot=Bot(token=TOKEN)
dp = Dispatcher()




@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Assalawma aleykum 😊")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Qanday jardem bere alaman?")


async def main():

    print("bot iske qosildi ✅")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())