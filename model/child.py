from model.mobile import Mobile
from model.sprite import Sprite
from shared.boardgame import BoardGame


class Child(Mobile):
    def __init__(self, x: int, y: int):
        super().__init__(Sprite("o"), x, y)

    def move(self, boardgame: BoardGame):
        pass
