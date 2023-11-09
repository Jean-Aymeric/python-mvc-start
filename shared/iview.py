from abc import ABC, abstractmethod

from shared.boardgame import BoardGame


class IView(ABC):
    @abstractmethod
    def display(self, message) -> None:
        ...

    def displayBoard(self, board: BoardGame) -> None:
        ...
