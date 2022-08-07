import random
from mini_games.games.calculator import get_calculator_example
from mini_games.games.even_num import get_even_num_example
from mini_games.games.prime_num import get_prime_num_example
from mini_games.games.progression import get_progression_example
from mini_games.games.greatest_common_divisor import get_gcd_example


games = [
    get_calculator_example(),
    get_even_num_example(),
    get_prime_num_example(),
    get_progression_example(),
    get_gcd_example(),
]


def get_game():
    game = random.choice(games)
    games.remove(game)
    return game
