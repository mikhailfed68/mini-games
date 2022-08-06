import random


def get_even_num_example():
    RULES = 'Задача на определение четности числа'

    num = random.randint(1, 1000)
    question = f'Является ли {num} четным числом? (Да/Нет)'
    answer = 'Да' if num % 2 == 0 else 'Нет'
    return (question, answer, RULES)
