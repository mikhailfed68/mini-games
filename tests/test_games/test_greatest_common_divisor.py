from mini_games.games import greatest_common_divisor


def test_find_gcd():
    assert greatest_common_divisor.find_gcd(11, 15) == 1
    assert greatest_common_divisor.find_gcd(12, 15) == 3
    assert greatest_common_divisor.find_gcd(20, 20) == 20


def test_get_gcd_example():
    expected = greatest_common_divisor.get_gcd_example()
    assert isinstance(expected, tuple)
    assert isinstance(expected[0], str)
    assert isinstance(expected[1], int)
    assert expected[2] == 'Задача на поиск наибольшего общего делителя'
