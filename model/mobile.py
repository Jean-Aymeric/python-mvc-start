from abc import ABC, abstractmethod

from model.sprite import Sprite
from model.tile import Tile
from shared.boardgame import BoardGame


class Mobile(Tile, ABC):
    __x: int
    __y: int

    def __init__(self, sprite: Sprite, x: int, y: int):
        super().__init__(sprite, True)
        self.__x = x
        self.__y = y

    def getX(self) -> int:
        return self.__x

    def getY(self) -> int:
        return self.__y

    def setX(self, x: int):
        self.__x = x

    def setY(self, y: int):
        self.__y = y

    @abstractmethod
    def move(self, boardgame: BoardGame):
        ...
