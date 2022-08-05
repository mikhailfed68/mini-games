from mini_games.games import calculator


def test_get_calculator_question():
    expected = calculator.get_calculator_question()
    assert isinstance(expected, tuple)
    assert isinstance(expected[0], str)
    assert isinstance(expected[1], int)
    assert expected[2] == 'Задача на базовые математические операции с числами'