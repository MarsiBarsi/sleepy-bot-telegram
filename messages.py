# локализация
import dbworker

lang_status = 1

if lang_status == 1:
    help_mes = '''Наш сон - это сложный физиологический процесс, представляющий собой последовательность фаз: бодрствование, быстрый сон (REM), фаза 1, фаза 2, фаза 3 (ранее выделяли фазу 4, однако позже было решено обьединить ее с фазой 3).

Фазы сна можно объеденить в три основные:
Бодрствование - цикл, когда вы просыпаетесь или активно двигаетесь во время сна. Причем, вы не всегда можете помнить эти моменты.
фаза 1 и фаза 2 - легкий сон
фаза 3 и REM - глубокий сон.

Лучше всего просыпаться во время фазы легкого сна, поскольку в этот период ваше тело наиболее восприимчиво к внешней среде и "сонная инерция" (желание спать дальше, вялость, головная боль) ощущается не так сильно.

sleepy bot будет подсчитывать, во сколько вам нужно лечь, чтобы проснуться максимально бодрым'''
    forgotten_name = 'ты забыл ввести свое имя'
    forgotten_time = 'ты забыл ввести время пробуждения'
    forgotten_hours = 'ты забыл ввести продолжительность сна'

    hello_new = 'привет, как тебя зовут?'

    reset_mes = 'хорошо, начнем заново. Как тебя зовут?'

    ok_name = 'Отличное имя, запомню! Теперь укажи, во сколько ты встаешь!'

    num_error = 'Что-то не так, попробуй ещё раз!'
    num_wrong = 'Это неправильное время'
    ok_time = 'принято'

    to_hours = 'теперь введи, сколько часов ты хочешь спать'

    ok_hours = 'Теперь я буду говорить тебе, когда ложиться спать'

    # кнопки:
    sleep_set_but = 'Настройки твоего сна'
    how_but = 'Как это работает?'
    change_mes = 'Если захочешь что-то изменить, нажимай на кнопки'

    # inline catcher:
    new_sets = 'Введите новое время пробуждения: '
else:
    help_mes = '''Our sleep is a complex physiological process...'''
    forgotten_name = 'you forgot to enter your name'
    forgotten_time = 'you forgot to enter the awakening time'
    forgotten_hours = 'you forgot to enter the duration of sleep'

    hello_new = 'Hello what is your name?'

    reset_mes = 'well, let\'s start again. What\'s your name?'

    ok_name = 'Great name! Now tell me when you get up!'

    num_error = 'Something went wrong, try again!'
    num_wrong = 'incorrect time format'
    ok_time = 'accepted'

    to_hours = 'enter how many hours you want to sleep'

    ok_hours = 'Now I will tell you when you should go to bed'

    # кнопки:
    sleep_set_but = 'sleep setting'
    how_but = 'How is it work?'
    change_mes = 'If you want to change something, click on the buttons'

    # inline catcher:
    new_sets = 'Enter the new wake-up time: '
