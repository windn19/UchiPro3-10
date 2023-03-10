import telebot

from settings import token


TOKEN = token
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    print(message)
    bot.send_message(message.chat.id, "Я тестовый бот!")


@bot.message_handler(content_types=['text'])
def echo_message(message):
    bot.send_message(message.chat.id, message.text.upper())


bot.infinity_polling()
