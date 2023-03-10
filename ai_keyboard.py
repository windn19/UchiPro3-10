from aiogram import Bot, Dispatcher, types, executor

from settings import token


bot = Bot(token)
dp = Dispatcher(bot)
ikb = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton('Hello', callback_data='get_hello')],
                                                  [types.InlineKeyboardButton('Bye', callback_data='get_bye')]])


@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, text='Добро пожаловать', reply_markup=ikb)


@dp.callback_query_handler(text='get_hello')
async def hello_message(message: types.CallbackQuery):
    await message.message.answer('Hello')
    # return message.answer()
    # await bot.send_message(message.chat.id, 'Hello')


@dp.callback_query_handler(text='get_bye')
async def hello_message(message: types.CallbackQuery):
    await message.message.answer('Bye')
    # return message.answer()


@dp.message_handler(content_types=['text'])
async def echo_message(message: types.Message):
    await bot.send_message(message.chat.id, text=message.text.upper())


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)