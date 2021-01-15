import unittest
import numpy as np
from GameField import GameField
from Saver import GameSaver


class TestGameField(unittest.TestCase):

    def test_can_put_number(self):
        game = GameField(amount_of_points=0)

        game.put_number(0, 0, 5)

        # with self.assertRaises(AssertionError):
        #     game.put_number(0, 0, 4)

        game.plot()

        self.assertFalse(game.can_put_number(1, 1, 5))
        self.assertFalse(game.can_put_number(0, 0, 5))
        self.assertFalse(game.can_put_number(8, 0, 5))
        self.assertFalse(game.can_put_number(0, 5, 5))

        self.assertTrue(game.can_put_number(5, 7, 3))

    def test_fill_random_numbers(self):
        game = GameField(amount_of_points=10)

        self.assertTrue((game.game_field == -1).sum() == 81 - 10)

    def test_saving_and_loading(self):
        game = GameField(amount_of_points=10)
        field = game.game_field

        saver = GameSaver()
        saver.save_game(game)

        game = saver.reload_game()

        self.assertTrue(
            np.array_equal(game.game_field, field)
        )
