from vedis import Vedis
import config


# Пытаемся узнать из базы «состояние» пользователя
def get_current_state(user_id):
    with Vedis(config.db_file) as db:
        try:
            return db[user_id]
        except KeyError:  # Если такого ключа почему-то не оказалось
            return config.States.S_START.value  # значение по умолчанию - начало диалога

def get_language(user_id):
    with Vedis(config.db_file) as db:
        try:
            return db[user_id+'1']
        except KeyError:  # Если такого ключа почему-то не оказалось
            return '0'  # значение по умолчанию - начало диалога


# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id, value):
    with Vedis(config.db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False

def set_language(user_id, value):
    with Vedis(config.db_file) as db:
        try:
            db[user_id+'1'] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False
