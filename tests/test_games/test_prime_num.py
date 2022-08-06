from mini_games.games import prime_num


def test_is_prime():
    assert prime_num.is_prime(1) == 'Нет'
    assert prime_num.is_prime(2) == 'Да'
    assert prime_num.is_prime(11) == 'Да'
    assert prime_num.is_prime(15) == 'Нет'


def test_get_prime_num_example():
    expected = prime_num.get_prime_num_example()
    assert isinstance(expected, tuple)
    assert isinstance(expected[0], str)
    assert expected[1] == 'Да' or 'Нет'
    assert expected[2] == 'Задача на нахождение простого числа (Да/Нет)'
