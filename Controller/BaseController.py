from abc import abstractmethod


class BaseController:

    @abstractmethod
    def solve(self) -> bool:
        pass
