from aiogram import Bot, Dispatcher, types, executor
import requests

from settings import token


bot = Bot(token)
dp = Dispatcher(bot)
ikb = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton('Котика!')],
                                          [types.KeyboardButton('Песика!')]],
                                resize_keyboard=True)
URL_CAT = 'https://cataas.com/cat'
URL_DOG = 'https://dog.ceo/api/breeds/image/random'


def get_cat():
    response = requests.get(URL_CAT)
    return response.content


def get_dog():
    response = requests.get(URL_DOG).json()
    response = requests.get(response['message'])
    return response.content


@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, text='Добро пожаловать', reply_markup=ikb)


@dp.message_handler(regexp='кот')
async def cat_message(message: types.Message):
    await bot.send_photo(message.chat.id, photo=get_cat())


@dp.message_handler(regexp=r'п[ёе]?с')
async def cat_message(message: types.Message):
    await bot.send_photo(message.chat.id, photo=get_dog())
    await bot.send_v


@dp.message_handler(content_types=['text'])
async def echo_message(message: types.Message):
    await bot.send_message(message.chat.id, text=message.text.upper())


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)