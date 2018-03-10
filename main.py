import telebot
from telebot import types
import config
import dbworker
import messages

# bot init:
bot = telebot.TeleBot(config.token)


# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):
    hlp(message)
    state = dbworker.get_current_state(message.chat.id)
    if state == config.States.S_ENTER_NAME.value:
        bot.send_message(message.chat.id, messages.forgotten_name)
    elif state == config.States.S_ENTER_TIME.value:
        bot.send_message(message.chat.id, messages.forgotten_time)
    elif state == config.States.S_SEND_HOURS.value:
        bot.send_message(message.chat.id, messages.forgotten_hours)
    else:  # Под "остальным" понимаем состояние "0" - начало диалога
        bot.send_message(message.chat.id, messages.hello_new)
        dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, messages.reset_mes)
    dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_NAME.value)
def user_entering_name(message):
    # В случае с именем не будем ничего проверять, пусть хоть "25671", хоть Евкакий
    bot.send_message(message.chat.id, "Отличное имя, запомню! Теперь укажи, во сколько ты встаешь!")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_TIME.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_TIME.value)
def user_entering_time(message):
    # А вот тут сделаем проверку
    if not message.text.isdigit():
        # Состояние не меняем, поэтому только выводим сообщение об ошибке и ждём дальше
        bot.send_message(message.chat.id, "Что-то не так, попробуй ещё раз!")
        return
    # На данном этапе мы уверены, что message.text можно преобразовать в число, поэтому ничем не рискуем
    if int(message.text) < 0 or int(message.text) > 24:
        bot.send_message(message.chat.id, "Это неправильное время")
        return
    else:
        # Время введено корректно, можно идти дальше
        bot.send_message(message.chat.id, "Принято")
        dbworker.set_state(message.chat.id, config.States.S_ENTER_HOURS.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_HOURS.value)
def user_entering_hours(message):
    # А вот тут сделаем проверку
    if not message.text.isdigit():
        # Состояние не меняем, поэтому только выводим сообщение об ошибке и ждём дальше
        bot.send_message(message.chat.id, "Что-то не так, попробуй ещё раз!")
        return
    # На данном этапе мы уверены, что message.text можно преобразовать в число, поэтому ничем не рискуем
    if int(message.text) < 3 or int(message.text) > 12:
        bot.send_message(message.chat.id, "Это неправильное время")
        return
    else:
        # Время введёно корректно, можно идти дальше
        bot.send_message(message.chat.id, "Теперь я буду говорить тебе, когда ложиться спать")
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Настройки твоего сна", callback_data="sleep_settings")
        but_2 = types.InlineKeyboardButton(text="Как это работает?", callback_data="how_is_it_work")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Если захочешь что-то изменить, нажимай на кнопки", reply_markup=key)


@bot.callback_query_handler(func=lambda call: True)
def inline_catcher(call):
    if call.data == 'sleep_settings':
        dbworker.set_state(call.message.chat.id, config.States.S_ENTER_TIME.value)
        bot.send_message(call.message, 'Введите новое время пробуждения: ')
    if call.data == 'how_is_it_work':
        hlp(call.message)


# command /help
@bot.message_handler(commands=['help'])
def hlp(message):
    bot.send_message(message.chat.id, messages.help_mes)


bot.polling(none_stop=True)
