from aiogram import Bot, Dispatcher, executor, types

from settings import token


bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help', 'start'])
async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, 'Добро пожаловать')


@dp.message_handler(content_types=['text'])
async def echo_message(message: types.Message):
    await bot.send_message(message.chat.id, text=message.text.upper())
    await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
