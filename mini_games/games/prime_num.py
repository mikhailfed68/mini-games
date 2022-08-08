import random


def is_prime(num):
    if num < 2:
        return 'Нет'

    divider = 2
    while divider <= num // 2:
        if num % divider == 0:
            return 'Нет'
        divider += 1
    return 'Да'


def get_prime_num_example():
    RULES = 'Задача на нахождение простого числа (Да/Нет)'

    num = random.randint(1, 100)
    question = f'Число {num} является простым?'
    answer = is_prime(num)
    return (question, answer, RULES)
