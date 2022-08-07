from mini_games.games import progression


def test_get_progression_example():
    expected = progression.get_progression_example()
    assert isinstance(expected, tuple)
    assert isinstance(expected[0], str)
    assert isinstance(expected[1], int)
    assert expected[2] == 'Задача на поиск пропущенного числа в прогрессии'
