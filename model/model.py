from model.forest import Forest
from model.population import Population
from shared.boardgame import BoardGame
from shared.imodel import IModel


class Model(IModel):
    __forest: Forest
    __population: Population

    def __init__(self):
        self.__forest = Forest(20, 40, 7)
        self.__population = Population(self.__forest)
        self.__population.addChildren(10)

    def getBoardGame(self) -> BoardGame:
        return self.__forest
