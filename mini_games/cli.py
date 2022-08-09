def get_greet():
    print('Приветствую тебя в игре!')
    return None


def get_rules():
    print('''
    Для начала я тебе расскажу правила этой игры ;)

    Правила следующие:
    1) Игра состоит из пяти математических мини-задач
    2) Тебе нужно пройти все 5 задач
    3) Также у тебя есть право на две ошибки
    ''')


def get_start_or_exit():
    return input('Нажми Enter, что бы начать (Или введите "Выйти", что бы закрыть игру) ') # noqa


def get_username():
    username = input('Напиши свое имя :) ')
    print(f'Хорошо, {username}!')
    return username


def get_user_answer():
    return input('Твой ответ: ')
