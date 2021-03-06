import random
from abc import abstractmethod, ABC

import numpy as np


class BaseField:

    @abstractmethod
    def fill_random_numbers(self, amount_of_numbers):
        pass

    @abstractmethod
    def is_field_empty(self, row, column):
        pass

    @abstractmethod
    def put_number(self, row, column, value):
        pass

    @abstractmethod
    def is_finished(self):
        pass

    @abstractmethod
    def plot(self):
        pass

    @abstractmethod
    def clean(self):
        pass

    @abstractmethod
    def can_put_number(self, row, column, value):
        pass

    @abstractmethod
    def delete_number(self, row, column, value):
        pass


class GameField(BaseField, ABC):

    def __init__(self, amount_of_points: int, saved_state=None):
        super().__init__()
        print("Game is creating!")

        # Судоку всегда 9*9

        # -1 is empty field
        self.field_size = 9

        # If game was saved from user
        if saved_state is not None:
            self.game_field = saved_state

        # Else generate by ourselves
        else:
            self.game_field = np.zeros(shape=(9, 9), dtype=np.int)  # Filled with 0's
            self.fill_random_numbers(amount_of_points)

        # Now we are ready to play!
        print("Now we are ready to play! Plotting field...")
        self.plot()

    def fill_random_numbers(self, amount_of_numbers: int):
        assert 0 <= amount_of_numbers < self.field_size ** 2, "amount of numbers to generate is too small or too big"

        for i in range(amount_of_numbers):

            # Проверка, что на это место мы можем поставить число
            while True:

                row = random.randint(0, self.field_size - 1)
                column = random.randint(0, self.field_size - 1)
                value = random.randint(1, 9)

                if self.can_put_number(row, column, value):
                    self.put_number(row, column, value)
                    break

                else:
                    # print(f"We can not put {value} in ({row}, {column}) field, trying ones again!")
                    continue

    def is_field_empty(self, row, column):

        return self.game_field[row][column] == 0

    def put_number(self, row, column, value):
        assert self.can_put_number(row, column, value), f"Value {value} can not be set in ({row}, {column}) field!"
        assert 0 <= value <= 9

        self.game_field[row][column] = value

    def can_put_number(self, row, column, value):

        # Это поле может быть занято
        if not self.is_field_empty(row, column):
            return False

        # В этом квадрате уже есть эта цифра
        square_x, square_y = row // 3, column // 3
        square = self.game_field[square_x * 3: square_x * 3 + 3, square_y * 3: square_y * 3 + 3]
        if np.any(square == value):
            return False

        # В этой строке уже есть эта цифра
        if np.any(self.game_field[row, :] == value):
            return False

        # В этой столбце уже есть эта цифра
        if np.any(self.game_field[:, column] == value):
            return False

        return True

    def is_finished(self):

        # Неэффективно, можно потом тут ускорить
        return (self.game_field == 0).sum() == 0

    def plot(self):
        print(self.game_field)

    def clean(self):
        del self.game_field

    def delete_number(self, row, column, value):
        assert self.is_field_empty(row, column), "This field is already empty!"

        self.game_field[row, column] = -1

    def find_free_indexes(self):
        for i in range(9):
            for j in range(9):
                if self.game_field[i][j] == 0:
                    return i, j

    def clean_field(self, row, column):
        self.game_field[row][column] = 0
