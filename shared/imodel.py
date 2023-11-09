from abc import ABC, abstractmethod

from shared.boardgame import BoardGame


class IModel(ABC):
    @abstractmethod
    def getBoardGame(self) -> BoardGame:
        ...
