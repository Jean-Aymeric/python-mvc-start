from shared.icontroller import IController
from shared.imodel import IModel
from shared.iview import IView


class Controller(IController):
    __view: IView
    __model: IModel

    def __init__(self, view: IView, model: IModel):
        self.__view = view
        self.__model = model

    def getView(self) -> IView:
        return self.__view

    def getModel(self) -> IModel:
        return self.__model

    def start(self):
        self.__view.displayBoard(self.__model.getBoardGame())
