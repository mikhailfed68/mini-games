from mini_games.games import even_num


def test_get_even_num_question():
    expected = even_num.get_even_num_example()
    assert isinstance(expected, tuple)
    assert isinstance(expected[0], str)
    assert expected[1] == 'Да' or 'Нет'
    assert expected[2] == 'Задача на определение четности числа'
