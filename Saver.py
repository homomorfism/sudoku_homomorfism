from abc import ABC, abstractmethod
from GameField import GameField
import pickle


class BaseSaver:

    @abstractmethod
    def save_game(self, current_game) -> None:
        pass

    def reload_game(self):
        pass


class GameSaver(BaseSaver, ABC):

    def __init__(self, path):
        self.file_path = path

    def save_game(self, current_game) -> None:
        with open(self.file_path, "w") as file:
            pickle.dump(current_game.game_field, file)

    def reload_game(self):
        with open(self.file_path, "r") as file:
            game_field = pickle.load(self.file_path)

            game = GameField(amount_of_numbers=0, saved_state=game_field)
            return game
