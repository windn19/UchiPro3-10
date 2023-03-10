import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from settings import token

TOKEN = token
URL_CAT = 'https://cataas.com/cat'
URL_DOG = 'https://dog.ceo/api/breeds/image/random'

bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Котика!'))
keyboard.add(KeyboardButton('Пёсика!'))


def get_cat():
    response = requests.get(URL_CAT)
    return response.content


def get_dog():
    response = requests.get(URL_DOG).json()
    response = requests.get(response['message'])
    return response.content


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Я тестовый бот!",
                     reply_markup=keyboard)


@bot.message_handler(regexp='кот')
def cat_image_message(message):
    photo = get_cat()
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='п[ёе]с')
def cat_image_message(message):
    photo = get_dog()
    bot.send_photo(message.chat.id, photo)


bot.infinity_polling()
