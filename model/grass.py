from model.sprite import Sprite
from model.tile import Tile


class Grass(Tile):
    def __init__(self):
        super().__init__(Sprite("."), True)
