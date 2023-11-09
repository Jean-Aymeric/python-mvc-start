import random

from model.child import Child
from model.mobile import Mobile
from shared.boardgame import BoardGame


class Population():
    __children: [Child]
    __boardgame: BoardGame

    def __init__(self, boardgame: BoardGame):
        self.__children = []
        self.__boardgame = boardgame

    def addChild(self, child: Child):
        self.__children.append(child)

    def getAt(self, x, y) -> [Mobile]:
        mobiles = []
        for child in self.__children:
            if child.getX() == x and child.getY() == y:
                mobiles.append(child)
        return mobiles

    def moveAll(self):
        for child in self.__children:
            child.move(self.__boardgame)

    def addChildren(self, nbChildren: int):
        for i in range(nbChildren):
            self.__children.append(Child(random.randint(1, self.__boardgame.getHeight() - 1),
                                         random.randint(1, self.__boardgame.getWidth() - 1)))
