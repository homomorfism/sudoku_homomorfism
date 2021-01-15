from abc import ABC

from Controller.BaseController import BaseController
from GameField import GameField


class ComputerController(BaseController, ABC):

    def __init__(self):
        super().__init__()

        amount_of_points = input("How many point to generate? default - 0. $ ")
        amount_of_points = 0 if amount_of_points == "" else int(amount_of_points)

        self.game = GameField(amount_of_points=int(amount_of_points))

    def solve(self) -> bool:

        while not self.game.is_finished():
            row, column = self.game.find_free_indexes()

            for value in range(1, 10):
                if self.game.can_put_number(row, column, value):
                    self.game.put_number(row, column, value)

                    if self.solve():
                        return True

                    self.game.clean_field(row, column)

            return False

        self.game.plot()
        return True
