from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
import asyncio

# Bot tokenni shu yerga yozing:
API_TOKEN = "7796296335:AAFFUdOI_Qnj95VkGA8JaRzh-jJAclVOqug"

if not API_TOKEN:
    raise ValueError("Token bo'sh! Iltimos, to'g'ri token kiriting.")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    await message.answer("Salom! Men EXO Botman. Sizga qanday yordam bera olaman?")

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
