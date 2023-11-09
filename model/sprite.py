from shared.isprite import ISprite


class Sprite(ISprite):
    __character: str

    def __init__(self, character: str):
        self.__character = character

    def getCharacter(self) -> str:
        return self.__character

    def getImage(self) -> str:
        return ""
