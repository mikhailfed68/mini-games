from mini_games import cli
from mini_games.games import list_games


def is_right_answer(right_answer, user_answer):
    if str(right_answer) == user_answer:
        print('Верно!')
        return True
    print(f'Ошибка, правильный ответ: {right_answer} :)')
    return False


def start_game():
    cli.get_greet()
    username = cli.get_username()
    cli.get_rules()
    rounds_count = 1
    mistakes_count = 0
    while rounds_count < 5 and mistakes_count <= 2:
        question, right_answer, RULES = list_games.get_game()
        print(f'\nРаунд {rounds_count}/5, Ошибок: {mistakes_count}')
        print(f'{RULES}')
        print(question)
        if is_right_answer(right_answer, cli.get_user_answer()) is False:
            mistakes_count += 1
        rounds_count += 1
    if mistakes_count == 3:
        return print(f'\nК сожалению, это фиаско {username} ;) Но ты можешь попытаться снова!') # noqa
    return print(f'\nПоздравляю, {username}!')
