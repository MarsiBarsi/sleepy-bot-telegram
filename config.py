from enum import Enum

token = ''
db_file = "database.vdb"

database_name = 'users.db'  # Файл с базой данных

class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_NAME = "1"
    S_ENTER_TIME = "2"
    S_ENTER_HOURS = "3"
