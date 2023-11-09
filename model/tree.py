from model.sprite import Sprite
from model.tile import Tile


class Tree(Tile):
    def __init__(self):
        super().__init__(Sprite("#"), False)
