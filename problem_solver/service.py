from problem_solver.chessboard import make_board, KnightFigure, SIZE_OF_BOARD
from problem_solver.models import Board, Field


class KnightFigureService:

    def __init__(self, place):
        self.start_x = int(place[0])
        self.start_y = int(place[1])

    def execute(self):
        board = make_board(self.start_x, self.start_y)
        knight_figure = KnightFigure(board)
        knight_figure.move(self.start_x, self.start_y)
        obj_board = Board.objects.create()
        for i in range(SIZE_OF_BOARD.max + 1):
            for j in range(SIZE_OF_BOARD.max + 1):
                value = board[i][j]
                Field.objects.create(board=obj_board, position_x=i, position_y=j, value=value)
        return board
