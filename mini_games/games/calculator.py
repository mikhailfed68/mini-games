import random
from operator import add
from operator import mul
from operator import sub
from operator import floordiv


def get_calculator_example():
    RULES = 'Задача на базовые математические операции с числами'
    MATCH_SIGNS = (
        ('+', add),
        ('*', mul),
        ('-', sub),
        (':', floordiv),
    )

    sigh = random.choice(MATCH_SIGNS)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f'{num1} {sigh[0]} {num2} = ?'
    answer = sigh[1](num1, num2)
    return (question, answer, RULES)
