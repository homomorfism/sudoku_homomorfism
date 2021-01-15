import unittest

import numpy as np

from Controller.PlayerController import PlayerController
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

        self.assertTrue((game.game_field == 0).sum() == 81 - 10)

    def test_saving_and_loading(self):
        game = GameField(amount_of_points=10)
        field = game.game_field

        saver = GameSaver()
        saver.save_game(game)

        game = saver.reload_game()

        self.assertTrue(
            np.array_equal(game.game_field, field)
        )

    def test_can_be_finished(self):
        player_controller = PlayerController()
        player_controller.game.game_field = np.array([
            [5, 8, 1, 6, 7, 2, 4, 3, 9],
            [7, 9, 2, 8, 4, 3, 6, 5, 1],
            [3, 6, 4, 5, 9, 1, 7, 8, 2],

            [4, 3, 8, 9, 5, 7, 2, 1, 6],
            [2, 5, 6, 1, 8, 4, 9, 7, 3],
            [1, 7, 9, 3, 2, 6, 8, 4, 5],

            [8, 4, 5, 2, 1, 9, 3, 6, 7],
            [9, 1, 3, 7, 6, 8, 5, 2, 4],
            [6, 2, 7, 4, 3, 5, 1, 9, 0],
        ])
        player_controller.game.plot()
        player_controller.solve()
