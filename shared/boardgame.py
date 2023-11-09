from abc import ABC, abstractmethod

from shared.isprite import ISprite


class BoardGame(ABC):
    @abstractmethod
    def getWidth(self) -> int:
        ...

    def getHeight(self) -> int:
        ...

    def getAt(self, x: int, y: int) -> ISprite:
        ...
