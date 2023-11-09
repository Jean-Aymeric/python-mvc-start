from abc import ABC

from model.sprite import Sprite


class Tile(ABC):
    __sprite: Sprite
    __crossable: bool

    def __init__(self, sprite: Sprite, crossable: bool):
        self.__sprite = sprite
        self.__crossable = crossable

    def getSprite(self) -> Sprite:
        return self.__sprite

    def isCrossable(self) -> bool:
        return self.__crossable
