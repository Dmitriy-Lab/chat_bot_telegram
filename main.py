# BOT_NAME = @py_test_small_bot

pip install aiogram nest_asyncio
import nest_asyncio
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
import requests

nest_asyncio.apply()

logging.basicConfig(level=logging.INFO)

API_TOKEN = '7502210955:AAHjDSBRjvgNHidx3owUaThwuDr1IncGJmw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добрый день. Как вас зовут?")

@dp.message(F.text)
async def say_hello(message: types.Message):
    dollar_info = get_dollar_info()
    await message.answer(f"Рад знакомству, {message.text}! Курс доллара сегодня {round(dollar_info, 2)} ")

def get_dollar_info():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    return data['Valute']['USD']['Value']

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
