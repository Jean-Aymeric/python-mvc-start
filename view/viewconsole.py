from shared.boardgame import BoardGame
from shared.iview import IView


class View(IView):
    def display(self, message) -> None:
        print("*" * 100)
        print(message)
        print("*" * 100)

    def displayBoard(self, board: BoardGame) -> None:
        for y in range(board.getHeight()):
            for x in range(board.getWidth()):
                print(board.getAt(x, y).getSprite().getCharacter(), end="")
            print()
        print(board)
