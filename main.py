import telebot
import config
import dbworker


# bot init:
bot = telebot.TeleBot(config.token)


# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):
    state = dbworker.get_current_state(message.chat.id)
    if state == config.States.S_ENTER_NAME.value:
        bot.send_message(message.chat.id, "Забыл ввести имя")
    elif state == config.States.S_ENTER_TIME.value:
        bot.send_message(message.chat.id, "Забыл ввести время пробуждения")
    elif state == config.States.S_SEND_HOURS.value:
        bot.send_message(message.chat.id, "Забыл ввести продолжительность сна")
    else:  # Под "остальным" понимаем состояние "0" - начало диалога
        bot.send_message(message.chat.id, "Привет! Как я могу к тебе обращаться?")
        dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Что ж, начнём по-новой. Как тебя зовут?")
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
        # Возраст введён корректно, можно идти дальше
        bot.send_message(message.chat.id, "Принято")
        dbworker.set_state(message.chat.id, config.States.S_SEND_HOURS.value)


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
        # Возраст введён корректно, можно идти дальше
        bot.send_message(message.chat.id, "окей")

'''
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
    bot.send_message(message.chat.id, 'хорошо, ты будешь вставать в ' + sent.text + ' и спать по ' + hours.text + ' часов')
'''

bot.polling(none_stop=True)