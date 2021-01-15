from abc import ABC
from Controller.BaseController import BaseController
from Saver import GameSaver
from GameField import GameField


class PlayerController(BaseController, ABC):
    def __init__(self):
        super().__init__()

        self.saver = GameSaver()

        amount_of_points = input("How many point to generate? default - 0. $ ")
        amount_of_points = 0 if amount_of_points == "" else int(amount_of_points)

        self.game = GameField(amount_of_points=int(amount_of_points))

    def solve(self):

        while not self.game.is_finished:
            row, column, value = PlayerController.validate_line_input()

            if self.game.can_put_number(row, column, value):
                self.game.put_number(row, column, value)
                self.game.plot()

            else:
                print("You can not fill that field with this number!")

    @staticmethod
    def validate_line_input():
        while True:
            try:
                row, column, value = \
                    map(int, input("Enter row, column and value to put number(in format: $1 5 7)").split())
                assert row >= 0 and column >= 0 and value >= 0
            except ValueError:
                continue

            return row, column, value
