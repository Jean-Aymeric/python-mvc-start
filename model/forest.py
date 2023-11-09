import random

from model.grass import Grass
from model.tile import Tile
from model.tree import Tree
from shared.boardgame import BoardGame
from shared.isprite import ISprite


class Forest(BoardGame):
    __field: [[Tile]]
    __height: int
    __width: int
    __tree: Tree
    __grass: Grass

    def __init__(self, height: int, width: int, density: int):
        self.__width = width
        self.__height = height
        self.__field = []
        self.__tree = Tree()
        self.__grass = Grass()
        for row in range(height):
            line = []
            for column in range(width):
                if row == 0 or row == height - 1 or column == 0 or column == width - 1:
                    line.append(self.__tree)
                else:
                    if random.randint(0, 100) < density:
                        line.append(self.__tree)
                    else:
                        line.append(self.__grass)
            self.__field.append(line)

    def getWidth(self) -> int:
        return self.__width

    def getHeight(self) -> int:
        return self.__height

    def getAt(self, x: int, y: int) -> ISprite:
        return self.__field[y][x]
