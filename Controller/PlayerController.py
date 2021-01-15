from abc import ABC

from Controller.BaseController import BaseController
from GameField import GameField
from Saver import GameSaver


class PlayerController(BaseController, ABC):
    def __init__(self):
        super().__init__()

        self.saver = GameSaver()

        amount_of_points = input("How many point to generate? default - 0. $ ")
        amount_of_points = 0 if amount_of_points == "" else int(amount_of_points)

        self.game = GameField(amount_of_points=int(amount_of_points))

    def solve(self) -> bool:

        while not self.game.is_finished():

            wants_to_sleep = input("Wants to save game: yes - 1, no - 0, default: 0. $ ")

            # Need to save game
            if wants_to_sleep == "1":
                self.saver.save_game(self.game)

                while True:
                    resume = input("Want's to resume (1 - yes, 0 - no. default - no)? $ ")
                    if resume == "1":
                        self.game = self.saver.reload_game()
                        break

            row, column, value = PlayerController.validate_line_input()

            if self.game.can_put_number(row, column, value):
                self.game.put_number(row, column, value)
                self.game.plot()

            else:
                print("You can not fill that field with this number!")

        return True

    @staticmethod
    def validate_line_input():
        while True:
            try:
                row, column, value = \
                    map(int, input("Enter row, column and value to put number(in format: $1 5 7). $ ").split())
                assert row >= 0 and column >= 0 and value >= 0
            except ValueError:
                continue

            return row, column, value
