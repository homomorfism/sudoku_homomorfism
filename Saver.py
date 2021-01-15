import pickle
from abc import ABC, abstractmethod

from GameField import GameField


class BaseSaver:

    @abstractmethod
    def save_game(self, current_game) -> None:
        pass

    def reload_game(self):
        pass


class GameSaver(BaseSaver, ABC):

    def __init__(self):
        self.file_path = 'save1.pkl'

    def save_game(self, current_game) -> None:
        with open(self.file_path, "wb") as file:
            pickle.dump({"game_field": current_game.game_field, }, file)

    def reload_game(self):
        with open(self.file_path, "rb") as file:
            data = pickle.load(file)

            game = GameField(amount_of_points=0, saved_state=data['game_field'])
            return game
