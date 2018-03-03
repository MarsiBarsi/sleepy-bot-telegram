import telebot
from telebot import types

# bot init:
TOKEN = 'your token'

bot = telebot.TeleBot(TOKEN)

# command /help
@bot.message_handler(commands=['help'])
def hlp(message):
    bot.send_message(message.chat.id, 'Привет, это помощь!')


@bot.message_handler(commands=['start'])
def start(message):
    # additional keyboard testing
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    button_time = types.KeyboardButton(text="Задать время для сна", callback_data="set_time")
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "=)", reply_markup=keyboard)

    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(message.chat.id, 'Всем привет. И даже тебе, {name}!'.format(name=message.text))
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)


bot.polling()
