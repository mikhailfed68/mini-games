import random


def find_gcd(num1, num2):
    while max(num1, num2) % min(num1, num2) != 0:
        lowest = max(num1, num2) % min(num1, num2)
        if num1 > num2:
            num1 = lowest
        else:
            num2 = lowest
    return min(num1, num2)


def get_gcd_example():
    RULES = 'Задача на поиск наибольшего общего делителя'

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'НОД({num1}, {num2}) = ?'
    answer = find_gcd(num1, num2)
    return (question, answer, RULES)
