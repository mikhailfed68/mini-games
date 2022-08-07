import random


def get_progression_example():
    RULES = 'Задача на поиск пропущенного числа в прогрессии'

    start = random.randint(0, 50)
    step = random.randint(1, 4)
    end = start + step * 7
    progression = range(start, end, step)
    missing_num = random.choice(progression)

    list_items = [
        '..' if item is missing_num else str(item)
        for item in progression
    ]

    question = ' '.join(list_items)
    return (question, missing_num, RULES)
