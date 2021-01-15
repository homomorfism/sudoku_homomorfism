import unittest

from GameField import GameField


class TestGameField(unittest.TestCase):

    def test_can_put_number(self):
        game = GameField(amount_of_numbers=0)

        game.put_number(0, 0, 5)

        # with self.assertRaises(AssertionError):
        #     game.put_number(0, 0, 4)

        game.plot()

        self.assertFalse(game.can_put_number(1, 1, 5))
        # self.assertFalse(game.can_put_number(0, 0, 5))
        # self.assertFalse(game.can_put_number(8, 0, 5))
        # self.assertFalse(game.can_put_number(0, 5, 5))
        #
        # self.assertTrue(game.can_put_number(5, 7, 3))

    def test_saving_gave(self):
        pass
