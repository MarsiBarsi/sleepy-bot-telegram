import telebot
from telebot import types

# bot init:
TOKEN = ''

bot = telebot.TeleBot(TOKEN)


# command /help
@bot.message_handler(commands=['help'])
def hlp(message):
    bot.send_message(message.chat.id, 'Привет, это помощь!')


@bot.message_handler(commands=["start"])
def start(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Настройки твоего сна", callback_data="sleep_settings")
    but_2 = types.InlineKeyboardButton(text="Как это работает?", callback_data="how_is_it_work")
    key.add(but_1, but_2)
    bot.send_message(message.chat.id, "Привет, я умный бот для сна. Выбери действие:", reply_markup=key)


@bot.callback_query_handler(func=lambda call: True)
def inline_catcher(call):
    if call.data == 'sleep_settings':
        sleep_settings(call.message)
    if call.data == 'how_is_it_work':
        hlp(call.message)


def sleep_settings(message):
    sent = bot.send_message(message.chat.id, 'Во сколько ты хочешь вставать?')

    hours = bot.send_message(message.chat.id, 'Сколько часов в день ты готов спать?')
    bot.send_message(message.chat.id,
                     'хорошо, ты будешь вставать в ' + sent.text + ' и спать по ' + hours.text + ' часов')


bot.polling(none_stop=True)