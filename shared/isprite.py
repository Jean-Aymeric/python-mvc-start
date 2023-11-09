from abc import ABC, abstractmethod


class ISprite(ABC):
    @abstractmethod
    def getCharacter(self) -> str:
        ...

    @abstractmethod
    def getImage(self) -> str:
        ...
